import os
import pandas as pd
from itertools import combinations
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv('dataset_limpio_2076326.csv')
paises_unicos = df['Pais'].unique()

output_folder = "Pruebas Estadisticas"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

resultados_magnitud = []
resultados_profundidad = []

#Comparaciones de magnitudes y profundidades para cada par de países
for pais1, pais2 in combinations(paises_unicos, 2):
    data_pais1_magnitud = df[df['Pais'] == pais1]['Magnitud']
    data_pais2_magnitud = df[df['Pais'] == pais2]['Magnitud']

    #Prueba de t de Student para comparar las magnitudes
    t_statistic_magnitud, p_value_magnitud = stats.ttest_ind(data_pais1_magnitud, data_pais2_magnitud, equal_var=False) 
    mean_diff_magnitud = data_pais1_magnitud.mean() - data_pais2_magnitud.mean()
    is_significant_magnitud = "La diferencia en magnitudes es estadísticamente significativa." if p_value_magnitud < 0.05 else "No hay evidencia estadística de diferencia en magnitudes."

    resultados_magnitud.append({
        'Comparacion': f"{pais1} vs {pais2}",
        'Estadistica_t': t_statistic_magnitud,
        'Valor_p': p_value_magnitud,
        'Diferencia_en_magnitudes': mean_diff_magnitud,
        'Significativo_nivel_0.05': is_significant_magnitud
    })

    print(f"Comparación entre {pais1} y {pais2} (Magnitud):")
    print("Resultado de la prueba de t (Magnitud):")
    print("Estadística t:", t_statistic_magnitud)
    print("Valor p:", p_value_magnitud)
    print("Diferencia en magnitudes:", mean_diff_magnitud)
    print(is_significant_magnitud)
    print()

    data_pais1_profundidad = df[df['Pais'] == pais1]['Profundidad']
    data_pais2_profundidad = df[df['Pais'] == pais2]['Profundidad']

    #Prueba de t de Student para comparar las profundidades
    t_statistic_profundidad, p_value_profundidad = stats.ttest_ind(data_pais1_profundidad, data_pais2_profundidad, equal_var=False)  
    mean_diff_profundidad = data_pais1_profundidad.mean() - data_pais2_profundidad.mean()
    is_significant_profundidad = "La diferencia en profundidades es estadísticamente significativa." if p_value_profundidad < 0.05 else "No hay evidencia estadística de diferencia en profundidades."

    resultados_profundidad.append({
        'Comparacion': f"{pais1} vs {pais2}",
        'Estadistica_t': t_statistic_profundidad,
        'Valor_p': p_value_profundidad,
        'Diferencia_en_profundidades': mean_diff_profundidad,
        'Significativo_nivel_0.05': is_significant_profundidad
    })

    print(f"Comparación entre {pais1} y {pais2} (Profundidad):")
    print("Resultado de la prueba de t (Profundidad):")
    print("Estadística t:", t_statistic_profundidad)
    print("Valor p:", p_value_profundidad)
    print("Diferencia en profundidades:", mean_diff_profundidad)
    print(is_significant_profundidad)
    print()

resultados_magnitud_df = pd.DataFrame(resultados_magnitud)
resultados_profundidad_df = pd.DataFrame(resultados_profundidad)
resultados_magnitud_csv_path = os.path.join(output_folder, 'Prueba_t_student_comparacion_magnitudes.csv')
resultados_magnitud_df.to_csv(resultados_magnitud_csv_path, index=False)
resultados_profundidad_csv_path = os.path.join(output_folder, 'Prueba_t_student_comparacion_profundidades.csv')
resultados_profundidad_df.to_csv(resultados_profundidad_csv_path, index=False)

print("Resultados de magnitud guardados en:", resultados_magnitud_csv_path)
print("Resultados de profundidad guardados en:", resultados_profundidad_csv_path)

rutas_csv = {
    'ANOVA_magnitud_por_anio': os.path.join(output_folder, 'ANOVA_magnitud_por_anio.csv'),
    'ANOVA_profundidad_por_anio': os.path.join(output_folder, 'ANOVA_profundidad_por_anio.csv'),
    'ANOVA_magnitud_por_mes': os.path.join(output_folder, 'ANOVA_magnitud_por_mes.csv'),
    'ANOVA_profundidad_por_mes': os.path.join(output_folder, 'ANOVA_profundidad_por_mes.csv'),
    'ANOVA_magnitud_por_pais': os.path.join(output_folder, 'ANOVA_magnitud_por_pais.csv'),
    'ANOVA_profundidad_por_pais': os.path.join(output_folder, 'ANOVA_profundidad_por_pais.csv'),
    'ANOVA_magnitud_por_hora': os.path.join(output_folder, 'ANOVA_magnitud_por_hora.csv'),
    'ANOVA_profundidad_por_hora': os.path.join(output_folder, 'ANOVA_profundidad_por_hora.csv'),
    'ANOVA_magnitud_por_estacion': os.path.join(output_folder, 'ANOVA_magnitud_por_estacion.csv'),
    'ANOVA_profundidad_por_estacion': os.path.join(output_folder, 'ANOVA_profundidad_por_estacion.csv')
}

#ANOVA para comparar la magnitud por año
modelo_magnitud_por_anio = ols('Magnitud ~ C(Año)', data=df).fit()
anova_magnitud_por_anio = sm.stats.anova_lm(modelo_magnitud_por_anio, typ=2)
print("ANOVA para la Magnitud por Año:")
print(anova_magnitud_por_anio)
print()

