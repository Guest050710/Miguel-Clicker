import os
import time
from os import system

lazy import rich
from rich import print
from rich.layout import *
from rich.console import *
from rich.padding import *
from rich.live import *
from rich.align import *

from concurrent.futures import ThreadPoolExecutor

import readchar
from readchar import readkey, key

import ui
import engine

def loopDisplay():
    with (Live(ui.layout, screen=True, auto_refresh=True, refresh_per_second=30)):
        while True:
            ui.displayBody()

            time.sleep(0.01)

def loopInput():
    while True:
        tecla = readchar.readkey()

        if tecla == "z":
            engine.jogador.adicionarDinheiro()

with ThreadPoolExecutor(max_workers=2) as executor:
    # Roda duas tarefas ao mesmo tempo
    executor.submit(loopDisplay)
    executor.submit(loopInput)