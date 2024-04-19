import pandas as pd
import numpy as np

df = pd.read_excel("devoluciones.xlsx")
#print(df.head())
#print(df.info())
#print(df.isnull().sum())

# debido a que sería muy drástico eliminar las filas que posean este dato faltante, el DataFrame se vería sumamente afectado y los resultados sesgados. Por ello se opto por cambiar el valor nulo a dato inválido. 
df['FECHA_CANCELA'].fillna('00/00/0000  00:00:00 y. y.', inplace=True) 

#el mismo concepto se aplico a para 'DOC_ANT'
df['DOC_ANT'].fillna('Y00000', inplace=True) 

#CONVERTIR A CSV
df.to_csv('devoluciones_limpio.csv')