with open(rutas_csv['ANOVA_magnitud_por_anio'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Magnitud por Año\n\n")
    f.write(str(anova_magnitud_por_anio))

#ANOVA para comparar la profundidad por año
modelo_profundidad_por_anio = ols('Profundidad ~ C(Año)', data=df).fit()
anova_profundidad_por_anio = sm.stats.anova_lm(modelo_profundidad_por_anio, typ=2)
print("ANOVA para la Profundidad por Año:")
print(anova_profundidad_por_anio)
print()

with open(rutas_csv['ANOVA_profundidad_por_anio'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Profundidad por Año\n\n")
    f.write(str(anova_profundidad_por_anio))

df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')
df['Hora_del_dia'] = pd.cut(df['Hora'].dt.hour,
                           bins=[0, 6, 12, 18, 24],
                           labels=['Madrugada', 'Mañana', 'Tarde', 'Noche'],
                           include_lowest=True)

#ANOVA para comparar la magnitud entre diferentes horas del día
modelo_magnitud_por_hora = ols('Magnitud ~ C(Hora_del_dia)', data=df).fit()
anova_magnitud_por_hora = sm.stats.anova_lm(modelo_magnitud_por_hora, typ=2)
print("ANOVA para la Magnitud por Hora del Día:")
print(anova_magnitud_por_hora)
print()

with open(rutas_csv['ANOVA_magnitud_por_hora'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Magnitud por Hora del Día\n\n")
    f.write(str(anova_magnitud_por_hora))

#ANOVA para comparar la profundidad entre diferentes horas del día
modelo_profundidad_por_hora = ols('Profundidad ~ C(Hora_del_dia)', data=df).fit()
anova_profundidad_por_hora = sm.stats.anova_lm(modelo_profundidad_por_hora, typ=2)
print("ANOVA para la Profundidad por Hora del Día:")
print(anova_profundidad_por_hora)
print()

with open(rutas_csv['ANOVA_profundidad_por_hora'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Profundidad por Hora del Día\n\n")
    f.write(str(anova_profundidad_por_hora))

df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.month

# ANOVA para comparar la magnitud en diferentes meses
modelo_magnitud_por_mes = ols('Magnitud ~ C(Mes)', data=df).fit()
anova_magnitud_por_mes = sm.stats.anova_lm(modelo_magnitud_por_mes, typ=2)
print("ANOVA para la Magnitud por Mes:")
print(anova_magnitud_por_mes)
print()

with open(rutas_csv['ANOVA_magnitud_por_mes'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Magnitud por Mes\n\n")
    f.write(str(anova_magnitud_por_mes))

#ANOVA para comparar la profundidad en diferentes meses
modelo_profundidad_por_mes = ols('Profundidad ~ C(Mes)', data=df).fit()
anova_profundidad_por_mes = sm.stats.anova_lm(modelo_profundidad_por_mes, typ=2)
print("ANOVA para la Profundidad por Mes:")
print(anova_profundidad_por_mes)
print()

with open(rutas_csv['ANOVA_profundidad_por_mes'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Profundidad por Mes\n\n")
    f.write(str(anova_profundidad_por_mes))

def obtener_estacion(mes):
    if mes in [12, 1, 2]:
        return 'Verano'
    elif mes in [3, 4, 5]:
        return 'Otoño'
    elif mes in [6, 7, 8]:
        return 'Invierno'
    else:
        return 'Primavera'

df['Estacion'] = df['Mes'].apply(obtener_estacion)

#ANOVA para comparar la magnitud en diferentes estaciones del año
modelo_magnitud_por_estacion = ols('Magnitud ~ C(Estacion)', data=df).fit()
anova_magnitud_por_estacion = sm.stats.anova_lm(modelo_magnitud_por_estacion, typ=2)
print("ANOVA para la Magnitud por Estación del Año:")
print(anova_magnitud_por_estacion)
print()

with open(rutas_csv['ANOVA_magnitud_por_estacion'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Magnitud por Estación del Año\n\n")
    f.write(str(anova_magnitud_por_estacion))

#ANOVA para comparar la profundidad en diferentes estaciones del año
modelo_profundidad_por_estacion = ols('Profundidad ~ C(Estacion)', data=df).fit()
anova_profundidad_por_estacion = sm.stats.anova_lm(modelo_profundidad_por_estacion, typ=2)
print("ANOVA para la Profundidad por Estación del Año:")
print(anova_profundidad_por_estacion)
print()

with open(rutas_csv['ANOVA_profundidad_por_estacion'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Profundidad por Estación del Año\n\n")
    f.write(str(anova_profundidad_por_estacion))

#ANOVA para comparar la magnitud por país
modelo_magnitud_por_pais = ols('Magnitud ~ C(Pais)', data=df).fit()
anova_magnitud_por_pais = sm.stats.anova_lm(modelo_magnitud_por_pais, typ=2)
print("ANOVA para la Magnitud por País:")
print(anova_magnitud_por_pais)
print()

with open(rutas_csv['ANOVA_magnitud_por_pais'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Magnitud por País\n\n")
    f.write(str(anova_magnitud_por_pais))

#ANOVA para comparar la profundidad por país
modelo_profundidad_por_pais = ols('Profundidad ~ C(Pais)', data=df).fit()
anova_profundidad_por_pais = sm.stats.anova_lm(modelo_profundidad_por_pais, typ=2)
print("ANOVA para la Profundidad por País:")
print(anova_profundidad_por_pais)
print()

with open(rutas_csv['ANOVA_profundidad_por_pais'], 'w', encoding='utf-8') as f:
    f.write("ANOVA para la Profundidad por País\n\n")
    f.write(str(anova_profundidad_por_pais))
