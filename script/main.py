"""
    Autores: Blanca Gonzalez, Gonzalo García, Nicolás Olabarría y Pablo Bobo
    Fecha: 9 de Junio de 2021
    Tema: Manejo de datos Confidenciales

"""


import Menu
import Manejo_de_datos
import CambiosNombres

# Lectura de direcciones de los archivos
route = Menu.Menu()

# Lectura de las columnas de cada ruta
i = 1
for url in route:
    Manejo_de_datos.lectura_nombre_columnas(url, i)
    i = i +1

url = []

for url in route:
    CambiosNombres.cambios_nombres(url)
