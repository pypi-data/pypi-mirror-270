#define PY_SSIZE_T_CLEAN
#define RPMALLOC_FIRST_CLASS_HEAPS 1
#include <Python.h>
#include <errno.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include "rpmalloc.h"
#include "rpmalloc.c"

#ifdef better_messages
    #include <string.h>
#endif

struct SecretStorage {
    bool sentinel;
    Py_ssize_t length;
    char data[];
};

struct InterpreterState {
    rpmalloc_heap_t* heap;
};

void m_free(void* m) {
    struct InterpreterState* state = PyModule_GetState(m);
    rpmalloc_heap_free_all(state->heap);
    rpmalloc_heap_release(state->heap);
}

int m_clear(PyObject* mod) {
    PyObject* cls = PyObject_GetAttrString(mod, "Secret");
    if (cls == NULL) {
        return -1;
    }

    Py_CLEAR(cls);
    Py_DECREF(cls);
    return 0;
}

int m_traverse(PyObject* mod, visitproc visit, void* arg) {
    PyObject* cls = PyObject_GetAttrString(mod, "Secret");
    if (cls == NULL) {
        return -1;
    }

    Py_VISIT(cls);
    Py_DECREF(cls);
    return 0;
}

PyModuleDef secret_mod = {
    PyModuleDef_HEAD_INIT,
    .m_name="secret",
    .m_doc=PyDoc_STR(
        "A module for handling secret data in a way to reduce leaks."
    ),
    .m_size=sizeof(struct InterpreterState),
    .m_free=m_free,
    .m_traverse=m_traverse,
    .m_clear=m_clear
};

static void*
map_page(size_t size, size_t alignment, size_t* offset, size_t* mapped_size) {
    void* page = os_mmap(size, alignment, offset, mapped_size);

    if (page == MAP_FAILED) {
        perror("Could not allocate memory.\n");
        #ifdef better_messages
            perror(strerrorname_np(errno));
        #endif
        perror("\n");
        abort();
    }

    if (madvise(page, size, MADV_DONTDUMP)) {
        perror("MADV_DONTDUMP failure: ");
        #ifdef better_messages
            perror(strerrorname_np(errno));
        #endif
        perror("\n");
    }

    if (madvise(page, size, MADV_WIPEONFORK)) {
        perror("MADV_WIPEONFORK failure: ");
        #ifdef better_messages
            perror(strerrorname_np(errno));
        #endif
        perror("\n");
    }

    if (madvise(page, size, MADV_UNMERGEABLE)) {
        perror("MADV_UNMERGEABLE failure: ");
        #ifdef better_messages
            perror(strerrorname_np(errno));
        #endif
        perror("\n");
    }

    if (mlock(page, size)) {
        perror("mlock failure: ");
        #ifdef better_messages
            perror(strerrorname_np(errno));
        #endif
        perror("\n");
    }

    return page;
}


PyObject *reveal(PyObject* self, PyObject* Py_UNUSED(unsused)) {
    PyObject* mod = PyState_FindModule(&secret_mod);
    PyTypeObject* cls = (PyTypeObject*)PyObject_GetAttrString(mod, "Secret");

    if (cls == NULL) {
        return NULL;
    }

    struct SecretStorage** self_slot = PyObject_GetTypeData(self, cls);

    if (!(*self_slot)->sentinel) {
        Py_DECREF(cls);
        return Py_None;
    }

    PyObject* string = PyUnicode_DecodeUTF8(
        (*self_slot)->data,
        (*self_slot)->length,
        "strict"
    );

    if (string == NULL) {
        Py_DECREF(cls);
        return NULL;
    }

    Py_DECREF(cls);
    return string;
}

PyObject *tp_repr(PyObject* Py_UNUSED(self)) {
    return PyUnicode_InternFromString("<Secret Redacted>");
}

void tp_dealloc(PyObject* self) {
    PyObject* mod = PyState_FindModule(&secret_mod);
    PyTypeObject* cls = (PyTypeObject*)PyObject_GetAttrString(mod, "Secret");

    if (cls == NULL) {
        return;
    }

    struct InterpreterState* state = PyModule_GetState(mod);
    struct SecretStorage** self_slot = PyObject_GetTypeData(self, cls);

    PyTypeObject *tp = Py_TYPE(self);
    Py_INCREF(tp);
    tp->tp_clear(self);
    tp->tp_free(self);
    Py_DECREF(tp);
    Py_DECREF(cls);
    rpmalloc_heap_free(state->heap, *self_slot);
}

