## Pulei as partes básicas (atentar arquivo 'colinhas' e 'EssentialPython.Rmd')

import os
os.chdir("/Users/fernandovieira/OneDrive/1. Educacao/INFO E ESTAT/RAIZ_Livro_ML_Tinnian_Ganesh/PracticalMachineLearningWithRandPython/Chapter2-EssentialPythonForDatascience")
os.getcwd()
os.listdir()


import pandas as pd
tendulkar = pd.read_csv("tendulkar1.csv", encoding="ISO-8859-1")
tendulkar


## Operações lambda
a =[5,2,3,1,7]
b =[1,5,4,6,8]

add = lambda x,y: x+y
square = lambda x: x**2

print(list(map(add,a,b)))
add(4,6)

print(list(map(square,a)))
square(2)

# Lambda em uma coluna de data frame
tendulkar['4s'] = pd.to_numeric(tendulkar['4s'])
tendulkar
tendulkar['4s'].apply(lambda x:4*x)

# Função lambda para converter Celsius em Fahrenheit
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, Celsius))
print(Fahrenheit)

## Funções
def produto(x, y):
    valor = x*y
    return(valor)

produto(8,7)