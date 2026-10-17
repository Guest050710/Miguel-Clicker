import rich.align
from rich.layout import *
from rich.text import *
from rich.table import *

import engine

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
    Layout(Panel(""))
)

layout["Body"].update(
    Layout(Panel(""))
)

layout["Footer"].update(
    Layout(Panel("",title="Outros", style="purple",))
)

# Criar textos para os painéis

def displayBody():
    linhaBody = Table.grid(expand=True)
    linhaBody.add_column(justify="left")
    linhaBody.add_column(justify="right")
    linhaBody.add_row(f"Dinheiro [green]($)[reset]: {engine.jogador.dinheiro} ", f"Dinheiro por segundo [green](DPS)[reset]: {engine.jogador.dps}")

    layout["Body"].update(
        Layout(Panel(linhaBody)))

def displayHeader():
    linhaHeader = Table.grid(expand=True)
    linhaHeader.add_column(justify="left")
    linhaHeader.add_column(justify="right")
    linhaHeader.add_row("MIGUEL CLICKER ", f"[bold white]Versão:[reset] [italic]{engine.version}")

    layout["Header"].update(
        Layout(Panel(Align(linhaHeader, vertical="middle"))))