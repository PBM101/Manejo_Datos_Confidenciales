import pandas as pd

def cambios_nombres(url):

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

    return


