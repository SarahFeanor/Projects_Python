import random

print('***** BEM VINDO AO JOGO DA ADIVINHAÇÃO *****')

print("Você terá três chances para adivinhar um número aleatório, entre 1 e 20")

num = random.randint(1,20)

for i in range(5):
    print('\nQual a sua escolha?')
    chute = int(input())
    if chute == num:
        print('\nParabéns, você acertou!')
        break
    elif chute > num:
        print('Numero baixo.')
if chute != num:
    print('\nO número secreto era o {}'.format(num))