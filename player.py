import random
import numpy as np
from stats import generate_stats
from pos import generate_pos
from skills import generate_skills
from awareness import generate_att, generate_def

def calculate_imc(weight, length):
    # Calcula el IMC usando la fórmula: IMC = peso (kg) / (altura (m) ** 2)
    return weight / ((length / 100) ** 2)

def generate_player(position, rating, number):
    player = {}

    name = "Player"
    positions = generate_pos(position) # posiciones adicionales

    player["Name"] = name
    player["Shirt Name"] = name
    player["Number"] = number
    player["Foot"] = random.choices(["R", "L"], weights=[0.8, 0.2])[0]
    player["Positions"] = position + "* "+ positions
    player["Injury Tolerance"] = random.choices(["A", "B", "C"], weights=[0.8, 0.15, 0.05])[0]

    player["Condition/Fitness"] = random.randint(1, 8)
    player["Weak Foot Accuracy"] = random.randint(1, 8)
    player["Weak Foot Frequency"] = random.randint(1, 8)
    player["Attack Awareness"] = generate_att(position)
    player["Defence Awareness"] = generate_def(position)

    # Generación utilizando distribución gaussiana
    player["Age"] = int(np.random.normal(28, 8))  # Media 28, Desviación estándar 8
    player["Length"] = int(np.random.normal(182, 18))  # Media 178, Desviación estándar 20
    player["Weight"] = int(np.random.normal(78, 10))  # Media 78, Desviación estándar 10

    # Asegurarse de que las edades estén dentro del rango 15-50
    player["Age"] = max(min(player["Age"], 45), 15)
    # Asegurarse de que las longitudes estén dentro del rango 148-220
    player["Length"] = max(min(player["Length"], 220), 148)
    # Asegurarse de que los pesos estén dentro del rango 30-128
    player["Weight"] = max(min(player["Weight"], 128), 30)

    # Definir el rango de IMC realista para un futbolista
    min_imc = 20
    max_imc = 24

    # Calcular el IMC y ajustar el peso si es necesario para que esté dentro del rango
    imc = calculate_imc(player["Weight"], player["Length"])
    if imc < min_imc:
        # Ajustar el peso para lograr el IMC mínimo
        adjusted_weight = int((min_imc * ((player["Length"] / 100) ** 2)))
        player["Weight"] = max(min(adjusted_weight, 128), 30)  # Asegurarse del rango nuevamente
    elif imc > max_imc:
        # Ajustar el peso para lograr el IMC máximo
        adjusted_weight = int((max_imc * ((player["Length"] / 100) ** 2)))
        player["Weight"] = max(min(adjusted_weight, 128), 30)  # Asegurarse del rango nuevamente

    player["STATS"] = generate_stats(position, rating)
    player["SKILLS"] = generate_skills(position, positions, rating)

    return player

def save_to_txt(players):
    with open("players.txt", "w") as file:
        for player in players:
            file.write("Name: {}\n".format(player["Name"]))
            file.write("Shirt Name: {}\n".format(player["Shirt Name"]))
            file.write("Number: {}\n".format(player["Number"]))
            file.write("Foot: {}\n".format(player["Foot"]))
            file.write("Position: {}\n".format(player["Positions"]))
            file.write("Injury Tolerance: {}\n".format(player["Injury Tolerance"]))
            file.write("Age: {}\n".format(player["Age"]))
            file.write("Height: {}\n".format(player["Length"]))
            file.write("Weight: {}\n".format(player["Weight"]))
            file.write("Form: {}\n".format(player["Condition/Fitness"]))
            file.write("Weak Foot Accuracy: {}\n".format(player["Weak Foot Accuracy"]))
            file.write("Weak Foot Frequency: {}\n".format(player["Weak Foot Frequency"]))
            file.write("Attack Awareness: {}\n".format(player["Attack Awareness"]))
            file.write("Defence Awareness: {}\n\n".format(player["Defence Awareness"]))

            if "STATS" in player:
                file.write("Stats:\n")
                for stat, stat_value in player["STATS"].items():
                    file.write("  {}: {}\n".format(stat, stat_value))

            if "SKILLS" in player:
                file.write("Skills:\n")
                for skill in player["SKILLS"]:
                    file.write(" {}\n".format(skill))
            file.write("\n" + "-" * 20 + "\n")

players = []
players.append(generate_player("CMF", 90, 9))

save_to_txt(players)
print("Players saved to players.txt")
