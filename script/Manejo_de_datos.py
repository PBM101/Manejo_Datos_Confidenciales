"""
    Autores: Pablo Bobo
    Fecha: 9 de Junio de 2021
    Tema: Manejo de Datos

"""

def lectura_nombre_columnas(url=None, num=-1):
    """
    Función que crea un archivo txt con los headers del archivo csv indicado
    url: String con la dirección de memoria del archivo a obtener headers
    num: Número de documento en dónde almacenar los datos tal que: columnasnum.txt
    """
    import sys  # comprobación de librerías adecuadas
    modulename = "pd"
    if modulename not in sys.modules:
        import pandas as pd

    if url == None:  # Obtención de url de datos
        route = input("Introduzca la url desde dónde desea extraer los datos: ")
    else:
        route = url