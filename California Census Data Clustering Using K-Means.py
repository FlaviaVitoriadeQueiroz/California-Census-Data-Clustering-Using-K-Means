'''Projeto: Agrupamento de Dados do Censo da Califórnia com K-Means
Objetivo
O objetivo deste projeto é utilizar o algoritmo K-Means para identificar grupos semelhantes de regiões da Califórnia 
com base em características socioeconômicas e habitacionais presentes no conjunto de dados California Housing. 
Por meio da clusterização, busca-se descobrir padrões ocultos nos dados sem utilizar informações prévias de classificação.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer


# Carregar o conjunto de dados California Housing
df = pd.read_csv(r"C:\Users\F Vitória de Queiroz\Downloads\housing.csv")
df.head()

# EDA
print("Linhas e Colunas:")
print(df.shape)

df.info()

print(df.isnull().sum())

print(df.describe())


# Visualização dos Dados
# Histograma das Variáveis
df.hist(figsize=(15,10), bins=20)
plt.show()

# Matriz de Correlação
plt.figure(figsize=(10,8))
sns.heatmap( df.drop('ocean_proximity', axis=1).corr(), annot=True, cmap="coolwarm")
plt.show()


# Padronização dos Dados
imputer = SimpleImputer(strategy='mean')
dados_imputados = imputer.fit_transform(df.drop('ocean_proximity', axis=1))
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados_imputados)


# Método do Cotovelo
imputer = SimpleImputer(strategy='mean')
dados_padronizados = scaler.fit_transform(dados_imputados)

inercia = []

for k in range(1,11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(dados_padronizados)
    inercia.append(kmeans.inertia_)


# Gráfico do Cotovelo
plt.figure(figsize=(8,5))
plt.plot(range(1,11), inercia, marker="o")
plt.xlabel("Número de Clusters")
plt.ylabel("Inércia")
plt.title("Método do Cotovelo")

plt.show()


# Silhouette Score para validar K
from sklearn.metrics import silhouette_score

scores = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(dados_padronizados)
    scores.append(silhouette_score(dados_padronizados, labels))

plt.plot(range(2, 11), scores, marker='o')
plt.title('Silhouette Score por K')
plt.show()


# Removendo variáveis multicolineares
# total_bedrooms e households são quase redundantes com total_rooms
# Remover pode melhorar a qualidade dos clusters
features = ['longitude', 'latitude', 'housing_median_age',
            'median_income', 'median_house_value', 'population']


# Aplicação do K-Means
# K = 4 (com base no gráfico do cotovelo)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clusters = kmeans.fit_predict(dados_padronizados)

df["Cluster"] = clusters


# Quantidade de Registros por Cluster
print(df["Cluster"].value_counts())


# Características de Cada Cluster
analise_clusters = df.drop('ocean_proximity', axis=1).groupby("Cluster").mean()
print(analise_clusters)


# Visualização dos Clusters
plt.figure(figsize=(10,6))
plt.scatter(df["median_income"], df["median_house_value"], c=df["Cluster"], cmap="viridis")
plt.xlabel("Renda Média")
plt.ylabel("Preço Médio das Casas")
plt.title("Clusters Identificados pelo K-Means")
plt.show()


# Mapa Geográfico
plt.figure(figsize=(10, 6))
plt.scatter(df["longitude"], df["latitude"], c=df["Cluster"], cmap="viridis", alpha=0.4, s=5)
plt.colorbar(label="Cluster")
plt.title("Distribuição Geográfica dos Clusters")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()