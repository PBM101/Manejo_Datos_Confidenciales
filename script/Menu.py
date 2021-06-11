# Funcionalidad relacionada con el menú

"""
    Autores: Nicolás Olabarría
    Fecha: 9 de Junio de 2021
    Tema: Menú
"""

import pandas as pd

def Menu():
    """
    The Menu() function asks for a route and stores it in a string variable.
    :return: A list of strings with the routes to the files
    """
    
    # Mensajes utilizados en el menú
    messageOption = '¿Cómo quiere leer las direcciones de los datasets?[man/txt]: '
    messageNotValid = 'Opción no válida. Introdúzcalo de nuevo\n'


    print(
        'Puedes introducir los datos manualmente (man), o si los tienes en un .txt hacerlo de manera automática (txt)')
    option = input(messageOption)

    while option.upper() != 'MAN' and option.upper() != 'TXT':
        print(messageNotValid)
        option = input(messageOption)

    route = []

    if option.upper() == 'MAN':
        route = LecturaManual()
    elif option.upper() == 'TXT':
        route = LecturaTXT()

    return route

def LecturaManual():
    """
    Lectura de las rutas de manera manual.
    :return: Devuelve una lista de rutas introducidas de manera manual.
    """
    messageDone = 'Si quiere terminar el proceso escribe "Done"\n'
    messageRoute = 'Introduzca la dirección del archivo: '
    print(messageDone)
    command = input(messageRoute)

    route = []

    if command.upper() != 'DONE':
        while command.upper() != 'DONE':

            while True:
                try:
                    data = pd.read_csv(command)
                    break
                except FileNotFoundError:
                    print('La dirección no es correcta')
                    command = input(messageRoute)

            route.append(command)
            command = input(messageRoute)

    return route

def LecturaTXT():
    """
    Función para la lectura de las rutas de manera automática.
    :return: Devuelve una lista de rutas sacadas de un archivo .txt.
    """
    txt_route = input('Introduzca la ruta del archivo: ')
    while True:
        try:
            with open(txt_route, 'r') as route_file:
                route = []
                i = 1
                for line in route_file.readlines():
                    print('Ruta ', i, ':', line)
                    i+=1
                    line = line.replace("\n", "")
                    print(line)
                    route.append(line)
            break
        except FileNotFoundError:
            txt_route = input('La ruta no es válida, introdúzcala de nuevo: ')

    return route




