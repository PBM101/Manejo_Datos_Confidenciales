"""
    Autores: Blanca Gonzalez, Gonzalo García, Nicolás Olabarría y Pablo Bobo
    Fecha: 9 de Junio de 2021
    Tema: Manejo de datos Confidenciales

"""

import Menu
import Manejo_de_datos
import cambios_nombres

# Lectura de direcciones de los archivos
route = Menu.menu()

# Lectura de las columnas de cada ruta
i = 1
for url in route:
    Manejo_de_datos.lectura_nombre_columnas(url, i)
    i = i +1


dataFrames = []

for url in route:
    dataFrames.append(cambios_nombres.cambios_nombres(url))

# Aquí deberían ir las rutas de los archivos
title = 'Columnas1.txt'

for dataFrame in dataFrames:
    cambios_nombres.nombres_originales(dataFrame,title)