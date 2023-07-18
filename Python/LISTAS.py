''' 
    AUTOR: SARAH F. REZENDE
    DATA: 17/07/2023
    AULA3: LISTAS   
    
************************************************
LISTAS >>>> Em Python, uma lista é uma estrutura de 
dados que permite armazenar múltiplos  elementos em 
uma  única  variável.  É uma  das  estruturas  mais 
versáteis  e  amplamente  utilizadas  na  linguagem.

Uma lista é definida utilizando colchetes [] 
e os elementos são separados por vírgulas. 

    lista = []
    lista = list()
    
***********************************************
'''

# antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com listas

notas = [7.9, 9.7, 8.2]

# criando listas

lista = []
lista = list()
lista = [26, "sarah", 3.14159, False]
lista_de_listas = [10, [1,2,3]]

# indexação e Slices (fatiamento)

lista = [26, "sarah", 3.14159, False]
#         0,    1   ,    2   ,   3
#        -4,   -3   ,   -2   ,  -1

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# slices

lista = [10, 50, 30, 40, 25, 60, 5]
#         0,  1,  2,  3,  4,  5, 6

print(lista[0:3])    # 10, 50, 30
print(lista[3:6])    # 40, 25, 60
print(lista[:3])     # 10, 50, 30
print(lista[3:])     # 40, 25, 60, 5
print(lista[2:6:2])  # 30,  25

# Interção com FOR
# Utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# Utilizando os ìndices

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
   print (lista[2])
 # print (i)
    


