import reflex as rx
from ..template import template

@rx.page(route="/resume")
@template
def resume():
    """The resume page."""
    return rx.flex(
        rx.chakra.image(
            src="/resume.jpg",
            width="50%",
            height="100%",
            # border_radius="full",
        ),
        rx.button(
            "Download Resume PDF",
            on_click=rx.download(url="/Lucca_Psaila.pdf"),
            width="20em",
        ),
        align="center",
        justify="center",
        width="100%",
        direction="column",
    )