# California Census Data Clustering Using K-Means

🇧🇷 Português | 🇺🇸 English

---

# 🇧🇷 Português

## Sobre o Projeto

Este projeto aplica técnicas de Machine Learning Não Supervisionado para identificar padrões e agrupamentos em dados do censo habitacional da Califórnia utilizando o algoritmo K-Means.

O objetivo é segmentar regiões com características semelhantes relacionadas à renda, população, habitação e valor dos imóveis, permitindo a descoberta de padrões ocultos sem a utilização de rótulos previamente definidos.

---

## Objetivo

Desenvolver um modelo de clusterização capaz de agrupar regiões da Califórnia com características socioeconômicas semelhantes.

A análise busca identificar padrões importantes presentes nos dados e compreender melhor as relações entre renda, habitação e valor dos imóveis.

---

## Dataset

O projeto utiliza o California Housing Dataset, amplamente empregado em estudos de aprendizado de máquina e mineração de dados.

O conjunto contém informações demográficas e habitacionais coletadas a partir do censo da Califórnia.

### Variáveis Utilizadas

| Variável           | Descrição                     |
| ------------------ | ----------------------------- |
| Longitude          | Longitude da região           |
| Latitude           | Latitude da região            |
| Housing Median Age | Idade mediana das residências |
| Total Rooms        | Total de cômodos              |
| Total Bedrooms     | Total de quartos              |
| Population         | População da região           |
| Households         | Número de domicílios          |
| Median Income      | Renda mediana                 |
| Median House Value | Valor mediano dos imóveis     |

---

## Análise Exploratória dos Dados

Foram realizadas etapas de exploração dos dados, incluindo:

* Visualização das primeiras linhas do dataset;
* Verificação de valores ausentes;
* Estatísticas descritivas;
* Análise da distribuição das variáveis;
* Matriz de correlação entre os atributos.

Essas análises permitem compreender melhor a estrutura dos dados antes da aplicação do algoritmo de agrupamento.

---

## Pré-processamento

Como o algoritmo K-Means utiliza distância euclidiana para formar os agrupamentos, foi necessário realizar a padronização dos dados.

Foi utilizado o método:

* StandardScaler

Esse processo garante que todas as variáveis contribuam de forma equilibrada para o cálculo das distâncias, evitando que atributos com escalas maiores tenham influência excessiva na formação dos clusters.

---

## Modelo Utilizado

### K-Means Clustering

K-Means é um algoritmo de aprendizado não supervisionado utilizado para agrupar observações semelhantes.

O funcionamento do algoritmo ocorre em quatro etapas principais:

1. Define-se o número de clusters (K);
2. O algoritmo escolhe centroides iniciais;
3. Cada observação é associada ao centroide mais próximo;
4. Os centroides são recalculados até a convergência do modelo.

O resultado é a formação de grupos com características semelhantes internamente e diferentes dos demais grupos.

---

## Escolha do Número de Clusters

Para determinar a quantidade ideal de clusters, foi utilizado o Método do Cotovelo (Elbow Method).

Essa técnica avalia a inércia do modelo para diferentes valores de K e identifica o ponto onde o ganho de desempenho começa a diminuir.

O valor escolhido permitiu obter agrupamentos representativos sem aumentar desnecessariamente a complexidade do modelo.

---

## Análise dos Clusters

Após a aplicação do K-Means, os grupos formados foram analisados por meio das médias das variáveis em cada cluster.

A análise permitiu identificar:

* Regiões com alta renda e imóveis valorizados;
* Regiões com renda intermediária e preços moderados;
* Regiões com menor renda e menor valor imobiliário;
* Áreas com características populacionais e habitacionais específicas.

---

## Visualização dos Resultados

Foram construídos gráficos para facilitar a interpretação dos agrupamentos, incluindo:

* Histograma das variáveis;
* Matriz de correlação;
* Gráfico do Método do Cotovelo;
* Visualização dos clusters em relação à renda média e ao valor dos imóveis.

Essas visualizações ajudam a compreender a distribuição dos dados e a separação dos grupos encontrados.

