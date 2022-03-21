import math


def read_file(file_path, lista: list):
    # add data in one list, from a file
    with open(file_path, 'r') as file:
        for see in file:
            data_number = eval(see.replace("\n", ""))
            lista.append(data_number)
    file.close()


def significant_height(height, average):
    return abs(height - average)


def tiempo_reaccion(distance: eval, ro: eval):
    g = 980
    distancia = distance - ro
    calculate = (2 * distancia) / g
    return math.sqrt(calculate)


