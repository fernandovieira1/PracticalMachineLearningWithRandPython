#### CAPÍTULO 4 ####
# Algoritmos de ML relacionados a regressão:
# - Regressão simples
# - Regressão múltipla
# - Regressão polinomial
# - KNN
import os
os.chdir("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython/Chapter4-RegressionofAContinuousVariable")
os.getcwd()
os.listdir()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



## Ler os dados
df = pd.read_csv("Boston.csv", encoding="ISO-8859-1") # Considerando o pacote "RFunctions.R", o nome do data frame sempre deve ser 'df'

df.columns # https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html

### REGRESSÃO SIMPLES

# Selecionar y e x
y = df["medv"]
X = df["lstat"]

## Dividir os dados entre dados de treino e de teste (75, 25)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, random_state=0)
X_treino

# Colocando os valores em array
X_treino = X_treino.values.reshape(-1,1) 
X_teste = X_teste.values.reshape(-1,1)

X_treino.shape
X_teste.shape

## Regressão linear 
# y: Median value of owner-occupied homes in $1000's
# x: lower status of the population
linreg = LinearRegression().fit(X_treino, y_treino)
linreg.score(X_treino, y_treino)
linreg.intercept_
linreg.coef_

r2Treino = linreg.score(X_treino, y_treino)
r2Treino

r2Teste = linreg.score(X_teste, y_teste)
r2Teste

fig = plt.scatter(X_teste, y_teste) # Create a range of points. Compute yhat=coeff1*x + intercept and plot
x = np.linspace(0, 40, 20)
fig1 = plt.plot(x, linreg.coef_*x + linreg.intercept_, color="red")
fig1 = plt.title("Median value of homes ($1000) vs Lowe status (%)")
fig1 = plt.xlabel("Lower status (%)")
fig1 = plt.ylabel("Median value of owned homes ($1000)")
fig.figure.savefig('foo.png', bbox_inches='tight')
fig1.figure.savefig('foo1.png', bbox_inches='tight')
plt.show()