---

## Insights Obtidos

A análise revelou padrões importantes nos dados:

* A renda média possui forte relação com o valor dos imóveis;
* Regiões economicamente semelhantes tendem a ser agrupadas no mesmo cluster;
* O algoritmo conseguiu identificar segmentos distintos do mercado habitacional da Califórnia;
* A clusterização permitiu descobrir padrões sem a necessidade de uma variável alvo.

---

## Conclusão

O algoritmo K-Means demonstrou ser uma ferramenta eficiente para segmentação e análise exploratória de dados habitacionais.

O projeto evidenciou a capacidade do aprendizado não supervisionado em identificar padrões ocultos, fornecendo insights relevantes sobre características socioeconômicas e imobiliárias presentes no conjunto de dados.

---

# 🇺🇸 English

## About the Project

This project applies Unsupervised Machine Learning techniques to identify patterns and clusters within California housing census data using the K-Means algorithm.

The objective is to segment regions with similar characteristics related to income, population, housing conditions, and property values, enabling the discovery of hidden patterns without predefined labels.

---

## Objective

Build a clustering model capable of grouping California regions with similar socioeconomic characteristics.

The analysis aims to identify meaningful patterns within the data and better understand the relationships between income, housing, and property values.

---

## Dataset

The project uses the California Housing Dataset, one of the most widely used datasets for Machine Learning and Data Mining studies.

The dataset contains demographic and housing information collected from California census records.

### Features

| Feature            | Description              |
| ------------------ | ------------------------ |
| Longitude          | Geographic longitude     |
| Latitude           | Geographic latitude      |
| Housing Median Age | Median age of houses     |
| Total Rooms        | Total number of rooms    |
| Total Bedrooms     | Total number of bedrooms |
| Population         | Population size          |
| Households         | Number of households     |
| Median Income      | Median income            |
| Median House Value | Median property value    |

---

## Exploratory Data Analysis

The project includes:

* Dataset inspection;
* Missing value verification;
* Descriptive statistics;
* Feature distribution analysis;
* Correlation matrix visualization.

These steps help understand the dataset before applying clustering techniques.

---

## Data Preprocessing

Since K-Means is based on Euclidean distance calculations, feature scaling is required.

The project uses:

* StandardScaler

This process ensures that all variables contribute equally to distance calculations, preventing features with larger scales from dominating the clustering process.

---

## Model

### K-Means Clustering

K-Means is an unsupervised learning algorithm used to group similar observations.

The algorithm follows four main steps:

1. Define the number of clusters (K);
2. Initialize cluster centroids;
3. Assign observations to the nearest centroid;
4. Recalculate centroids until convergence.

The result is a set of clusters with high internal similarity and clear separation from other groups.

---

## Choosing the Number of Clusters

The Elbow Method was used to determine the optimal number of clusters.

This technique evaluates model inertia across different values of K and identifies the point where improvements begin to diminish.

The selected value provided representative clusters without unnecessarily increasing model complexity.

---

## Cluster Analysis

After applying K-Means, cluster characteristics were analyzed using the average values of each feature.

The analysis revealed:

* High-income regions with expensive properties;
* Middle-income regions with moderate housing values;
* Lower-income regions with lower property prices;
* Areas with distinct demographic and housing characteristics.

---

## Results Visualization

Several visualizations were created to facilitate cluster interpretation, including:

* Feature histograms;
* Correlation matrix;
* Elbow Method graph;
* Cluster visualization based on median income and housing values.

These visualizations help understand both data distribution and cluster separation.

---

## Insights

The analysis revealed important patterns:

* Median income has a strong relationship with housing values;
* Economically similar regions tend to belong to the same cluster;
* The algorithm successfully identified distinct housing market segments;
* Clustering uncovered hidden patterns without requiring a target variable.

---

## Conclusion

The K-Means algorithm proved to be an effective tool for segmentation and exploratory analysis of housing data.

This project highlights the power of unsupervised learning techniques in discovering hidden structures within datasets and generating valuable socioeconomic insights.

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

---

## Author

Flávia Vitória de Queiroz
