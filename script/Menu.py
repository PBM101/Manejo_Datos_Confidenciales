# Funcionalidad relacionada con el menú

def Menu():
    """
    The Menu() function asks for a route and stores it in a string variable.
    :return: A list of strings with the routes to the files
    """
    route = []
    route[0] = input('Introduzca la dirección del archivo: ')

    while(route != 'Done'):
        print('Si quieres terminar el proceso escribe "Done"\n')
        route.append(input('Introduzca la dirección del archivo: '))

    return route

