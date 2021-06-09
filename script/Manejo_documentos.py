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

    columnas = pd.read_csv(route, sep=";", header=None,
                           dayfirst=True, infer_datetime_format=True, nrows=1)

    # Escritura de archivos txt
    if num < 0:
        title = "Columnas.txt"
    else:
        number = str(num)
        title = "Columnas" + number + ".txt"

    with open(title, "w+") as file1:
        for i in range(len(columnas.columns)):
            file1.write(columnas[i][0])
            file1.write(',')

"""
def lectura_headers_archivos(lista):
    import sys  # comprobación de librerías adecuadas
    modulename = 'pd'
    if modulename not in sys.modules:
        import pandas as pd

    i = 1
    while i <= len(lista):
        lectura_nombre_columnas(url=lista[i - 1][0], num=i)
        i += 1
    print('Fin de creación de archivos')

"""