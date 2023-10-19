import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

output_folder = "Regresiones Lineales"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

data = pd.read_csv('dataset_limpio_2076326.csv')

data = data[data['Año'] != 2021]

earthquakes_by_year = data.groupby('Año')[['Magnitud', 'Profundidad']].mean().reset_index()

X_mag = earthquakes_by_year['Año'].values.reshape(-1, 1)
y_mag = earthquakes_by_year['Magnitud'].values

model_mag = LinearRegression()
model_mag.fit(X_mag, y_mag)

years_to_predict = [2022, 2023, 2024]
predicted_avg_magnitudes = model_mag.predict(np.array(years_to_predict).reshape(-1, 1))

X_prof = earthquakes_by_year['Año'].values.reshape(-1, 1)
y_prof = earthquakes_by_year['Profundidad'].values

model_prof = LinearRegression()
model_prof.fit(X_prof, y_prof)

predicted_avg_depths = model_prof.predict(np.array(years_to_predict).reshape(-1, 1))
X_ext = np.append(earthquakes_by_year['Año'], 2022)
y_ext_mag = model_mag.predict(X_ext.reshape(-1, 1))
y_ext_prof = model_prof.predict(X_ext.reshape(-1, 1))

earthquake_counts_by_year = data.groupby('Año')['Pais'].count().reset_index()
earthquake_counts_by_year.columns = ['Año', 'Cantidad']

X_count = earthquake_counts_by_year['Año'].values.reshape(-1, 1)
y_count = earthquake_counts_by_year['Cantidad'].values

model_count = LinearRegression()
model_count.fit(X_count, y_count)

years_to_predict_count = [2022, 2023, 2024]
predicted_counts = model_count.predict(np.array(years_to_predict_count).reshape(-1, 1))
X_ext_count = np.append(earthquake_counts_by_year['Año'], 2022)
y_ext_count = model_count.predict(X_ext_count.reshape(-1, 1))

plt.figure(figsize=(16, 6))
plt.scatter(earthquakes_by_year['Año'], earthquakes_by_year['Magnitud'], label='Promedio de Magnitud Real', color='blue')
plt.plot(years_to_predict, predicted_avg_magnitudes, label='Predicciones', color='red', marker='o')
plt.plot(X_ext, y_ext_mag, linestyle='dotted', color='green', label='Modelo')
plt.xlabel('Año')
plt.ylabel('Promedio de Magnitud')
plt.legend()
plt.savefig(os.path.join(output_folder, 'prediccion_magnitud_general.png'))

plt.figure(figsize=(16, 6))
plt.scatter(earthquakes_by_year['Año'], earthquakes_by_year['Profundidad'], label='Promedio de Profundidad Real', color='blue')
plt.plot(years_to_predict, predicted_avg_depths, label='Predicciones', color='red', marker='o')
plt.plot(X_ext, y_ext_prof, linestyle='dotted', color='green', label='Modelo')
plt.xlabel('Año')
plt.ylabel('Promedio de Profundidad')
plt.legend()
plt.savefig(os.path.join(output_folder, 'prediccion_profundidad_general.png'))

plt.figure(figsize=(16, 6))
plt.scatter(earthquake_counts_by_year['Año'], earthquake_counts_by_year['Cantidad'], label='Cantidad de Terremotos Real', color='blue')
plt.plot(years_to_predict_count, predicted_counts, label='Predicciones', color='red', marker='o')
plt.plot(X_ext_count, y_ext_count, linestyle='dotted', color='green', label='Modelo')
plt.xlabel('Año')
plt.ylabel('Cantidad de Terremotos')
plt.legend()
plt.savefig(os.path.join(output_folder, 'prediccion_num_terremotos_general.png'))

earthquakes_by_year = data.groupby('Año')[['Magnitud', 'Profundidad']].mean().reset_index()

X_mag = earthquakes_by_year['Año'].values.reshape(-1, 1)
y_mag = earthquakes_by_year['Magnitud'].values
model_mag = LinearRegression()
model_mag.fit(X_mag, y_mag)

X_prof = earthquakes_by_year['Año'].values.reshape(-1, 1)
y_prof = earthquakes_by_year['Profundidad'].values
model_prof = LinearRegression()
model_prof.fit(X_prof, y_prof)

years_to_predict = [2022, 2023, 2024]
predicted_avg_magnitudes = model_mag.predict(np.array(years_to_predict).reshape(-1, 1))
predicted_avg_depths = model_prof.predict(np.array(years_to_predict).reshape(-1, 1))

country_regression_folder_mag = os.path.join(output_folder, "Regresiones por país para magnitud")
country_regression_folder_prof = os.path.join(output_folder, "Regresiones por país para profundidad")

if not os.path.exists(country_regression_folder_mag):
    os.makedirs(country_regression_folder_mag)

if not os.path.exists(country_regression_folder_prof):
    os.makedirs(country_regression_folder_prof)

earthquakes_by_country = data.groupby(['Pais', 'Año'])[['Magnitud', 'Profundidad']].mean().reset_index()

models_mag_by_country = {}
models_prof_by_country = {}
predictions_mag_by_country = {}
predictions_prof_by_country = {}

