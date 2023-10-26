import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('dataset_limpio_etiquetado_2076326.csv')

X = data[['Magnitud', 'Profundidad']]
y = data['Etiqueta']

X.columns = ['Magnitud', 'Profundidad']
k = 1 
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Función para clasificar un nuevos puntos y devolver la etiqueta
def clasificar_terremoto(magnitud, profundidad):
    nuevo_punto = np.array([[magnitud, profundidad]])
    etiqueta = knn.predict(nuevo_punto)
    return etiqueta[0]

# Grafico de dispersion
fig, ax = plt.subplots()
colors = {
    'Terremoto significativo': 'red',
    'Terremoto leve': 'blue',
    'Terremoto insignificativo': 'green',
}

for label, color in colors.items():
    mask = (data['Etiqueta'] == label)
    ax.scatter(data[mask]['Magnitud'], data[mask]['Profundidad'], c=color, label=label)

# Clasificar y visualizar nuevos puntos
nuevo_punto1 = (5.0, 500)
nuevo_punto2 = (3.6, 750)
nuevo_punto3 = (3.9, 50)
nuevo_punto4 = (5.0, 50)
nuevo_punto5 = (4.5, 400)
nuevo_punto6 = (4.15, 250)

for punto in [nuevo_punto1, nuevo_punto2, nuevo_punto3, nuevo_punto4, nuevo_punto5, nuevo_punto6]:
    etiqueta_predicha = clasificar_terremoto(punto[0], punto[1])
    color_predicho = colors.get(etiqueta_predicha, 'black')
    ax.scatter(punto[0], punto[1], c=color_predicho, marker='x', s=100)

ax.legend()
ax.set_xlabel('Magnitud')
ax.set_ylabel('Profundidad')
plt.title('Clasificación de eventos sísmicos (incluyendo nuevos puntos)')
plt.savefig('Clasificacion/Grafico_dispersion_knn.png')
plt.show()

