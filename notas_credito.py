import pandas as pd
import numpy as np

df = pd.read_excel("notas_credito.xlsx")
#print(df.head())
#print(df.info())
#print(df.isnull().sum())

#Se rellenan pues al estar hablando de créditos sería terrible perder su registro. y afectaría los libros.
df['CVE_VEND'].fillna(0, inplace=True)

#lo mismo aplicable a esta columna, siempre tomando en cuenta el formato que poseen 
df['CVE_PEDI'].fillna('--', inplace=True)

#así como la fecha cancelada, ya que se esta hablando de un  gran numero de datos que resultan de vital importancia
df['FECHA_CANCELA'].fillna('00/00/0000  00:00:00 x. x.', inplace=True) 

#CONVERTIR A CSV
df.to_csv('notas_credito_limpio.csv')