# Funcionalidad relacionada con el menú

def Menu():
    """
    The Menu() function asks for a route and stores it in a string variable.
    :return: A list of strings with the routes to the files
    """
    messageDone = 'Si quiere terminar el proceso escribe "Done"\n'
    messageRoute = 'Introduzca la dirección del archivo: '

    route = []
    print(messageDone)
    command = input(messageRoute)
    if command.upper() != 'DONE':
        while command.upper() != 'DONE':
            route.append(command)
            command = input(messageRoute)

    print("Proceso terminado")

    print(route)


