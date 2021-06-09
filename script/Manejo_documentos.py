"""
    Autores: Nicolás Olabarría y Pablo Bobo
    Fecha: 9 de Junio de 2021
    Tema: Manejo de Documentos .txt

"""
def lectura_nombe_columnas():
    import pandas as pd

    route = input('Introduzca la url desde dónde desea extraer los datos: ')

    columnas = pd.read_csv(route, sep=';', header=None, dayfirst=True, infer_datetime_format=True, nrows=1)
    title = "Columnas1.txt"
    with open(title, "w+") as file1:
        for i in range(len(columnas.columns)):
            file1.write(columnas[i][0])
            file1.write(',')