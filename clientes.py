import pandas as pd
import numpy as np

df = pd.read_excel("clientes.xlsx")
#print(df.head())
#print(df.info())
#print(df.isnull().sum())

df = df.dropna()
# se decidio eliminar todas estas filas, debido a que su informacion termina siendo inválida o poco confiable debido a la falta de datos tan importantes como lo es el RFC y El nombre.
#Lo mejor sería solicitar al cliente volver a registrarse. 

#CONVERTIR A CSV
df.to_csv('clientes_limpio.csv')