int tp_clear(PyObject* self) {
    PyTypeObject* tp = Py_TYPE(self);
    Py_CLEAR(tp);
    return 0;
}

int tp_traverse(PyObject *self, visitproc visit, void *arg) {
    PyTypeObject* tp = Py_TYPE(self);
    Py_VISIT(tp);
    return 0;
}

int tp_init(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject* object;

    static char* names[] = {"", NULL};

    bool parse_result = !PyArg_ParseTupleAndKeywords(
        args,
        kwds,
        "O:Secret",
        names,
        &object
    );

    if (parse_result) {
        return -1;
    }

    PyObject* string = PyObject_Str(object);
    Py_ssize_t len;
    const char* data_buffer = PyUnicode_AsUTF8AndSize(string, &len);

    if (data_buffer == NULL) {
        return -1;
    }

    PyObject* mod = PyState_FindModule(&secret_mod);
    struct InterpreterState* state = PyModule_GetState(mod);

    struct SecretStorage* storage_buffer = rpmalloc_heap_alloc(
        state->heap,
        sizeof(struct SecretStorage) + (sizeof(char) * len)
    );

    storage_buffer->sentinel = true;
    storage_buffer->length = len;
    memcpy(&(storage_buffer->data), data_buffer, len);
    Py_DECREF(string);
    PyTypeObject* cls = (PyTypeObject*)PyObject_GetAttrString(mod, "Secret");

    if (cls == NULL) {
        return -1;
    }

    struct SecretStorage** self_slot = PyObject_GetTypeData(self, cls);
    *self_slot = storage_buffer;

    Py_DECREF(cls);

    return 0;
}

PyMethodDef methods[] = {
    {
        .ml_name="reveal",
        .ml_meth=(PyCFunction)reveal,
        .ml_flags=METH_NOARGS,
        .ml_doc=PyDoc_STR("Return the secret in the form of a string.")
    },
    {NULL}
};

PyType_Slot type_slot[] = {
    {
        .slot=Py_tp_doc,
        .pfunc=PyDoc_STR("A secret stored safely in memory."),
    },
    {
        .slot=Py_tp_repr,
        .pfunc=tp_repr,
    },
    {
        .slot=Py_tp_init,
        .pfunc=tp_init,
    },
    {
        .slot=Py_tp_methods,
        .pfunc=methods,
    },
    {
        .slot=Py_tp_dealloc,
        .pfunc=tp_dealloc,
    },
    {
        .slot=Py_tp_traverse,
        .pfunc=tp_traverse,
    },
    {
        .slot=Py_tp_clear,
        .pfunc=tp_clear,
    },
    {0, 0}
};



PyType_Spec SecretSpec = {
    .name="omniblack.secret.Secret",
    .basicsize=-(Py_ssize_t)sizeof(struct SecretStorage*),
    .flags=Py_TPFLAGS_IMMUTABLETYPE | Py_TPFLAGS_HAVE_GC,
    .slots=type_slot,
};


rpmalloc_interface_t mapping_interface = {
    .memory_map=map_page,
    .memory_commit=os_mcommit,
    .memory_decommit=os_mdecommit,
    .memory_unmap=os_munmap
};

rpmalloc_config_t allocator_config = {
    .page_size=0,
    .enable_huge_pages=0,
    .unmap_on_finalize=1,
    .disable_decommit=0,
    .page_name="secret heap",
    .huge_page_name="huge secret heap"
};

PyMODINIT_FUNC PyInit_secret(void) {
    rpmalloc_initialize_config(&mapping_interface, &allocator_config);
    PyObject* mod = PyModule_Create(&secret_mod);
    if (mod == NULL) {
        return NULL;
    }

    PyObject* type = PyType_FromModuleAndSpec(mod, &SecretSpec, NULL);

    if (PyModule_AddObjectRef(mod, "Secret", type)) {
        return NULL;
    }

    struct InterpreterState* state = PyModule_GetState(mod);
    state->heap = rpmalloc_heap_acquire();
    Py_DECREF(type);
    Py_DECREF(mod);

    return mod;
}
