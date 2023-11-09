from typing import Any, Dict

from setuptools import Extension

cflags = ['-std=c99']
ext_modules = [
    Extension(
        "streamdeck_uinput._uinput", ["streamdeck_uinput/uinput.c"],
        extra_compile_args=cflags,
    ),
]


def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
        }
    )