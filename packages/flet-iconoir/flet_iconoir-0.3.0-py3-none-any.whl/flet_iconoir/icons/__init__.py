# import importlib.resources as pkg_resources
from typing import Literal

from flet_iconoir.icons import regular, solid


library = {"regular": regular, "solid": solid}


def get_icon_path(icon_set: Literal["regular"] | Literal["solid"], name: str) -> str:
    # return pkg_resources.files(library[icon_set]) / f"{name}.svg"
    return (
        f"https://github.com/iconoir-icons/iconoir/raw/main/icons/{icon_set}/{name}.svg"
    )


__all__ = ["IconLibrary"]
