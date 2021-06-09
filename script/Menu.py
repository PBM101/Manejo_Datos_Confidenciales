# Funcionalidad relacionada con el menú

def Menu():
    """
    The Menu() function asks for a route and stores it in a string variable.
    :return: A list of strings with the routes to the files
    """
    route = []
    route.append(input(str('Introduzca la dirección del archivo: '))) # Input inicial de rutas

    i = 0 # Contador de posición

    while (route[i] != 'Done'):
        print('Si quieres terminar el proceso escribe "Done"\n')
        route.append(str(input('Introduzca la dirección del archivo: ')))
        i = i + 1

    return route

