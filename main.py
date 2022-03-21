import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import calculos_read_file as crf

# read the document with measures
document_path = 'dato_medidas.txt' # name of file
measures_list = []
crf.read_file(document_path, measures_list)
# print(measures_list)

# this is average of everything data of the list measures
average = np.mean(measures_list)
# print(average)



name_csv = "calculos_fisica.csv"
with open(name_csv, 'w') as file_csv:
    file_csv.write('Numero columna,h cm, |h - hpromedio|,tiempo de reaccion,\n')
    column_number = 0
    ei = 0.05
    significant_height_list = []
    for measure in measures_list:
        significant_height = crf.significant_height(measure, average)
        significant_height_list.append(significant_height) # para sacar RO
    RO = np.mean(significant_height_list)
    for measure in measures_list:
        column_number += 1
        serch_height = column_number - 1
        tiempo = crf.tiempo_reaccion(measure, RO)
        file_csv.write(f"{column_number}, {round(measure, 2)},{round(significant_height_list[serch_height], 2)}, {round(tiempo, 3)},\n")
    error_abs = RO + ei
    file_csv.write(f'\n\nPromedio,{average}')
    file_csv.write(f'\nRO, {RO}')
    file_csv.write(f'\nEi, {ei}')
    file_csv.write(f'\nError absoluto, {error_abs}')
file_csv.close()

# show the csv with pandas
# df = pd.read_csv(name_csv)
# print(df)


# graphs of csv
# plt.hist(df['tiempo de reaccion'], 15, color='blue')
# plt.show()
