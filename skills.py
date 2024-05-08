import random
import numpy as np

playstyles = {
    'P01 - Classic No.10': ['CMF', 'AMF'],
    'P02 - Anchor Man': ['DMF', 'CMF'],
    'P03 - Trickster': ['RMF', 'LMF', 'RWF', 'LWF', 'SS'],
    'P04 - Darting Run': ['RMF', 'LMF', 'RWF', 'LWF', 'SS'],
    'P05 - Mazing Run': ['RMF', 'LMF', 'RWF', 'LWF', 'SS'],
    'P06 - Pinpoint Pass': ['CB', 'RB', 'LB', 'DMF', 'CMF', 'SWP'],
    'P07 - Early Cross': ['RB', 'LB', 'RMF', 'LMF', 'RWF', 'LWF'],
    'P08 - Box to Box': ['DMF', 'CMF', 'AMF', 'RMF', 'LMF'],
    'P09 - Incisive Run': ['RB', 'LB', 'RMF', 'LMF', 'RWF', 'LWF'],
    'P10 - Long Ranger': ['CB', 'RB', 'LB', 'DMF', 'CMF', 'AMF', 'RMF', 'LMF', 'SWP'],
    'P11 - Enforcer': ['DMF', 'CMF'],
    'P12 - Goal Poacher': ['SS', 'CF'],
    'P13 - Dummy Runner': ['SS', 'CF'],
    'P14 - Free Roaming': ['CMF', 'AMF', 'RMF', 'LMF'],
    'P15 - Talisman': ['CMF', 'AMF', 'RMF', 'LMF'],
    'P16 - Fox in the Box': ['CF'],
    'P17 - Offensive Sideback': ['CB', 'RB', 'LB', 'SWP'],
    'P18 - Track Back': ['SS', 'CF']
}
# posibilidades de que le salga tal skill a un: delantero, medio, defensor, arquero
weights_skills = {
  'S01 - 1-touch Play': [1, 1, 1, 1], 'S02 - Outside Curve': [1, 1, 1, 0.1], 'S03 - Long Throw': [1, 1, 1, 0.1], 
  'S04 - Super-Sub': [1, 1, 1, 1], 'S05 - Speed Merchant': [1, 1, 0.5, 0.5], 'S06 - Long Range Drive': [1, 1, 0.1, 0.01], 
  'S07 - Shoulder Feint Skills': [1, 1, 0.1, 0.01], 'S08 - Turning Skills': [1, 1, 0.1, 0.01], 'S09 - Roulette Skills': [1, 1, 0.1, 0.01], 
  'S10 - Flip Flap Skills': [1, 1, 0.1, 0.01], 'S11 - Flicking Skills': [1, 1, 0.1, 0.01], 'S12 - Scissors Skills': [1, 1, 0.1, 0.01], 
  'S13 - Step On Skills': [1, 1, 0.1, 0.01], 'S14 - Deft Touch Skills': [1, 1, 0.1, 0.01], 'S15 - Knuckle Shot': [1, 1, 0.1, 0.01], 
  'S16 - Jumping Volley': [1, 1, 0.1, 0.01], 'S17 - Scissor Kick': [1, 1, 0.1, 0.01], 'S18 - Heel Flick': [1, 1, 1, 0.01], 
  'S19 - Weighted Pass': [0.5, 1, 1, 0.01], 'S20 - Double Touch': [1, 1, 0.1, 0.01], 'S21 - Run Around': [1, 1, 0.1, 0.01], 
  'S22 - Sombrero': [1, 1, 0.1, 0.01], 'S23 - 180 Drag': [1, 1, 0.1, 0.01], 'S24 - Lunging Tackle': [0.01, 0.5, 10, 0.01], 
  'S25 - Diving Header': [1, 0.5, 1, 0.01], 'S26 - GK Long Throw': [0.001, 0.001, 0.001, 25]
}

fow_weights_dict = {skill: weights[0] for skill, weights in weights_skills.items()}
med_weights_dict = {skill: weights[1] for skill, weights in weights_skills.items()}
def_weights_dict = {skill: weights[2] for skill, weights in weights_skills.items()}
gk_weights_dict = {skill: weights[3] for skill, weights in weights_skills.items()}

forwardFix = ["CF", "SS", "LWF", "RWF"]
centerFix = ["DMF", "CMF", "LMF", "RMF", "AMF"]
defenceFix = ["SWP", "CB", "LB", "RB"]

def generate_weights(rating):
    weights = [40, 60, 70, 75, 80, 82, 85, 88, 90, 93, 96, 99]
    # Cuanto mayor sea el rating, mayor será el peso en la lista finalWeights
    # adjusted_weights = [ max(rating - abs(weight - rating), 1) for weight in weights]
    adjusted_weights = [ (min((rating / weight) ** 10, 10) if rating >= weight else max((weight-rating) **-1, 0.0001) ) for weight in weights]
    # print(adjusted_weights)
    return adjusted_weights

def generate_skills(position, positions, rating):
  finalWeights = generate_weights(rating)
  quant = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], weights= finalWeights)[0]
  skills = []
  for _ in range(quant):
    if random.randint(1, 10) > 8 and position != "GK":
      newSkill = generate_playstyle(position)
    else:
      newSkill = generate_skill(position)
    if newSkill not in skills:
      skills.append(newSkill)
  # generar skills en base a la posicion principal y con algun random basado en el rating 
  return skills

def generate_skill(position):
  column = 3
  if position in forwardFix:
    column = 0
  elif position in centerFix:
    column = 1
  elif position in defenceFix:
    column = 2
  # Obtener las habilidades y pesos de la columna elegida
  skills_weights = list(weights_skills.items())
  skills, weights = zip(*skills_weights)
  weights_column = [w[column] for w in weights]

  # Elegir una habilidad basada en los pesos de la columna
  chosen_skill = random.choices(skills, weights=weights_column, k=1)[0]
  return chosen_skill

def generate_playstyle(position):
  # Filtrar los playstyles que contienen la posición especificada
  eligible_playstyles = [ps for ps, pos_list in playstyles.items() if position in pos_list]
  
  # Seleccionar aleatoriamente uno de los playstyles elegibles
  chosen_playstyle = random.choice(eligible_playstyles)
  
  return chosen_playstyle

""" rate=109
print(rate)
pos = "AMF"
pos2 = ["CF", "SS"]
players = []
length_counts = [0] * 12 
for _ in range(100000):
  players.append(generate_skills(pos, pos2, rate))

for player in players:
  length = len(player)
  length_counts[length] += 1
for length, count in enumerate(length_counts):
    print(f'Len {length}: {count}') """
""" for player in players:
  print(len(player), end=' - ') """
