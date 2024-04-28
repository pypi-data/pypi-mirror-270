from typing import Any, Literal

import flet as ft

from flet_iconoir.icons import get_icon_path


def IconoirIcon(
    icon_name: str,
    icon_set: Literal["regular"] | Literal["solid"] = "regular",
    icon_color: str = None,
    **kwargs
):
    return ft.Image(
        src=get_icon_path(icon_set, icon_name),
        color=icon_color or ft.colors.PRIMARY,
        expand=True,
        fit=ft.ImageFit.CONTAIN,
        **kwargs,
    )
