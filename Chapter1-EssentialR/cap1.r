#### Chapter 1: Essential R ####
# Mais detalhes no arquivo 'EssentialR-1.Rmd'
setwd("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython/Chapter1-EssentialR")
dir()

## Tipos de variáveis
# R has the following variable types 
# 1.Character 
print("Olá, mundo!")
class("Olá, mundo!")
# 2. Integer
print(as.integer(2))
class(as.integer(2))
# 3. Numeric 
print(2)
class(2)
# 4. Logical
print(4>=3)
class(4>=3)
# 5. Complex
print(1 + 2i)
class(1 + 2i)
# 6. Raw
raw(length = 0)
class(raw(length = 0))

## Conjuntos de dados

## Vetores
# Todos os elementos são do mesmo tipo
meuVetor <- c(1,2,4,55,7,88)
print(meuVetor)
class(meuVetor)

meuVetor2 <- c("um", "dois", "cem")
print(meuVetor2)
class(meuVetor2)

## Matrizes
minhaMatriz <- matrix(1:20, nrow=5, ncol=4)
print(minhaMatriz)

## Listas
# Os elementos podem ser de tipos diferentes
w <- list(nome="Fred", meusNumerosEscritos=meuVetor, minhaMatriz5x5=minhaMatriz, idade=5.3)
print(w)
class(w)

## Data frames
# Seguem a mesma lógica do Excel. Mistura os conceitos de matrizes (linhas e colunas) com listas
# (elementos de tipos diferentes), por isso são os mais usados.
d <- c(1,2,3,4)
e <- c("red", "white", "red", NA) 
f <- c(TRUE,TRUE,TRUE,FALSE) 
mydataframe <- data.frame(d,e,f) 
names(mydataframe) <- c("ID","Color","Passed") # variable names mydataframe
mydataframe

## Comandos úteis
ls() # mostra todos os objetos no ambiente/environment
rm("talObjeto") # remove um objeto do ambiente
rm(list=ls()) # remove todos os objetos do ambiente
colnames() # nome de colunas
names() # nome de colunas
sapply(iris, class) # Verificar o tipo de cada coluna
par(mfrow=c(2,2)) # seta o display para duas linhas e duas colunas
dev.off() # Reseta o display
pairs(iris) # fará gráficos de dispersão de pares de dados (bom para ver correlação e tendências)
?complete.cases

Ganesh, Tinniam V. Practical Machine Learning with R and Python: Machine Learning in Stereo (p. 21). Edição do Kindle. 

## For loops
# Try to use vector functions using sapply,lapply,tapply instead of ‘for’ loops. for loops are very performance intensive.
for(i in 1:5){
    print(i)
}

for(i in 1:5){
    print(i*5)
}

## Funções
produto <- function(a, b) {
    c = a*b
    c
}
produto(2, 4)