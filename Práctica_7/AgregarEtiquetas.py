import pandas as pd

data = pd.read_csv('dataset_limpio_2076326.csv')

def asignar_etiqueta(row):
    if row['Magnitud'] >= 4.6 and row['Profundidad'] >= 300:
        return 'Terremoto significativo'
    elif row['Magnitud'] >= 4.2 and row['Magnitud'] < 4.6 and row['Profundidad'] < 400 and row['Profundidad'] >= 200:
        return 'Terremoto leve'
    elif row['Magnitud'] < 4.2 and row['Profundidad'] >= 0 and row['Profundidad'] < 200:
        return 'Terremoto insignificativo'
    else:
        return 'No terremotos'


data['Etiqueta'] = data.apply(asignar_etiqueta, axis=1)

data.to_csv('dataset_limpio_etiquetado_2076326.csv', index=False)