import os
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

data = pd.read_csv('dataset_limpio_2076326.csv')

output_dir = 'Visualización de Datos'
os.makedirs(output_dir, exist_ok=True)

output_dir_paises = os.path.join(output_dir, 'scatter_plots_by_country')
output_dir_anios = os.path.join(output_dir, 'scatter_plots_by_year')
output_dir_paises_anios = os.path.join(output_dir, 'scatter_plots_by_country_year')
output_dir_boxplots_magnitud = os.path.join(output_dir, 'box_plots_by_year_magnitud')
output_dir_boxplots_profundidad = os.path.join(output_dir, 'box_plots_by_year_profundidad')
output_dir_boxplots_pais_magnitud = os.path.join(output_dir, 'box_plots_by_country_magnitud')
output_dir_boxplots_pais_profundidad = os.path.join(output_dir, 'box_plots_by_country_profundidad')
output_dir_histograms_magnitud = os.path.join(output_dir, 'histograms_magnitud')
output_dir_histograms_profundidad = os.path.join(output_dir, 'histograms_profundidad')
output_dir_lineplots_magnitud = os.path.join(output_dir, 'line_plots_magnitud')
output_dir_lineplots_profundidad = os.path.join(output_dir, 'line_plots_profundidad')
output_dir_barplots_paises = os.path.join(output_dir, 'bar_plots_by_country')
output_dir_barplots_anios = os.path.join(output_dir, 'bar_plots_by_year')
output_dir_maps = os.path.join(output_dir, 'Maps')
os.makedirs(output_dir_paises, exist_ok=True)
os.makedirs(output_dir_anios, exist_ok=True)
os.makedirs(output_dir_paises_anios, exist_ok=True)
os.makedirs(output_dir_boxplots_magnitud, exist_ok=True)
os.makedirs(output_dir_boxplots_profundidad, exist_ok=True)
os.makedirs(output_dir_boxplots_pais_magnitud, exist_ok=True)
os.makedirs(output_dir_boxplots_pais_profundidad, exist_ok=True)
os.makedirs(output_dir_histograms_magnitud, exist_ok=True)
os.makedirs(output_dir_histograms_profundidad, exist_ok=True)
os.makedirs(output_dir_lineplots_magnitud, exist_ok=True)
os.makedirs(output_dir_lineplots_profundidad, exist_ok=True)
os.makedirs(output_dir_barplots_paises, exist_ok=True)
os.makedirs(output_dir_barplots_anios, exist_ok=True)
os.makedirs(output_dir_maps, exist_ok=True)

# Gráficos de dispersión por país
paises_unicos = data['Pais'].unique()
for pais in paises_unicos:
    data_pais = data[data['Pais'] == pais]
    magnitud = data_pais['Magnitud']
    profundidad = data_pais['Profundidad']
    
    plt.scatter(profundidad, magnitud, alpha=0.5)
    plt.xlabel('Profundidad')
    plt.ylabel('Magnitud')
    plt.title(f'Relación entre Magnitud y Profundidad para {pais}')
    file_name = f'{output_dir_paises}/{pais}_scatter_plot.png'
    plt.savefig(file_name)
    plt.close()

print('Gráficos por país guardados en imágenes individuales.')

# Gráficos de dispersión por año
anios_unicos = data['Año'].unique()
for anio in anios_unicos:
    data_anio = data[data['Año'] == anio]
    magnitud = data_anio['Magnitud']
    profundidad = data_anio['Profundidad']
    
    plt.scatter(profundidad, magnitud, alpha=0.5)
    plt.xlabel('Profundidad')
    plt.ylabel('Magnitud')
    plt.title(f'Relación entre Magnitud y Profundidad para el año {anio}')
    file_name = f'{output_dir_anios}/{anio}_scatter_plot.png'
    plt.savefig(file_name)
    plt.close()

print('Gráficos por año guardados en imágenes individuales.')

