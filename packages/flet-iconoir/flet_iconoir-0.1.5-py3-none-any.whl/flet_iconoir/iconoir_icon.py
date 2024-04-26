from typing import Any, Literal

import flet as ft

from flet_iconoir.icons import get_icon_path


def IconoirIcon(
    icon_name: str,
    icon_set: Literal["regular"] | Literal["solid"] = "regular",
    icon_size: int = 32,
    icon_color: str = None,
    **kwargs
):
    return ft.Image(
        src=get_icon_path(icon_set, icon_name),
        color=icon_color or ft.colors.PRIMARY,
        width=icon_size,
        height=icon_size,
        **kwargs,
    )
