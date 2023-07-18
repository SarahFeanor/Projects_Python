''' 
    AUTOR: SARAH F. REZENDE
    DATA: 17/07/2023
    AULA3: LAÇOS DE REPETIÇÃO (For)   
    
************************************************
FOR >>>> 

Em Python, a palavra-chave  "for" é   utilizada   para 
criar um loop (laço)  de  repetição,  também conhecido 
como estrutura de repetição "for loop". Essa estrutura 
permite  executar  um  bloco  de  código  várias vezes, 
percorrendo uma sequência de elementos, como uma lista, 
uma string, um dicionário ou um range.

    for variavel in range(1, 12, 3):
        print(variavel)

***********************************************
RANGE() >>>>

    range(5) conta de 0 a 4
        # 0, 1, 2, 3, 4
         
    range(1,7) conta de 1 a 6
        # 1, 2, 3, 4 , 5, 6
        
    range(1, 12, 3) conta de 1 a 11 pulando de 3 em 3
        # 1, 4, 7, 10
    
************************************************
'''
# MEDIA DE NOTAS

soma = 0

for i in range(1, 4):
    nota = float (input(f'Informe a sua nota {i}: '))
    
    soma = soma + nota
    
    print(soma / 3)