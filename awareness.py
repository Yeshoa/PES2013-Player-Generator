import random
import numpy as np

def generate_att(position):
    value = 1  # Valor predeterminado

    if position in ["CF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 100])[0]
    if position in ["SS"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 100])[0]
    if position in ["LWF", "RWF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 70])[0]
    elif position in ["AMF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 7])[0]
    elif position in ["LMF", "RMF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 6])[0]
    elif position in ["CMF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 1])[0]
    elif position in ["DMF"]:
        value = random.choices([1, 2, 3], weights=[1, 20, 1])[0]
    elif position in ["LB", "RB"]:
        value = random.choices([1, 2, 3], weights=[0, 4, 3])[0]
    elif position in ["SWP", "CB"]:
        value = random.choices([1, 2, 3], weights=[1, 30, 2])[0]
    elif position == "GK":
        value = random.choices([1, 2, 3], weights=[0, 1, 0.01])[0]

    return value

def generate_def(position):
    value = 1  # Valor predeterminado

    if position in ["CF"]:
        value = random.choices([1, 2, 3], weights=[5, 30, 2])[0]
    if position in ["SS"]:
        value = random.choices([1, 2, 3], weights=[1, 20, 2])[0]
    if position in ["LWF", "RWF"]:
        value = random.choices([1, 2, 3], weights=[2, 8, 1])[0]
    elif position in ["AMF"]:
        value = random.choices([1, 2, 3], weights=[2, 11, 1])[0]
    elif position in ["LMF", "RMF"]:
        value = random.choices([1, 2, 3], weights=[1, 10, 1])[0]
    elif position in ["CMF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 1])[0]
    elif position in ["DMF"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 20])[0]
    elif position in ["LB", "RB"]:
        value = random.choices([1, 2, 3], weights=[0, 4, 3])[0]
    elif position in ["SWP", "CB"]:
        value = random.choices([1, 2, 3], weights=[0, 1, 100])[0]
    elif position == "GK":
        value = random.choices([1, 2, 3], weights=[0, 1, 0.01])[0]

    return value