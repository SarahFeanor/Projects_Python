''' 
    AUTHOR: SARAH F. REZENDE
    DATA: 10/07/2023
    AULA2: CONVERSÃO DE TIPOS                  
'''

# CONVERSÃO DE TIPOS

idade = "28"
num1  = "10"
num2  = "20"

# O resultado será uma concatenação do 10 e 20 gerando o valor de 1020
print(num1 + num2) 

print(idade, type(idade)) #str

# Convertendo os tipos manualmente

idade_inteira = int(idade) # Conversão manual

print(idade_inteira, type(idade_inteira)) 

# Quando usamos o input, o texto digitado será sempre str
# Convertendo o input para qualquer outro tipo

altura = int (input('Qual a sua altura? '))
print(altura, type(altura))