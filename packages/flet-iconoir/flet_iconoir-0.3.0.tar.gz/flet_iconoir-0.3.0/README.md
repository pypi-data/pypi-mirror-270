# flet iconoir

> the [Iconoir](https://iconoir.com/) library, wrapped for [Flet](https://flet.dev/).

## usage

adds a new `IconoirIcon` function. use it like this with a name from the [Iconoir](https://iconoir.com/) list!

```python
page.add(
    IconoirIcon(
        icon_name="wifi",
        icon_set="regular",  # or "solid" !
        icon_color=ft.colors.PRIMARY,  # default
        **kwargs,  # passed to the flet.Image this thing returns!
    )
)
```

also adds the `IconoirIconButton`, which is a class with more parameters.

```python
page.add(
    IconoirIconButton(
        page=page,  # reference to the page this button will be on
        icon_name="settings",
        icon_set="regular",
        on_click=lambda: print("clicked!"),  # defaults to None
        icon_size=16,
        icon_color=ft.colors.ON_PRIMARY,
        hover_color=ft.colors.PRIMARY_CONTAINER,
        bg_color=ft.colors.ON_PRIMARY_CONTAINER,
        padding=8,
        circular=True,
        border_radius=8,  # for when circular is False
    )
)
```

quick, dirty, simple, hopefully helpful. find me on [github](https://github.com/hexbenjamin) and reach out if you have questions. have a day!
