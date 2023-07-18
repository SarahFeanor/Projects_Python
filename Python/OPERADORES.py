''' 
    AUTHOR: SARAH F. REZENDE
    DATA: 10/07/2023
    AULA3: OPERADORES ARITIMÉTICOS E BOOLEANOS                  
'''

# Operações Matemmáticas (Aritiméticas)

'''
    soma: +
    subtração: -
    Multiplicação: *
    Divisão: /
    Divisão inteira (descarta a parte decimal): //
    Resto de divisão: %
    Potência (ao cubo, elevado): **
'''

num1 = 10
num2 = 20

print(num1 + num2)   #  30
print(num1 - num2)   # -10
print(num1 * num2)   #  200
print(num1 / num2)   #  0.5
print(num1 // num2)  #  0
print(20 % 3)        #  2
print(2 ** 3)        #  8

# Operações Booleanas

'''
    >   Maior
    <   Menor
    ==  Igual
    !=  Diferente
    >=  Maior ou Igual
    
'''

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.77
altura3 = altura2

print(idade1 > idade2)          # False
print(idade1 < idade2)          # True
print('Python' == 'python')     # False
print('Banana' != 'abacaxi')    # True
print(altura1 >= altura2)       # False
print(altura2 > altura3)        # False