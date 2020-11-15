#### CAPÍTULO 4 ####
# Algoritmos de ML relacionados a regressão:
# - Regressão simples
# - Regressão múltipla
# - Regressão polinomial
# - KNN
import os
os.chdir("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython/Chapter4-RegressionofAContinuousVariable")
os.chdir("C:/Users/70485992191/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython-2/Chapter4-RegressionofAContinuousVariable")
os.getcwd()
os.listdir()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

## Ler os dados
df = pd.read_csv("Boston.csv") # Considerando o pacote "RFunctions.R", o nome do data frame sempre deve ser 'df'
df
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

### REGRESSÃO MÚLTIPLA
# Ler os dados
crimesDF = pd.read_csv("crimes.csv", encoding="ISO-8859-1")
crimesDF

crimesDF.columns # https://rpubs.com/ksakwa/470184

# Remover as 7 primeiras colunas
crimesDF1 = crimesDF.iloc[:,7:crimesDF.shape[1]]

# Convert to numeric
crimesDF2 = crimesDF1.apply(pd.to_numeric, errors='coerce')

# Impute NA to 0s
crimesDF2.fillna(0, inplace=True)

# Selecionar y e x
y = crimesDF2.iloc[:,121]
X = crimesDF2.iloc[:,0:120]

## Dividir os dados entre dados de treino e de teste (75, 25)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, random_state=0)
X_treino

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

### 1.4c K Nearest Neighbors Regression – R( Normalized)
Ganesh, Tinniam V. Practical Machine Learning with R and Python: Machine Learning in Stereo (p. 105). Edição do Kindle.

# Objetivo: encontrar a potência do carro (mpg) de acordo com as características ( cylinder, horsepower etc.)

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler

autoDF = pd.read_csv("auto_mpg.csv",encoding="ISO-8859-1")
autoDF.shape
autoDF.columns

autoDF1 = autoDF[['mpg','cylinder','displacement','horsepower','weight','acceleration','year']]

autoDF2 = autoDF1.apply(pd.to_numeric, errors='coerce')

autoDF3 = autoDF2.dropna()
autoDF3.shape

X = autoDF3[['cylinder','displacement','horsepower','weight','acceleration','year']]
y = autoDF3['mpg']

# Perform a train/ testsplit
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

# Use MinMaxScaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Apply scaling on test set
X_test_scaled = scaler.transform(X_test)

# Create a list of neighbors
rsquared=[]
neighbors=[1,2,4,6,8,10,12,15,20,25,30]

for i in neighbors:
    # Fit a KNN model
    knnreg = KNeighborsRegressor(n_neighbors = i).fit(X_train_scaled, y_train)
    # Compute R squared
    rsquared.append(knnreg.score(X_test_scaled, y_test))
    print('R-squared test score: {:.3f}'.format(knnreg.score(X_test_scaled, y_test)))
    
# Plot the number of neighors vs the R squared
fig4=plt.plot(neighbors,rsquared)
fig4=plt.title("KNN regression - R squared vs Number of neighbors(Normalized)")
fig4=plt.xlabel("Neighbors")
fig4=plt.ylabel("R squared")
fig4.figure.savefig('foo4.png', bbox_inches='tight')
plt.show()
print("Finished plotting and saving")

## R-squared test score: 0.703
## R-squared test score: 0.810
## R-squared test score: 0.830

