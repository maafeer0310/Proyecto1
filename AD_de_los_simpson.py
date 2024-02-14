import pandas as pd
import matplotlib.pyplot as plt

#Descargar los datos de los dialogos de Los Simpson
df = pd.read_csv("dialogo.csv")

#Eliminar filas con informacion no relevante
df = df.dropna()

#Lista de datos
personajes = df["Personaje"].value_counts()

#Cantidad de dialogos por personajes
plt.bar(personajes.index, personajes)
plt.xlabel("Personaje")
plt.ylabel("Cantidad de dialogos")
plt.title("Cantidad de dialogos por personaje")
plt.show()