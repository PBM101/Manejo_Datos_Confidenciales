import pandas as pd

i = 0

def cambios_nombres(url):

    """
    Función para cambiar los nombres de los dataFrames a utilizar
    :param url: necesita la dirección de los dataFrames a utilizar
    :return: devuelve un dataFrame
    """

    dataFrame = pd.read_csv(url)
    print("Vas a cambiar los nombres de las columnas del data Frame de la dirección:\n", url)

    for index in range(0,len(dataFrame.columns)):
        print(type(dataFrame.columns[index]))
        new_title = input("Introduzca el nuevo nombre: ")
        dict = {dataFrame.columns[index] : new_title}
        print(new_title)
        dataFrame.rename(columns = dict, inplace = True)
        index += 1

    print(dataFrame.columns)

    return dataFrame

def nombres_originales(dataFrame, title):

    with open(title, "r") as name_file:
        name_list = name_file.readlines()
        name_list = name_list[0].split(',')
        name_list = list(filter(lambda item: item.strip(), name_list))

        for i in range(0, len(dataFrame.columns)):
            dict = {dataFrame.columns[i] : name_list[i]}
            dataFrame.rename(columns = dict, inplace = True)

    print(dataFrame)
    return dataFrame


