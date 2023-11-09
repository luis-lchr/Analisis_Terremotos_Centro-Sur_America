import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def cargar_datos(file_name):
    df = pd.read_csv(file_name)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Año'] = df['Fecha'].dt.year
    df_sin_2021 = df[df['Año'] != 2021]
    return df_sin_2021

def ajustar_modelos(df, categorias):
    modelos = {}
    for categoria in categorias:
        terremotos_por_categoria = df[df['Etiqueta'] == categoria]
        terremotos_por_categoria_por_año = terremotos_por_categoria['Año'].value_counts().sort_index()
        años_por_categoria = terremotos_por_categoria_por_año.index
        cantidad_terremotos_por_categoria = terremotos_por_categoria_por_año.values
        años_por_categoria = np.array(años_por_categoria)
        modelo = LinearRegression()
        modelo.fit(años_por_categoria.reshape(-1, 1), cantidad_terremotos_por_categoria)
        modelos[categoria] = modelo
    return modelos

def graficar_pronostico(df, categorias, modelos, años_para_prediccion):
    plt.figure(figsize=(10, 6))
    for categoria in categorias:
        terremotos_por_categoria = df[df['Etiqueta'] == categoria]
        terremotos_por_categoria_por_año = terremotos_por_categoria['Año'].value_counts().sort_index()
        años_por_categoria = terremotos_por_categoria_por_año.index
        cantidad_terremotos_por_categoria = terremotos_por_categoria_por_año.values
        años_por_categoria = np.array(años_por_categoria)
        plt.plot(años_por_categoria, [modelos[categoria].coef_[0] * x + modelos[categoria].intercept_ for x in años_por_categoria])
        plt.scatter(años_por_categoria, cantidad_terremotos_por_categoria, s=80, marker="o", label=categoria)

    plt.ylabel("Cantidad de Terremotos")
    plt.xlabel("Años")
    plt.title("Pronóstico de Terremotos por Categoría (Forecasting)")
    plt.legend()

    for categoria in categorias:
        terremotos_por_categoria = df[df['Etiqueta'] == categoria]
        terremotos_por_categoria_por_año = terremotos_por_categoria['Año'].value_counts().sort_index()
        años_por_categoria = terremotos_por_categoria_por_año.index
        cantidad_terremotos_por_categoria = terremotos_por_categoria_por_año.values
        años_por_categoria = np.array(años_por_categoria)
        modelo = modelos[categoria]
        modelo.fit(años_por_categoria.reshape(-1, 1), cantidad_terremotos_por_categoria)
        prediccion = modelo.predict(np.array([2020, 2021, 2022, 2023]).reshape(-1, 1))
        plt.plot([2020, 2021, 2022, 2023], prediccion, linestyle='--', label=f'Predicción de {categoria}')

    for categoria in categorias:
        terremotos_por_categoria = df[df['Etiqueta'] == categoria]
        terremotos_por_categoria_por_año = terremotos_por_categoria['Año'].value_counts().sort_index()
        años_por_categoria = terremotos_por_categoria_por_año.index
        cantidad_terremotos_por_categoria = terremotos_por_categoria_por_año.values
        años_por_categoria = np.array(años_por_categoria)
        modelo = modelos[categoria]
        modelo.fit(años_por_categoria.reshape(-1, 1), cantidad_terremotos_por_categoria)
        prediccion = modelo.predict(np.array([2022, 2023]).reshape(-1, 1))
        plt.scatter([2022, 2023], prediccion, c='black', s=100, label=f'Predicciones adicionales de {categoria}')

    for categoria in categorias:
        terremotos_por_categoria = df[df['Etiqueta'] == categoria]
        terremotos_por_categoria_por_año = terremotos_por_categoria['Año'].value_counts().sort_index()
        años_por_categoria = terremotos_por_categoria_por_año.index
        cantidad_terremotos_por_categoria = terremotos_por_categoria_por_año.values
        años_por_categoria = np.array(años_por_categoria)
        modelo = modelos[categoria]
        modelo.fit(años_por_categoria.reshape(-1, 1), cantidad_terremotos_por_categoria)
        prediccion = modelo.predict(np.array([2021]).reshape(-1, 1))
        plt.scatter([2021], prediccion, c='black', s=100, label=f'Predicción de {categoria} para 2021')

    plt.savefig('Forecasting/Grafico_prediccion_forecasting.png')
    plt.show()

if __name__ == "__main__":
    data_file = "dataset_limpio_etiquetado_2076326.csv"
    df = cargar_datos(data_file)
    categorias = ['Terremoto insignificativo', 'Terremoto significativo', 'Terremoto leve']
    modelos = ajustar_modelos(df, categorias)
    años_para_prediccion = [2020, 2021, 2022, 2023]
    graficar_pronostico(df, categorias, modelos, años_para_prediccion)
