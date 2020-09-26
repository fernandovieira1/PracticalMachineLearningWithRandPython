#### CAPÍTULO 4 ####
# Algoritmos de ML relacionados a regressão:
# - Regressão simples
# - Regressão múltipla
# - Regressão polinomial
# - KNN

setwd("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython/Chapter4-RegressionofAContinuousVariable")
dir()
source("RFunctions.R")

## Ler os dados
df <- read.csv("Boston.csv") # Considerando o pacote "RFunctions.R", o nome do data frame sempre deve ser 'df'
head(df)
tail(df)

names(df) # https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html

### REGRESSÃO SIMPLES
## Dividir os dados entre dados de treino e de teste (75, 25)
treino_idx <- trainTestSplit(df, trainPercent=75, seed=5) # Função importada de "RFunctions.R"
treino_idx

treino <- df[treino_idx,]
teste <- df[-treino_idx,]

dim(treino)
dim(teste)

## Regressão linear 
# y: Median value of owner-occupied homes in $1000's
# x: lower status of the population
linreg <- lm(medv~lstat, data=df)
summary(linreg, digits = 2)

plot(df$lstat,df$medv, xlab="Lower status (%)",ylab="Median value of owned homes ($1000)", main="Median value of homes ($1000) vs Lowe status (%)")
abline(linreg,lwd=3,col="red")

rsquared <- Rsquared(linreg,teste,teste$medv)
rsquared

round(Rsquared(linreg,treino,treino$medv), 4)