for country in earthquakes_by_country['Pais'].unique():
    country_data = earthquakes_by_country[earthquakes_by_country['Pais'] == country]
    
    X_country = country_data['Año'].values.reshape(-1, 1)
    y_mag_country = country_data['Magnitud'].values
    y_prof_country = country_data['Profundidad'].values
    
    model_mag_country = LinearRegression()
    model_mag_country.fit(X_country, y_mag_country)
    
    model_prof_country = LinearRegression()
    model_prof_country.fit(X_country, y_prof_country)
    
    models_mag_by_country[country] = model_mag_country
    models_prof_by_country[country] = model_prof_country
    
    predictions_mag_country = model_mag_country.predict(np.array(years_to_predict).reshape(-1, 1))
    predictions_prof_country = model_prof_country.predict(np.array(years_to_predict).reshape(-1, 1))
    
    predictions_mag_by_country[country] = predictions_mag_country
    predictions_prof_by_country[country] = predictions_prof_country

for country, model_mag in models_mag_by_country.items():
    model_prof = models_prof_by_country[country]
    
    plt.figure(figsize=(16, 6))
    plt.scatter(earthquakes_by_country[earthquakes_by_country['Pais'] == country]['Año'], earthquakes_by_country[earthquakes_by_country['Pais'] == country]['Magnitud'], label='Promedio de Magnitud Real', color='blue')
    plt.plot(years_to_predict, predictions_mag_by_country[country], label='Predicciones', color='red', marker='o')
    
    X_ext_country = np.append(country_data['Año'], 2022)
    y_ext_mag = model_mag.predict(X_ext_country.reshape(-1, 1))
    plt.plot(X_ext_country, y_ext_mag, linestyle='dotted', color='green', label='Modelo')
    
    plt.xlabel('Año')
    plt.ylabel('Promedio de Magnitud')
    plt.legend()
    
    image_filename_mag = os.path.join(country_regression_folder_mag, f'prediccion_magnitud_{country}.png')
    plt.savefig(image_filename_mag)
    plt.close()

for country, model_prof in models_prof_by_country.items():
    model_mag = models_mag_by_country[country]
    
    plt.figure(figsize=(16, 6))
    plt.scatter(earthquakes_by_country[earthquakes_by_country['Pais'] == country]['Año'], earthquakes_by_country[earthquakes_by_country['Pais'] == country]['Profundidad'], label='Promedio de Profundidad Real', color='blue')
    plt.plot(years_to_predict, predictions_prof_by_country[country], label='Predicciones', color='red', marker='o')
    
    X_ext_country = np.append(country_data['Año'], 2022)
    y_ext_prof = model_prof.predict(X_ext_country.reshape(-1, 1))
    plt.plot(X_ext_country, y_ext_prof, linestyle='dotted', color='green', label='Modelo')
    
    plt.xlabel('Año')
    plt.ylabel('Promedio de Profundidad')
    plt.legend()
    
    image_filename_prof = os.path.join(country_regression_folder_prof, f'prediccion_profundidad_{country}.png')
    plt.savefig(image_filename_prof)
    plt.close()

earthquakes_count_by_country = data.groupby(['Pais', 'Año'])['Magnitud'].count().reset_index()
earthquakes_count_by_country.columns = ['Pais', 'Año', 'Cantidad']

country_regression_folder_count = os.path.join(output_folder, "Regresiones por país para cantidad de terremotos")

if not os.path.exists(country_regression_folder_count):
    os.makedirs(country_regression_folder_count)

models_count_by_country = {}
predictions_count_by_country = {}

for country in earthquakes_count_by_country['Pais'].unique():
    country_data = earthquakes_count_by_country[earthquakes_count_by_country['Pais'] == country]
    
    X_country_count = country_data['Año'].values.reshape(-1, 1)
    y_count_country = country_data['Cantidad'].values
    
    model_count_country = LinearRegression()
    model_count_country.fit(X_country_count, y_count_country)
    
    models_count_by_country[country] = model_count_country
    
    predictions_count_country = model_count_country.predict(np.array(years_to_predict).reshape(-1, 1))
    predictions_count_by_country[country] = predictions_count_country

for country, model_count in models_count_by_country.items():
    
    plt.figure(figsize=(16, 6))
    plt.scatter(earthquakes_count_by_country[earthquakes_count_by_country['Pais'] == country]['Año'], earthquakes_count_by_country[earthquakes_count_by_country['Pais'] == country]['Cantidad'], label='Cantidad de Terremotos Real', color='blue')
    plt.plot(years_to_predict, predictions_count_by_country[country], label='Predicciones', color='red', marker='o')
    
    X_ext_country_count = np.append(country_data['Año'], 2022)
    y_ext_count = model_count.predict(X_ext_country_count.reshape(-1, 1))
    plt.plot(X_ext_country_count, y_ext_count, linestyle='dotted', color='green', label='Modelo')
    
    plt.xlabel('Año')
    plt.ylabel('Cantidad de Terremotos')
    plt.legend()
    
    image_filename_count = os.path.join(country_regression_folder_count, f'prediccion_num_terremotos_{country}.png')
    plt.savefig(image_filename_count)
    plt.close()

print("Regresiones Lineales guardadas exitosamente")