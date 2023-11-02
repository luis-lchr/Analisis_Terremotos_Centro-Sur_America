import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import random
import numpy as np

df = pd.read_csv('dataset_limpio_2076326.csv')
data = df[["Magnitud", "Profundidad"]]

#KMeans con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(data)
df['Cluster'] = kmeans.labels_

#Generar puntos aleatorios y clasificarlos
num_points = 200  
random_points = np.array([[random.uniform(min(data["Magnitud"]), max(data["Magnitud"])), 
                           random.uniform(min(data["Profundidad"]), max(data["Profundidad"]))] 
                          for _ in range(num_points)])

random_labels = kmeans.predict(random_points)

random_df = pd.DataFrame(random_points, columns=["Magnitud", "Profundidad"])
random_df['Cluster'] = random_labels

combined_df = pd.concat([df, random_df])

plt.scatter(combined_df[combined_df["Cluster"] != -1]["Magnitud"], combined_df[combined_df["Cluster"] != -1]["Profundidad"],
            c=combined_df[combined_df["Cluster"] != -1]['Cluster'], cmap='viridis', marker='o', alpha=0.5)

plt.xlabel("Magnitud")
plt.ylabel("Profundidad")
plt.title("Diagrama de Dispersión: Magnitud vs. Profundidad (K-means Clustering)")
plt.legend()
plt.savefig('Agrupacion/Grafico_dispersion_kmeans.png')
plt.show()