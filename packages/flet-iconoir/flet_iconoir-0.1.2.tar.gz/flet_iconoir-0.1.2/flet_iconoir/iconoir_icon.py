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

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "icon_color":
            self.icon_color = value
        elif name == "icon_name":
            self.icon_name = value
        elif name == "icon_set":
            self.icon_set = value
        elif name == "icon_size":
            self.icon_size = value

        return super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        if name == "icon_name":
            return self.icon_name
        if name == "icon_set":
            return self.icon_set
        if name == "icon_size":
            return self.icon_size
        if name == "icon_color":
            return self.icon_color

        return super().__getattribute__(name)
