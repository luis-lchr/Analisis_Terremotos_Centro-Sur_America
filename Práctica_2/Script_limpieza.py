import pandas as pd
import requests
from io import StringIO

url = "https://zenodo.org/record/4670969/files/terremotos_centro_sur_america.csv"

response = requests.get(url)

if response.status_code == 200:
    df = pd.read_csv(StringIO(response.text))
    print(df.head())

    def procesar_columna_fecha_y_hora(df):
        df['Fecha'] = df['Fecha y Hora'].str.slice(stop=11)
        df['Hora'] = df['Fecha y Hora'].str.slice(start=12)

        df = df.drop(['Fecha y Hora'], axis=1)

        df['Fecha'] = df['Fecha'].str.strip()

        df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d %b %Y', errors='coerce')
        df['Hora'] = df['Hora'].str.replace(' GMT', '')

        return df

    def procesar_columna_profundidad_ubicacion(df):
        df['Profundidad'] = df['Profundidad'].str.extract('(\d+\.?\d*)').astype(float)
        df = df.drop(['Ubicacion'], axis=1)

        return df

    df = procesar_columna_fecha_y_hora(df)
    df = procesar_columna_profundidad_ubicacion(df)

    nuevo_orden_columnas = ['Pais', 'Fecha', 'Hora', 'Año', 'Magnitud', 'Profundidad']
    df = df[nuevo_orden_columnas]

    print(df.head())

    # df.to_csv('dataset_2076326.csv', index=False)
    df.to_csv('dataset_limpio_2076326.csv', index=False)

    print("El conjunto de datos se ha descargado exitosamente.")
else:
    print("Error")