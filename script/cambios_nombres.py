import pandas as pd
import os

def cambios_nombres(url):

    """
    Función para cambiar los nombres de los dataFrames a utilizar
    :param url: necesita la dirección de los dataFrames a utilizar
    :return: devuelve un dataFrame
    """

    dataFrame = pd.read_csv(url)
    print("Vas a cambiar los nombres de las columnas del data Frame de la dirección:\n", url)

    option = input("¿Tienes las variables guardadas o prefieres introducirlas de manera manual?[txt/man]: ")

    while option.upper() != 'TXT' and option.upper() != 'MAN':
        print("La opción introducida no es válida, intentalo de nuevo.")
        option = input("¿Tienes las variables guardadas o prefieres introducirlas de manera manual?[txt/man]: ")

    dict = {}

    if option.upper() == 'MAN':
        for index in range(0, len(dataFrame.columns)):
            print(type(dataFrame.columns[index]))
            new_title = input("Introduzca el nuevo nombre: ")
            dict = {dataFrame.columns[index]: new_title}
            print(new_title)
            dataFrame.rename(columns=dict, inplace=True)
            index += 1
    elif option.upper() == 'TXT':
        variable_list = variables_guardadas()
        i = 0
        for key in dataFrame.columns:
            dict[key] = variable_list[i]
            i += 1
        print(dict)
        dataFrame.rename(columns = dict, inplace = True)
    print(dataFrame.columns)

    return dataFrame

def variables_guardadas():

    """
    Función para leer los nombres de las variables a las que se quieren cambiar las columnas del dataFrame
    :return:Devuelve una lista con los nombres de las variables nuevas.
    """

    variable_route = input("Introduzca la ruta del directorio donde tiene guardadas las variables: ")
    while os.path.exists(variable_route) == False:
        variable_route = input("La ruta no existe, introdúzcala de nuevo: ")

    files = os.listdir(variable_route)
    for i in range(1, len(files) + 1):
        print(i,'.', files[i - 1])

    while True:
        try:
            option = int(input("Introduzca el número del archivo donde tiene guardadas las variables: "))
            while option > len(files) + 1 or option == 0:
                option = int(input("Esa opción no es válida, inténtalo de nuevo, mamón: "))
            print("El archivo que quiere abrir es: ", files[option - 1])
            try:
                with open(files[option - 1], 'r') as variable_file:
                    variable_list = []
                    for lines in variable_file.readlines():
                        variable_list.append(lines)
                    break
            except OSError:
                option= int(input("Ese archivo no se puede leer. Introduzca otra opcion:"))
                break
            break
        except ValueError:
            option = int(input("Esa opción no es válida, inténtalo de nuevo: "))

    for i in range(0, len(variable_list)):
        variable_list[i] = variable_list[i].replace('\n', '')

    return variable_list

def nombres_originales(dataFrame, title):

    """
    Esta función devuelve los nombres de las columnas de un dataFrame desde los que se definieron previamente a los
    nombres originales.
    :param dataFrame: dataFrame al que se le quieren volver a cambiar los nombres a sus originales.
    :param title: nombre del archivo de texto donde están guardadas los nombres de las variables originales.
    :return: devuelve el dataFrame con los nombres de las variables originales.
    """

    option = input("¿Quiere guardar los nombres de sus variables para usarlos en un futuro? [yes/no]:")
    while option.upper() != 'YES' and option.upper() != 'NO':
        print("La opción elegida no es válida, inténtelo de nuevo.")
        option = input("¿Quiere guardar los nombres de sus variables para usarlos en un futuro? [yes/no]:")

    if option.upper() == 'YES':
        new_variables_route = input("Introduzca el nombre de la ruta: ")
        while os.path.exists(new_variables_route) == False:
            print("La ruta seleccionada no existe, inténtelo de nuevo.\n")
            new_variables_route = input("Introduzca el nombre de la ruta: ")
        title_new = input("¿Cómo quiere llamar al archivo?: ")
        with open(title_new + '.txt', 'w+') as file:
            for i in range(0, len(dataFrame.columns)):
                file.writelines(dataFrame.columns[i] + '\n')

    with open(title, 'r') as name_file:
        name_list = name_file.readlines()
        name_list = name_list[0].split(',')
        name_list = list(filter(lambda item: item.strip(), name_list))

        for i in range(0, len(dataFrame.columns)):
            dict = {dataFrame.columns[i] : name_list[i]}
            dataFrame.rename(columns = dict, inplace = True)

    print(dataFrame)
    return dataFrame