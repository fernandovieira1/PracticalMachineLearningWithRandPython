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
nrow(df)

### REGRESSÃO SIMPLES
## Dividir os dados entre dados de treino e de teste (75, 25)
treino_idx <- trainTestSplit(df, trainPercent=75, seed=5) # Função importada de "RFunctions.R"
treino_idx # não entendi de qual colunas se extraiu os dados
length(treino_idx)

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

### REGRESSÃO MÚLTIPLA
## Ler os dados
crimesDF <- read.csv("crimes.csv")
head(crimesDF)
tail(crimesDF)

names(crimesDF) # https://rpubs.com/ksakwa/470184

# Remover as 7 primeiras colunas
crimesDF1 <- crimesDF[,7:length(crimesDF)]

# Converter todos para numérico
crimesDF2 <- sapply(crimesDF1, as.numeric)
head(crimesDF2)
tail(crimesDF2)

# Procurar por NAs
a <- is.na(crimesDF2)
a

# Substituir NAs por 0
crimesDF2[a] <- 0

# Criar como dataframe
crimesDF2 <- as.data.frame(crimesDF2)

# Separar treino e teste
treino_idx <- trainTestSplit(crimesDF2, trainPercent=75, seed=5)
treino <- crimesDF2[treino_idx,]
teste <- crimesDF2[-treino_idx,]

dim(treino)
dim(teste)

## Regressão linear 
# y: ViolentCrimesPerPop
# x: Todos os outros

linreg <- lm(ViolentCrimesPerPop~., data=treino)
summary(linreg, digits=3)

rsquared <- Rsquared(linreg, teste, teste$ViolentCrimesPerPop)
rsquared

sprintf("R quadrado para regressão linear múltipla (crimes.csv)  é : %f", rsquared)

### 1.4c K Nearest Neighbors Regression – R( Normalized)
Ganesh, Tinniam V. Practical Machine Learning with R and Python: Machine Learning in Stereo (p. 103). Edição do Kindle. 

<<<<<<< HEAD
# Objetivo: encontrar a potência do carro (mpg) de acordo com as características ( cylinder, horsepower etc.)

=======
>>>>>>> 499b5dae9aac4d680335f9a32d5737c88cee216d
df <- read.csv("auto_mpg.csv")
head(df)
tail(df)

df1 <- as.data.frame(sapply(df, as.numeric))
head(df1)
tail(df1)

df2 <- df1 %>% select(cylinder,displacement, horsepower,weight, acceleration, year,mpg)
head(df2)
tail(df2)

df3 <- df2[complete.cases(df2),] # mantém apenas as linhas sem NA
head(df3)
<<<<<<< HEAD
tail(df3)

## Split and train
train_idx <- trainTestSplit(df3, trainPercent=75, seed=5)

train <- df3[train_idx,]
dim(train)

test <- df3[-train_idx,]
dim(test)

train.X <- train[,1:6] # feature
train.Y <- train[,7] # target

test.X <- test[,1:6] # feature
test.Y <- test[,7] # target

# Perform MinMaxScaling of feature variables (normalizar os dados para ficarem entre 0 e 1)
train.X.scaled <- MinMaxScaler(train.X)
test.X.scaled <- MinMaxScaler(test.X)

# Create a list of neighbors
rsquared <- NULL
neighbors <- c(1,2,4,6,8,10,12,15,20,25,30)

for(i in seq_along(neighbors)){
    # Fit a KNN model
    knn = knn.reg(train.X.scaled,test.X.scaled,train.Y,k=i)
    # Compute R ssquared
    rsquared[i] = knnRSquared(knn$pred,test.Y)
}

df <- data.frame(neighbors,Rsquared=rsquared)
df

# Plot the number of neighors vs the R squared
ggplot(df,aes(x=neighbors,y=Rsquared)) + 
geom_point() + 
geom_line(color="blue") + 
xlab("Number of neighbors") + 
ylab("R squared") + 
ggtitle("KNN regression - R squared vs Number of Neighors(Normalized)")

=======
tail(df3)
>>>>>>> 499b5dae9aac4d680335f9a32d5737c88cee216d
