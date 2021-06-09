# Funcionalidad relacionada con el menú

def Menu():
    """
    The Menu() function asks for a route and stores it in a string variable.
    :return: A list of strings with the routes to the files
    """
    
    # Mensajes utilizados en el menú
    messageDone = 'Si quiere terminar el proceso escribe "Done"\n'
    messageRoute = 'Introduzca la dirección del archivo: '
    
    # Declaración de la variable de lista de rutas 
    route = []
    
    print(messageDone)
    command = input(messageRoute)
    
    if command.upper() != 'DONE':
        while command.upper() != 'DONE':
            route.append(command)
            command = input(messageRoute)

    print("Proceso terminado")
    
    return route