# Gráficos de dispersión por país y año
for pais in paises_unicos:
    for anio in anios_unicos:
        data_pais_anio = data[(data['Pais'] == pais) & (data['Año'] == anio)]

        # Verifica si hay datos para ese país en ese año
        if not data_pais_anio.empty:
            magnitud = data_pais_anio['Magnitud']
            profundidad = data_pais_anio['Profundidad']

            plt.scatter(profundidad, magnitud, alpha=0.5)
            plt.xlabel('Profundidad')
            plt.ylabel('Magnitud')
            plt.title(f'Relación entre Magnitud y Profundidad para {pais}, año {anio}')
            file_name = f'{output_dir_paises_anios}/{pais}_{anio}_scatter_plot.png'
            plt.savefig(file_name)
            plt.close()
            print(f'Gráfico para {pais}, año {anio} guardado en imágenes individuales.')
        else:
            print(f'No hay datos para {pais}, año {anio}. No se generó el gráfico.')

print('Gráficos por país y año guardados en imágenes individuales.')

# Diagramas de caja por año para la magnitud
plt.figure(figsize=(14, 8)) 

for anio in anios_unicos:
    data_anio = data[data['Año'] == anio]
    magnitud = data_anio['Magnitud']
    
    box_plot = plt.boxplot(magnitud, positions=[anio], labels=[str(anio)])
    plt.setp(box_plot['medians'], color='red') 

plt.xlabel('Año')
plt.ylabel('Magnitud')
plt.title('Distribución de Magnitud por Año')
plt.grid(True)

boxplot_file_name = 'box_plot_by_year_magnitud.png'
plt.savefig(os.path.join(output_dir_boxplots_magnitud, boxplot_file_name))
plt.close()

# Diagramas de caja por año para la profundidad
plt.figure(figsize=(14, 8))  

for anio in anios_unicos:
    data_anio = data[data['Año'] == anio]
    profundidad = data_anio['Profundidad']
    
    box_plot = plt.boxplot(profundidad, positions=[anio], labels=[str(anio)])
    plt.setp(box_plot['medians'], color='red')  

plt.xlabel('Año')
plt.ylabel('Profundidad')
plt.title('Distribución de Profundidad por Año')
plt.grid(True)

boxplot_file_name = 'box_plot_by_year_profundidad.png'
plt.savefig(os.path.join(output_dir_boxplots_profundidad, boxplot_file_name))
plt.close()

# Diagramas de caja por país para la magnitud
plt.figure(figsize=(14, 8))  

for i, pais in enumerate(paises_unicos):
    data_pais = data[data['Pais'] == pais]
    magnitud = data_pais['Magnitud']
    
    box_plot = plt.boxplot(magnitud, positions=[i], labels=[pais])
    plt.setp(box_plot['medians'], color='red')  

plt.xlabel('País')
plt.ylabel('Magnitud')
plt.title('Distribución de Magnitud por País')
plt.xticks(range(len(paises_unicos)), paises_unicos, rotation='vertical') 
plt.grid(True)

boxplot_file_name = 'box_plot_by_country_magnitud.png'
plt.savefig(os.path.join(output_dir_boxplots_pais_magnitud, boxplot_file_name))
plt.close()

# Diagramas de caja por país para la profundidad
plt.figure(figsize=(14, 8))  

for i, pais in enumerate(paises_unicos):
    data_pais = data[data['Pais'] == pais]
    profundidad = data_pais['Profundidad']
    
    box_plot = plt.boxplot(profundidad, positions=[i], labels=[pais])
    plt.setp(box_plot['medians'], color='red') 

plt.xlabel('País')
plt.ylabel('Profundidad')
plt.title('Distribución de Profundidad por País')
plt.xticks(range(len(paises_unicos)), paises_unicos, rotation='vertical')  
plt.grid(True)

boxplot_file_name = 'box_plot_by_country_profundidad.png'
plt.savefig(os.path.join(output_dir_boxplots_pais_profundidad, boxplot_file_name))
plt.close()

# Histogramas de magnitud por año
for anio in anios_unicos:
    data_anio = data[data['Año'] == anio]
    magnitud = data_anio['Magnitud']
    
    plt.hist(magnitud, bins=20, alpha=0.7, label='Magnitud')
    plt.xlabel('Magnitud')
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de Magnitud para el año {anio}')
    plt.legend()
    
    hist_file_name = f'{output_dir_histograms_magnitud}/{anio}_histogram_magnitud.png'
    plt.savefig(hist_file_name)
    plt.close()

