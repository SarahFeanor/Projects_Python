''' 
    AUTOR: SARAH F. REZENDE
    DATA: 10/07/2023
    AULA3: FUNÇÕES
    
***********************************************

FUNÇÕES >>>>
Em Python, as funções são blocos de código reutilizáveis 
que podem ser definidos para executar uma determinada tarefa. 
Elas permitem agrupar um conjunto de instruções em um único 
bloco lógico, tornando o código mais organizado, legível e 
modular.

As funções são definidas usando a palavra-chave def, 
seguida pelo nome da função, parênteses contendo os parâmetros 
(argumentos) e um bloco de código indentado que especifica as ações 
a serem executadas pela função.

Funções que já usamos anteriormente:

    print()
    input()
    len()
    max()
    min()

************************************************
'''

# Criação de funções

# Função Inicial

def saudacao():
    print('Seja bem-vindo(a!)')
    print('Olá, é um prazer te conhecer!')

saudacao()

# Função com Parametros

def saudacao(nome, cidade):
    print(f'Seja bem-vindo(a!), {nome}')
    print(f'É um prazer ter você aqui em {cidade}!')

saudacao('Sarah', 'Belo Horizonte')


# Função com Parametros com default

def saudacao(nome, cidade = 'Belo Horizonte'):
    print(f'Seja bem-vindo(a!), {nome}')
    print(f'É um prazer ter você aqui em {cidade}!')

saudacao('Sarah')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2    

resultado = soma (5, 7)

print(' O resutado da soma é ', resultado)

# ***

def calculadora(num1, num2, operacao = "+"):
    if operacao == '+':
        return num1 + num2 
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora (10, 20, '-')

print(resultado)