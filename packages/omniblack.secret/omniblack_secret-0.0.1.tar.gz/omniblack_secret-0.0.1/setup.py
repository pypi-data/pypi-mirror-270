from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="omniblack.secret",
            include_dirs=[
                'include',
                '/usr/include/python3.12',
            ],
            extra_compile_args=[
                '-Wall',
                '-Wextra',
                '-std=gnu17',
            ],
            extra_link_args=[
                #'-Wl,--no-undefined',
            ],
            sources=[
                'secret.c',
            ],
        ),
    ]
)