print('Histogramas de magnitud por año guardados en imágenes individuales.')

# Histogramas de profundidad por año
for anio in anios_unicos:
    data_anio = data[data['Año'] == anio]
    profundidad = data_anio['Profundidad']
    
    plt.hist(profundidad, bins=20, alpha=0.7, label='Profundidad')
    plt.xlabel('Profundidad')
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de Profundidad para el año {anio}')
    plt.legend()
    
    hist_file_name = f'{output_dir_histograms_profundidad}/{anio}_histogram_profundidad.png'
    plt.savefig(hist_file_name)
    plt.close()

print('Histogramas de profundidad por año guardados en imágenes individuales.')

# Histogramas de magnitud por país
for pais in paises_unicos:
    data_pais = data[data['Pais'] == pais]
    magnitud = data_pais['Magnitud']
    
    plt.hist(magnitud, bins=20, alpha=0.7, label='Magnitud')
    plt.xlabel('Magnitud')
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de Magnitud para {pais}')
    plt.legend()
    
    hist_file_name = f'{output_dir_histograms_magnitud}/{pais}_histogram_magnitud.png'
    plt.savefig(hist_file_name)
    plt.close()

print('Histogramas de magnitud por país guardados en imágenes individuales.')

# Histogramas de profundidad por país
for pais in paises_unicos:
    data_pais = data[data['Pais'] == pais]
    profundidad = data_pais['Profundidad']
    
    plt.hist(profundidad, bins=20, alpha=0.7, label='Profundidad')
    plt.xlabel('Profundidad')
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de Profundidad para {pais}')
    plt.legend()
    
    hist_file_name = f'{output_dir_histograms_profundidad}/{pais}_histogram_profundidad.png'
    plt.savefig(hist_file_name)
    plt.close()

print('Histogramas de profundidad por país guardados en imágenes individuales.')

# Gráfico de barras para la cantidad de registros por país
registros_por_pais = data['Pais'].value_counts()

plt.figure(figsize=(14, 8))
plt.bar(registros_por_pais.index, registros_por_pais.values)
plt.xlabel('País')
plt.ylabel('Cantidad de Registros')
plt.title('Cantidad de Registros por País')
plt.xticks(rotation='vertical')
barplot_paises_file_name = 'bar_plot_registros_por_pais.png'
plt.savefig(os.path.join(output_dir_barplots_paises, barplot_paises_file_name))
plt.close()

print('Gráfico de barras de registros por país guardado en una imagen.')

# Gráfico de barras para la cantidad de registros por año
registros_por_anio = data['Año'].value_counts().sort_index()

plt.figure(figsize=(14, 8))
plt.bar(registros_por_anio.index.astype(str), registros_por_anio.values)
plt.xlabel('Año')
plt.ylabel('Cantidad de Registros')
plt.title('Cantidad de Registros por Año')
plt.xticks(rotation='vertical')
barplot_anios_file_name = 'bar_plot_registros_por_anio.png'
plt.savefig(os.path.join(output_dir_barplots_anios, barplot_anios_file_name))
plt.close()

print('Gráfico de barras de registros por año guardado en una imagen.')

# Gráfico de línea para la evolución de la magnitud a lo largo del tiempo
plt.figure(figsize=(14, 8))

media_magnitud_por_anio = data.groupby('Año')['Magnitud'].mean()

plt.plot(media_magnitud_por_anio.index, media_magnitud_por_anio, label='Magnitud', marker='o')

plt.xlabel('Año')
plt.ylabel('Media de Magnitud')
plt.title('Evolución de la Magnitud a lo largo del tiempo')
plt.legend()
plt.grid(True)

lineplot_magnitud_file_name = 'line_plot_magnitud.png'
plt.savefig(os.path.join(output_dir_lineplots_magnitud, lineplot_magnitud_file_name))

print('Gráfico de evolución de Magnitud guardado en una imagen.')
plt.close()

# Gráfico de línea para la evolución de la profundidad a lo largo del tiempo
plt.figure(figsize=(14, 8))

media_profundidad_por_anio = data.groupby('Año')['Profundidad'].mean()

plt.plot(media_profundidad_por_anio.index, media_profundidad_por_anio, label='Profundidad', marker='o')

