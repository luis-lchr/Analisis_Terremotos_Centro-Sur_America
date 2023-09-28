import pandas as pd
import os

data = pd.read_csv('dataset_limpio_2076326.csv')

# Obtener Año, Mes, Día
data['Fecha'] = pd.to_datetime(data['Fecha'])
data['Año'] = data['Fecha'].dt.year
data['Mes'] = data['Fecha'].dt.month
data['DiaSemana'] = data['Fecha'].dt.dayofweek

data['Profundidad'] = pd.to_numeric(data['Profundidad'], errors='coerce')
data = data.dropna(subset=['Profundidad'])

# Agrupar por País, Año y calcular estadísticas descriptivas de la magnitud
estadisticas_por_pais_anio_de_magnitud = data.groupby(['Pais', 'Año'])['Magnitud'].agg(['sum', 'count', 'mean', 'min', 'max']).reset_index()
estadisticas_por_pais_anio_de_magnitud['mean'] = estadisticas_por_pais_anio_de_magnitud['mean'].round(5)

# Agrupar por País, Año y calcular estadísticas descriptivas de la profundidad
estadisticas_por_pais_anio_de_profundidad = data.groupby(['Pais', 'Año'])['Profundidad'].agg(['sum', 'count', 'mean', 'min', 'max']).reset_index()
estadisticas_por_pais_anio_de_profundidad['mean'] = estadisticas_por_pais_anio_de_profundidad['mean'].round(5)

# Calcular la cantidad total de sismos por país
sismos_por_pais = data.groupby('Pais').size()
magnitud_promedio_por_pais = data.groupby('Pais')['Magnitud'].mean()
profundidad_promedio_por_pais = data.groupby('Pais')['Profundidad'].mean()

# Calcular la cantidad total de sismos por año
sismos_por_anio = data.groupby('Año').size()
magnitud_promedio_por_anio = data.groupby('Año')['Magnitud'].mean()
profundidad_promedio_por_anio = data.groupby('Año')['Profundidad'].mean()

# Calcular estadísticas por mes
estadisticas_por_mes = data.groupby('Mes')[['Magnitud', 'Profundidad']].agg(['mean', 'min', 'max', 'count'])
estadisticas_por_mes.columns = ['_'.join(col).strip() for col in estadisticas_por_mes.columns.values]
estadisticas_por_mes.reset_index(inplace=True)
estadisticas_por_mes['Magnitud_mean'] = estadisticas_por_mes['Magnitud_mean'].round(5)
estadisticas_por_mes['Profundidad_mean'] = estadisticas_por_mes['Profundidad_mean'].round(5)

# Calcular estadísticas por día de la semana
estadisticas_por_dia_semana = data.groupby('DiaSemana')[['Magnitud', 'Profundidad']].agg(['mean', 'min', 'max', 'count'])
estadisticas_por_dia_semana.columns = ['_'.join(col).strip() for col in estadisticas_por_dia_semana.columns.values]
estadisticas_por_dia_semana.reset_index(inplace=True)
estadisticas_por_dia_semana['Magnitud_mean'] = estadisticas_por_dia_semana['Magnitud_mean'].round(5)
estadisticas_por_dia_semana['Profundidad_mean'] = estadisticas_por_dia_semana['Profundidad_mean'].round(5)

# Carpeta para resultados
carpeta_resultados = 'Estadistica Descriptiva'

if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)

# Crear DataFrames
sismos_por_pais_df = sismos_por_pais.reset_index()
magnitud_promedio_por_pais_df = magnitud_promedio_por_pais.reset_index()
magnitud_promedio_por_pais_df['Magnitud'] = magnitud_promedio_por_pais_df['Magnitud'].round(5)
profundidad_promedio_por_pais_df = profundidad_promedio_por_pais.reset_index()
profundidad_promedio_por_pais_df['Profundidad'] = profundidad_promedio_por_pais_df['Profundidad'].round(5)
estadisticas_por_pais_anio_de_magnitud_df = estadisticas_por_pais_anio_de_magnitud.reset_index()
estadisticas_por_pais_anio_de_profundidad_df = estadisticas_por_pais_anio_de_profundidad.reset_index()
estadisticas_por_pais_anio_de_magnitud_df.drop(columns=['index'], inplace=True)
estadisticas_por_pais_anio_de_profundidad_df.drop(columns=['index'], inplace=True)
sismos_por_anio_df = sismos_por_anio.reset_index()
magnitud_promedio_por_anio_df = magnitud_promedio_por_anio.reset_index()
magnitud_promedio_por_anio_df['Magnitud'] = magnitud_promedio_por_anio_df['Magnitud'].round(5)
profundidad_promedio_por_anio_df = profundidad_promedio_por_anio.reset_index()
profundidad_promedio_por_anio_df['Profundidad'] = profundidad_promedio_por_anio_df['Profundidad'].round(5)

# Rutas para la carpeta 
sismos_por_pais_csv = os.path.join(carpeta_resultados, 'sismos_por_pais.csv')
magnitud_promedio_por_pais_csv = os.path.join(carpeta_resultados, 'magnitud_promedio_por_pais.csv')
profundidad_promedio_por_pais_csv = os.path.join(carpeta_resultados, 'profundidad_promedio_por_pais.csv')
estadisticas_por_pais_anio_de_magnitud_csv = os.path.join(carpeta_resultados, "estadisticas_por_pais_anio_de_magnitud.csv")
estadisticas_por_pais_anio_de_profundidad_csv = os.path.join(carpeta_resultados, "estadisticas_por_pais_anio_de_profundidad.csv")
sismos_por_anio_csv = os.path.join(carpeta_resultados, 'sismos_por_anio.csv')
magnitud_promedio_por_anio_csv = os.path.join(carpeta_resultados, 'magnitud_promedio_por_anio.csv')
profundidad_promedio_por_anio_csv = os.path.join(carpeta_resultados, 'profundidad_promedio_por_anio.csv')
estadisticas_por_mes_csv = os.path.join(carpeta_resultados, 'estadisticas_por_mes.csv')
estadisticas_por_dia_semana_csv = os.path.join(carpeta_resultados, 'estadisticas_por_dia_semana.csv')

# Guardar los CSV
sismos_por_pais_df.to_csv(sismos_por_pais_csv, index=False)
magnitud_promedio_por_pais_df.to_csv(magnitud_promedio_por_pais_csv, index=False)
profundidad_promedio_por_pais_df.to_csv(profundidad_promedio_por_pais_csv, index=False)
estadisticas_por_pais_anio_de_magnitud_df.to_csv(estadisticas_por_pais_anio_de_magnitud_csv, index=False)
estadisticas_por_pais_anio_de_profundidad_df.to_csv(estadisticas_por_pais_anio_de_profundidad_csv, index=False)
sismos_por_anio_df.to_csv(sismos_por_anio_csv, index=False)
magnitud_promedio_por_anio_df.to_csv(magnitud_promedio_por_anio_csv, index=False)
profundidad_promedio_por_anio_df.to_csv(profundidad_promedio_por_anio_csv, index=False)
estadisticas_por_mes.to_csv(estadisticas_por_mes_csv, index=False)
estadisticas_por_dia_semana.to_csv(estadisticas_por_dia_semana_csv, index=False)

print('Resultados guardados en la carpeta "Estadistica Descriptiva".')
