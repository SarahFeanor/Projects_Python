''' 
    AUTOR: SARAH F. REZENDE
    DATA: 17/07/2023
    AULA3: DICIONÁRIOS
    
***********************************************

DICIONARIOS >>>>

Em Python, um  dicionário  é uma estrutura de dados 
que permite armazenar  pares  de chave-valor. É uma 
coleção mutável, não ordenada e indexada, onde cada 
elemento é acessado por meio de uma chave única.

Os dicionários são definidos utilizando chaves {} e os 
pares de chave-valor são separados por dois pontos :. 
Cada par chave-valor é representado como chave: valor. 

************************************************
'''

# Criando um dicionario

dicionario = {}
dicionario = dict()

dicionario = { 'nome ': 'Sarah', 'idade ': 28, 'altura ': 1.60 }

print(dicionario)
print(dicionario['idade '])

# Adicionando elemento em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['idade '] = 29

print(dicionario)


# Interando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave] )
    
# testando a existência de uma chave

print('peso ' in dicionario)
print('altura ' in dicionario)