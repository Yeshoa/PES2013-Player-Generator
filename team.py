import random
import numpy as np
from player import generate_player, save_to_txt


# Generar jugadores de diferentes posiciones
positions_to_generate = ["CF", "WG", "LB", "CMF", "CB"]
players = [generate_player(position) for position in positions_to_generate]

# Guardar los jugadores en un archivo de texto
save_to_txt(players)
print("Players saved to players.txt")