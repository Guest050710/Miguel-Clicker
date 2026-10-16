lazy import rich
from rich import print
from rich.layout import *

# Criar e configurar layouts
layout = Layout()

layout.split_row(
    Layout(name="Nav"),
    Layout(name="Main")
)

layout["Main"].ratio = 3

layout["Main"].split_column(
    Layout(name="Header"),
    Layout(name="Body"),
    Layout(name="Footer")
)

layout["Body"].ratio = 3

# Nomear e deixar bonito layouts
layout["Nav"].update(
    Layout(Panel("",title="Menu", style="cyan",))
)

layout["Header"].update(
    Layout(Panel("",title="Informações", style="red",))
)

layout["Body"].update(
    Layout(Panel("", title="Miguel", style="white",))
)

layout["Footer"].update(
    Layout(Panel("",title="Outros", style="purple",))
)

print(layout)