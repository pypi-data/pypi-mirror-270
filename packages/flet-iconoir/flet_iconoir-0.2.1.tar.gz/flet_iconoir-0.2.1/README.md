# flet iconoir

> the [Iconoir](https://iconoir.com/) library, wrapped for [Flet](https://flet.dev/).

## usage

adds a new `IconoirIcon` function. use it like this with a name from the [Iconoir](https://iconoir.com/) list!

```python
page.add(
    IconoirIcon(
        icon_name="wifi",
        icon_set="regular",  # or "solid" !
        icon_size=32,  # default
        icon_color=ft.colors.PRIMARY,  # default
        **kwargs,  # passed to the flet.Image this thing returns!
    )
)
```

quick, dirty, simple, hopefully helpful. find me on [github](https://github.com/hexbenjamin) and reach out if you have questions. have a day!
