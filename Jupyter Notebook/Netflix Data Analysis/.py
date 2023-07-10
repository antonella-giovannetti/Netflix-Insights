import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv('votre_fichier.csv')

# Compter le nombre d'occurrences de chaque réalisateur
director_counts = data['director'].value_counts()

# Sélectionner les dix réalisateurs les plus fréquents
top_directors = director_counts.head(10)

# Tracer le graphique en utilisant un diagramme à barres
plt.bar(top_directors.index, top_directors.values)
plt.xlabel('Réalisateurs')
plt.ylabel('Nombre d\'apparitions')
plt.title('Nombre d\'apparitions des dix réalisateurs les plus fréquents')
plt.xticks(rotation=90)
plt.show()