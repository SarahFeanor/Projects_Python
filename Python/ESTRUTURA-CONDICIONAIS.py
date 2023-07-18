''' 
    AUTOR: SARAH F. REZENDE
    DATA: 10/07/2023
    AULA3: ESTRUTURAS CONDICIONAIS   
    
************************************************

    As estruturas condicionais, determinam 
    se um determinado trexo de código será 
    executado ou não com base em uma condição.
    
************************************************
    
    Imagine que você queira imprimir "Aprovado(a)", 
    caso o estaudante tenha uma média superior ou 
    igual a 7, e "Reprovado", caso a média seja 
    inferior a 7.
    
'''

# ESTRUTURA PARA DESCOBRIR A MAIOR OU MENOR IDADE

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print('Você é maior de idade.')
else: 
    print('Você é menor de idade.')
    
    
# ESTRUTRA PARA DESCOBRIR SE ALGUEM FOI REPROVADO OU APROVADO

media = float(input('Informe sua média? '))

if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
    
    
# ESTRUTURA QUE JÁ CALCULA A MEDIA DA NOTA TOTAL E DA O RESULTADO
# USANDO "ELIF", E "AND".

nota = float(input('Qual é a sua nota?'))
presenca = float(input('Qual a frequencia nas aulas?'))

media = (nota / 2)

if media >= 7 and presenca >= 70:
    print('Sua media foi ', media, ", você está aprovado!")
elif media >= 5 and presenca >= 50:
    print('Sua media foi ', media, ", você está de Recuperação!")
else:
    print('Sua media foi ', media, ", você está reprovado!")