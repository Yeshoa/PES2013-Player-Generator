import random
import math
import numpy as np
nulo = 0.4
bot = 0.85
bajo = 0.88
medio = 0.93
lbalto = 0.931
alto = 0.97
top = 1

def generate_stats(position, rating):
    stats = {}
    # el valor promedio de las habilidades clave es rating/key_mean[position]
    # mean = rating/key_mean[position]
    mean = rating/2.1+44

    for stat, weight in stats_weights[position].items():
        # Calcular el valor medio ajustado
        if (weight > medio):
            std_dev = 4  # Desviación habilidades clave
        else: 
            std_dev = random.uniform(4, 12) # desviación random
        adjusted_mean = (mean + 1) * weight # en las habilidades no clave para nada para nada usar un random con alta desviación
        value = int(np.random.normal(adjusted_mean, std_dev))
        value = max(value, 0)  # Asegurarse de que no sea negativo
        if value <= mean-25 and weight > bot: # si la habilidad random es demasiado baja para lo que es el jugador, le suma 20 para compensar un poco
            print(stat, value, mean-25, value+20)
            value += 20
        value = min(value, 99)  # Asegurarse de que esté entre 0 y 99
        stats[stat] = value
    return stats

# Definir promedio habilidades clave por posición
key_mean = {
    "GK": 1, "SWP": 1, "CB": 1, "LB": 1, "RB": 1, "DMF": 1, "CMF": 1, "LMF": 1, "RMF": 1, "AMF": 1, "LWF": 1, "RWF": 1, "SS": 1, "CF": 2.1+44
}
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
""" HACER UNA GLOBAL PARA TWK TEN FK CUR """
# Definir habilidades y sus pesos por posición
stats_weights = {
    "GK": {
        "Attack": nulo, "Defence": top, "Header Accuracy": bot, "Dribble Accuracy": bot, "Short Pass Accuracy": bot, "Short Pass Speed": bot,
        "Long Pass Accuracy": bot, "Long Pass Speed": bot, "Shot Accuracy": bot, "Place Kicking": bot, "Swerve": bot, "Ball Controll": bot,
        "Goal Keeping Skills": nulo, 
        "Response": top, "Explosive Power": top, "Dribble Speed": bot, "Top Speed": bot, 
        "Body Balance": top, "stamina": bot, "Kicking Power": medio, "Jump": alto, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "SWP": {
        "Attack": nulo, "Defence": top, "Header Accuracy": alto, "Dribble Accuracy": bot, "Short Pass Accuracy": bajo, "Short Pass Speed": bajo,
        "Long Pass Accuracy": bajo, "Long Pass Speed": bajo, "Shot Accuracy": bot, "Place Kicking": medio, "Swerve": medio, "Ball Controll": bajo,
        "Goal Keeping Skills": nulo, 
        "Response": top, "Explosive Power": medio, "Dribble Speed": bot, "Top Speed": alto, 
        "Body Balance": top, "stamina": top, "Kicking Power": alto, "Jump": top, 
        "Tenacity": top, "Teamwork": alto,
    },
    "CB": {
        "Attack": nulo, "Defence": top, "Header Accuracy": medio, "Dribble Accuracy": bot, "Short Pass Accuracy": bajo, "Short Pass Speed": bajo,
        "Long Pass Accuracy": bajo, "Long Pass Speed": bajo, "Shot Accuracy": bot, "Place Kicking": medio, "Swerve": medio, "Ball Controll": bot,
        "Goal Keeping Skills": nulo, 
        "Response": top, "Explosive Power": medio, "Dribble Speed": bot, "Top Speed": alto, 
        "Body Balance": top, "stamina": top, "Kicking Power": bajo, "Jump": top, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "LB": {
        "Attack": lbalto, "Defence": lbalto, "Header Accuracy": bajo, "Dribble Accuracy": lbalto, "Short Pass Accuracy": medio, "Short Pass Speed": medio,
        "Long Pass Accuracy": lbalto, "Long Pass Speed": lbalto, "Shot Accuracy": bajo, "Place Kicking": medio, "Swerve": medio, "Ball Controll": bajo,
        "Goal Keeping Skills": nulo, 
        "Response": lbalto, "Explosive Power": lbalto, "Dribble Speed": lbalto, "Top Speed": lbalto, 
        "Body Balance": lbalto, "stamina": lbalto, "Kicking Power": bajo, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "RB": {
        "Attack": lbalto, "Defence": lbalto, "Header Accuracy": bajo, "Dribble Accuracy": lbalto, "Short Pass Accuracy": medio, "Short Pass Speed": medio,
        "Long Pass Accuracy": lbalto, "Long Pass Speed": lbalto, "Shot Accuracy": bajo, "Place Kicking": medio, "Swerve": medio, "Ball Controll": bajo,
        "Goal Keeping Skills": nulo, 
        "Response": lbalto, "Explosive Power": lbalto, "Dribble Speed": lbalto, "Top Speed": lbalto, 
        "Body Balance": lbalto, "stamina": lbalto, "Kicking Power": bajo, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "DMF": {
        "Attack": alto, "Defence": top, "Header Accuracy": bajo, "Dribble Accuracy": alto, "Short Pass Accuracy": top, "Short Pass Speed": top,
        "Long Pass Accuracy": top, "Long Pass Speed": top, "Shot Accuracy": bot, "Place Kicking": medio, "Swerve": medio, "Ball Controll": alto,
        "Goal Keeping Skills": nulo, 
        "Response": medio, "Explosive Power": bajo, "Dribble Speed": alto, "Top Speed": bajo, 
        "Body Balance": alto, "stamina": top, "Kicking Power": bajo, "Jump": medio, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "CMF": {
        "Attack": alto, "Defence": alto, "Header Accuracy": alto, "Dribble Accuracy": top, "Short Pass Accuracy": top, "Short Pass Speed": top,
        "Long Pass Accuracy": top, "Long Pass Speed": alto, "Shot Accuracy": bot, "Place Kicking": medio, "Swerve": medio, "Ball Controll": alto,
        "Goal Keeping Skills": nulo, 
        "Response": medio, "Explosive Power": bajo, "Dribble Speed": top, "Top Speed": bajo, 
        "Body Balance": top, "stamina": top, "Kicking Power": bajo, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "LMF": {
        "Attack": top, "Defence": bajo, "Header Accuracy": bajo, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": top, "Long Pass Speed": alto, "Shot Accuracy": bajo, "Place Kicking": medio, "Swerve": medio, "Ball Controll": alto,
        "Goal Keeping Skills": nulo, 
        "Response": bajo, "Explosive Power": top, "Dribble Speed": top, "Top Speed": top, 
        "Body Balance": alto, "stamina": top, "Kicking Power": bajo, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "RMF": {
        "Attack": top, "Defence": bajo, "Header Accuracy": bajo, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": top, "Long Pass Speed": alto, "Shot Accuracy": bajo, "Place Kicking": medio, "Swerve": medio, "Ball Controll": alto,
        "Goal Keeping Skills": nulo, 
        "Response": bajo, "Explosive Power": top, "Dribble Speed": top, "Top Speed": top, 
        "Body Balance": alto, "stamina": top, "Kicking Power": bajo, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "AMF": {
        "Attack": top, "Defence": nulo, "Header Accuracy": bajo, "Dribble Accuracy": top, "Short Pass Accuracy": top, "Short Pass Speed": top,
        "Long Pass Accuracy": alto, "Long Pass Speed": alto, "Shot Accuracy": medio, "Place Kicking": medio, "Swerve": medio, "Ball Controll": top,
        "Goal Keeping Skills": nulo, 
        "Response": bajo, "Explosive Power": bajo, "Dribble Speed": alto, "Top Speed": alto, 
        "Body Balance": alto, "stamina": top, "Kicking Power": alto, "Jump": alto, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "LWF": {
        "Attack": alto, "Defence": nulo, "Header Accuracy": bajo, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": top, "Long Pass Speed": top, "Shot Accuracy": top, "Place Kicking": medio, "Swerve": medio, "Ball Controll": medio,
        "Goal Keeping Skills": nulo, 
        "Response": medio, "Explosive Power": top, "Dribble Speed": top, "Top Speed": top, 
        "Body Balance": alto, "stamina": alto, "Kicking Power": top, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "RWF": {
        "Attack": alto, "Defence": nulo, "Header Accuracy": bajo, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": top, "Long Pass Speed": top, "Shot Accuracy": top, "Place Kicking": medio, "Swerve": medio, "Ball Controll": medio,
        "Goal Keeping Skills": nulo, 
        "Response": medio, "Explosive Power": top, "Dribble Speed": top, "Top Speed": top, 
        "Body Balance": alto, "stamina": alto, "Kicking Power": top, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "SS": {
        "Attack": alto, "Defence": nulo, "Header Accuracy": medio, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": bajo, "Long Pass Speed": bajo, "Shot Accuracy": top, "Place Kicking": medio, "Swerve": medio, "Ball Controll": top,
        "Goal Keeping Skills": nulo, 
        "Response": alto, "Explosive Power": top, "Dribble Speed": alto, "Top Speed": top, 
        "Body Balance": alto, "stamina": medio, "Kicking Power": top, "Jump": bajo, 
        "Tenacity": medio, "Teamwork": medio,
    },
    "CF": {
        "Attack": top, "Defence": nulo, "Header Accuracy": alto, "Dribble Accuracy": top, "Short Pass Accuracy": alto, "Short Pass Speed": alto,
        "Long Pass Accuracy": bot, "Long Pass Speed": bot, "Shot Accuracy": top, "Place Kicking": bajo, "Swerve": bajo, "Ball Controll": alto,
        "Goal Keeping Skills": nulo, 
        "Response": medio, "Explosive Power": medio, "Dribble Speed": alto, "Top Speed": top, 
        "Body Balance": top,"stamina": bajo, "Kicking Power": top, "Jump": alto, 
        "Tenacity": medio, "Teamwork": medio,
    },
}
