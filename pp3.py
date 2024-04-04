import pandas as pd
import matplotlib.pyplot as plt


stations_df = pd.read_csv("STATION.csv")
alertes_df = pd.read_csv("ALERTE.csv")
releves_df = pd.read_csv("RELEVE.csv")
mesures_df = pd.read_csv("MESURE.csv")
lieux_df = pd.read_csv("LIEU.csv")






# Analyse de la fréquence des alertes par catégorie
alertes_df['CATÉGORIE'].value_counts().plot(kind='bar', color='orange')
plt.xlabel('Catégorie')
plt.ylabel('Nombre d\'alertes')
plt.title('Analyse de la fréquence des alertes par catégorie')
plt.xticks(rotation=45)
plt.show()