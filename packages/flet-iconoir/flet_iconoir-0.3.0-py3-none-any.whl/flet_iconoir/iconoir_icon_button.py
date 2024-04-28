import flet as ft
from flet_iconoir.iconoir_icon import IconoirIcon


class IconoirIconButton(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        icon_name: str,
        on_click: callable = None,
        icon_set: str = "regular",
        icon_size: int = 16,
        icon_color: str = ft.colors.ON_PRIMARY,
        hover_color: str = ft.colors.PRIMARY_CONTAINER,
        bg_color: str = ft.colors.ON_PRIMARY_CONTAINER,
        padding: int = 8,
        circular: bool = True,
        border_radius: int = 8,
    ):
        super().__init__()

        self.icon_name = icon_name
        self.icon_set = icon_set
        self.icon_size = icon_size

        self.icon_color = icon_color
        self.bgcolor = bg_color
        self.hover_color = hover_color

        self.page = page

        self.on_click = on_click
        self.padding = padding

        self.circular = circular
        self.border_radius = border_radius

        self.content = IconoirIcon(self.icon_name, self.icon_set, self.icon_color)

        self.shape = ft.BoxShape.CIRCLE if self.circular else ft.BoxShape.RECTANGLE
        self.on_hover = self.highlight

    def highlight(self, e: ft.ControlEvent) -> None:
        if e.data == "true":
            self._hold = self.icon_color
            self.icon_color = self.bgcolor
            self.bgcolor = self.hover_color
        else:
            self.hover_color = self.bgcolor
            self.bgcolor = self.icon_color
            self.icon_color = self._hold

        self.content.color = self.icon_color
        self.page.update()
