"""
    Autores: Nicolás Olabarría y Pablo Bobo
    Fecha: 9 de Junio de 2021
    Tema: Manejo de Datos

"""

messageOption = '¿Quieres sobreescribir este archivo?[yes/no]: '
messageNotValid = 'Opción no válida. Introdúzcalo de nuevo\n'

def lectura_nombre_columnas(url, num=-1):
    """
    Función que crea un archivo txt con los headers del archivo csv indicado .
    :param url: String con la dirección de memoria del archivo a obtener headers.
           num: Número de documento en dónde almacenar los datos tal que: columnas'num'.txt, en caso de ser negativo el archivo
            tendrá nombre Columnas.txt .
    :return: Nullo
    """
    import sys
    modulename = "pd"
    if modulename not in sys.modules:
        import pandas as pd

    columnas = pd.read_csv(url, sep=";", header=None,
                           dayfirst=True, infer_datetime_format=True, nrows=1)

    # Escritura de archivos txt
    if num < 0:
        title = "Columnas.txt"
    else:
        number = str(num)
        title = "Columnas" + number + ".txt"

    #Comprobación de ruta vacía
    from os import path
    print("Los archivos actuales se almacenarán en: ", path.dirname(path.abspath(__file__)))
    route = path.dirname(path.abspath(__file__)) + r'\\' + title
    if path.exists(route):
        print("La ruta señalada está ya en uso.\n")
        option = input(messageOption)
        while option.upper() != 'YES' and option.upper() != 'NO':
            print(messageNotValid)
            option = input(messageOption)
        if option.upper() == "YES":
            from os import remove
            remove(route)
            with open(title, "w+") as file1:
                for i in range(len(columnas.columns)):
                    file1.write(columnas[i][0])
                    file1.write(',')
        else:
            print("Las columnas del archivo no serán almacenadas en el archivo con nombre: ", title)
    else:
        with open(title, "w+") as file1:
            for i in range(len(columnas.columns)):
                file1.write(columnas[i][0])
                file1.write(',')

def headers_varios_archivos(lista):
    """
    Función genérica que recibe una lista de urls y crea sistemáticamente archivos para cada uno de las urls
    :param lista: Lista de rutas a varios archivos de los que se quiere obtener headers.
    :return: Nullo.
    """
    import sys  # comprobación de librerías adecuadas
    modulename = 'pd'
    if modulename not in sys.modules:
        import pandas as pd

    for i in range(len(lista)):
        lectura_nombre_columnas(lista[i], i)
    print('Fin de creación de archivos')

def eliminar_headers_originales(url=None):
    """
    Función que se encarga de eliminar los archivos con las columnas originales de los archivos
    :param: url: String con la dirección de memoria dónde deben estar almacenados los archivos con las columnas. En caso
                de que no se de una url, se tomará la url del directorio.
    :return: Nullo.
    """
    if url==None:
        from os import path
        route = path.dirname(path.abspath(__file__))
    else:
        route = url
    print("Se eliminarán los archivos columna en: ", route)