plt.xlabel('Año')
plt.ylabel('Media de Profundidad')
plt.title('Evolución de la Profundidad a lo largo del tiempo')
plt.legend()
plt.grid(True)

lineplot_profundidad_file_name = 'line_plot_profundidad.png'
plt.savefig(os.path.join(output_dir_lineplots_profundidad, lineplot_profundidad_file_name))

print('Gráfico de evolución de Profundidad guardado en una imagen.')
plt.close()

carpeta_guardado = "Visualización de Datos/Maps" 

# Mapa para la cantidad de registros de terremotos por país
registros_por_pais = data['Pais'].value_counts().reset_index()
registros_por_pais.columns = ['Pais', 'Cantidad']

media_magnitudes_por_pais = data.groupby('Pais')['Magnitud'].mean().reset_index()
media_profundidad_por_pais = data.groupby('Pais')['Profundidad'].mean().reset_index()

lat_lims = [-60, 85]  
lon_lims = [-170, -30]  

mapa_cantidad_registros = px.choropleth(registros_por_pais, 
                                        locations='Pais', 
                                        locationmode='country names',
                                        color='Cantidad', 
                                        hover_name='Pais',
                                        title='Cantidad de Registros de Terremotos por País',
                                        center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
                                        projection='natural earth',
                                        range_color=(0, registros_por_pais['Cantidad'].max()),  
                                        labels={'Cantidad': 'Cantidad de Registros'})

mapa_cantidad_registros.update_geos(
    visible=False, 
    lataxis_range=lat_lims, 
    lonaxis_range=lon_lims
)

mapa_cantidad_registros.update_layout(
    geo=dict(
        center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
        projection_scale=1,  
    ),
    height=400,  
    width=600  
)

mapa_cantidad_registros.write_image(os.path.join(carpeta_guardado, 'mapa_cantidad_registros_continente_americano.png'))
print('Mapa Cloropleta representando la cantidad de terremotos por país guardado en una imagen')

# Mapa para la media de las magnitudes
mapa_media_magnitudes = px.choropleth(media_magnitudes_por_pais, 
                                      locations='Pais', 
                                      locationmode='country names',
                                      color='Magnitud', 
                                      hover_name='Pais',
                                      title='Media de Magnitudes de Terremotos por País',
                                      center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
                                      projection='natural earth',
                                      range_color=(media_magnitudes_por_pais['Magnitud'].min(), media_magnitudes_por_pais['Magnitud'].max()),  
                                      labels={'Magnitud': 'Media de Magnitudes'})

mapa_media_magnitudes.update_geos(
    visible=False, 
    lataxis_range=lat_lims, 
    lonaxis_range=lon_lims
)

mapa_media_magnitudes.update_layout(
    geo=dict(
        center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
        projection_scale=1,  
    ),
    height=400,  
    width=600  
)

mapa_media_magnitudes.write_image(os.path.join(carpeta_guardado, 'mapa_media_magnitudes_continente_americano.png'))
print('Mapa Cloropleta representando la media de magnitudes por país guardado en una imagen')

# Mapa para la media de la profundidad
mapa_media_profundidad = px.choropleth(media_profundidad_por_pais, 
                                       locations='Pais', 
                                       locationmode='country names',
                                       color='Profundidad', 
                                       hover_name='Pais',
                                       title='Media de Profundidad de Terremotos por País',
                                       center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
                                       projection='natural earth',
                                       range_color=(media_profundidad_por_pais['Profundidad'].min(), media_profundidad_por_pais['Profundidad'].max()), 
                                       labels={'Profundidad': 'Media de Profundidad'})

mapa_media_profundidad.update_geos(
    visible=False, 
    lataxis_range=lat_lims, 
    lonaxis_range=lon_lims
)

mapa_media_profundidad.update_layout(
    geo=dict(
        center=dict(lat=(lat_lims[0] + lat_lims[1]) / 2, lon=(lon_lims[0] + lon_lims[1]) / 2),
        projection_scale=1,  
    ),
    height=400,  
    width=600  
)

mapa_media_profundidad.write_image(os.path.join(carpeta_guardado, 'mapa_media_profundidad_continente_americano.png'))
print('Mapa Cloropleta representando la media de profundidad por país guardado en una imagen')