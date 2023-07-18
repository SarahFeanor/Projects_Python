''' 
    AUTOR: SARAH F. REZENDE
    DATA: 17/07/2023
    AULA3: LAÇOS DE REPETIÇÃO (while)   
    
************************************************
WHILE (enquanto) >>>> 
a  estrutura de   repetição  WHILE é  um  laço condicional 
utilizado quando  é  necessário   executar  um determinado 
trecho  de  código  várias   vezes, sem  saber previamente 
quantas iterações serão necessárias.  O  while  continuará 
executando o código  enquanto   uma  determinada  condição 
não for satisfeita.  Dessa  forma,  o  while é  ideal para 
situações em que a quantidade de repetições é desconhecida.
    
************************************************
'''
# Exemplo 01: Jogo da Advinhação

print('*******JOGO DA ADVINHAÇÃO*******')

numero_sorteado = 15

numero_escolido = int(input ('Informe um numero entre 1 e 20:  '))

while numero_sorteado != numero_escolido:
    print('Você errou, tente novamente...')
    
    numero_escolido = int(input ('Informe um numero entre 1 e 20: '))
    
print("Parabéns, você acertou!")

# Exemplo 02: Estrutura com contador

print('*******CONTADOR*******')

contador = 0

while contador < 5:
    print(contador)
    
    contador = contador + 1