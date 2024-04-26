from typing import Any, Literal

import flet as ft

from flet_iconoir.icons import get_icon_path


class IconoirIcon(ft.Container):
    def __init__(
        self,
        icon_name: str,
        icon_set: Literal["regular"] | Literal["solid"] = "regular",
        icon_size: int = 32,
        icon_color: str = None,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)

        self.icon_set = icon_set
        self.icon_size = icon_size
        self.icon_color = icon_color

        self.icon_name = icon_name

        self.content = ft.Image(
            src=get_icon_path(self.icon_set, self.icon_name),
            color=self.icon_color or ft.colors.PRIMARY,
            expand=True,
        )

        self.width = self.icon_size
        self.height = self.icon_size
