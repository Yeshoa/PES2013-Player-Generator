import random
import numpy as np

# comparación posición del jugador 
forwardFix = ["CF", "SS", "LWF", "RWF"]
centerFix = ["DMF", "CMF", "LMF", "RMF", "AMF"]
defenceFix = ["SWP", "CB", "LB", "RB"]
# posiciones para generar 
forward = ["CF", "SS", "LWF", "RWF", "AMF"]
center = ["DMF", "CMF", "LMF", "RMF", "AMF"]
defence = ["SWP", "CB", "LB", "RB", "DMF"]

def generate_pos(position):
  positions = [position]
  # cantidad de posiciones adicionales que va a obtener el jugador 
  quant = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weights=[0.3, 0.4, 0.2, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001])[0]

  for i in range(quant):
    if position in forwardFix:
      # los pesos son las chances de que se genere una habilidad de delantero, medio, defensa 
      additional_position = random.choices([random.choice(forward), random.choice(center), random.choice(defence)], weights=[0.9, 0.095, 0.005])[0]
    elif position in centerFix:
      additional_position = random.choices([random.choice(center), random.choice(forward), random.choice(defence)], weights=[0.7, 0.15, 0.15])[0]
    elif position in defenceFix:
      additional_position = random.choices([random.choice(defence), random.choice(center), random.choice(forward)], weights=[0.95, 0.045, 0.005])[0]

    positions.append(additional_position) if additional_position != position and additional_position not in positions else None
  
  return ", ".join(positions)