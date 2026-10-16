import os
from os import system

lazy import rich
from rich import print
from rich.layout import *
from rich.console import *
from rich.padding import *
from rich.live import *

import readchar
from readchar import readkey, key

import ui

while True:
    with Live(ui.layout, screen=True, auto_refresh=True):
        tecla = readchar.readkey()

        ui.layout["Body"].update(
            Layout(Panel(f"{tecla}"))
        )