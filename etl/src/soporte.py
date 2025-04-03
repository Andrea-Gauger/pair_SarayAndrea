import pandas as pd

def apertura_exploracion(csv):
    """ Función a la que le paso el nombre del archivo, me crea un df y me hace una primera exploración"""
    csv = pd.read_csv(f"../files/{csv}.csv")        

    display(csv.head(5))
    print(f"\nEl df tiene las sigiuentes filas y columnas {csv.shape}\n-----" )
    print(f"{csv.columns}\n-----")
    display(f"{csv.info()}\n-----")
    display(csv.describe().T)
    print(csv.duplicated().sum())