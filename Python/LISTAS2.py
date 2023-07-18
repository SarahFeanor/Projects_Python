''' 
    AUTOR: SARAH F. REZENDE
    DATA: 17/07/2023
    AULA3: METODOS E FUNÇÕES DE LISTAS   
    
************************************************
    LISTAS >>>> 
Em   Python,   uma  lista  é   uma   estrutura   de 
dados que permite armazenar múltiplos  elementos em 
uma  única  variável.  É uma  das  estruturas  mais 
versáteis  e  amplamente  utilizadas  na  linguagem.

    Uma lista é definida utilizando colchetes [] 
e os elementos são separados por vírgulas. 

    APPEND >>>>
Em Python, o método append() é um  método  embutido em 
listas que permite adicionar um novo elemento ao final 
da lista  existente.  Ele  modifica  a  lista original, 
acrescentando o  elemento  fornecido como argumento ao 
final dela.

    INSERT >>>>
Em Python, o método insert() é um  método  embutido  em 
listas que permite  adicionar  um novo  elemento em uma 
posição específica  da lista.  Diferentemente do método 
append(), que  adiciona elementos ao  final da lista, o 
método insert() permite inserir um elemento em qualquer 
posição desejada.

    EXTEND >>>>
Em  Python, o  método extend() é um  método  embutido  
em listas que permite adicionar múltiplos elementos a 
uma  lista  existente.  Ele  é   usado para  estender 
(ou concatenar)  uma  lista com os elementos de outra 
lista ou de qualquer outra sequência iterável. 

    POP >>>
Para remover elementos, que especificamos, se não especificar 
ele deleta o ultimo elemento. 

    REMOVE >>>
Para remover elementos, que especificamos, não no index. 
Mas o elemento. 

    COUNT >>>
Quando vc quer contar quantas vezes um elemento apareceu na sua lista

    INDEX >>>
Ele te diz um determinado indice de um determinado elemento da lista.

    SORT >>>
Ele serve para vocês ordenar a lista. b

***********************************************
'''

# METODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append() insiro apenas no final

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert() insiro onde eu quiser

lista.insert(2, 10)

print('Depois do insert: ', lista)


# extend() juntar duas listas

lista2 = [1,2,3]

lista.extend(lista2)
print('Depois do extend: ', lista)

# >> REMOVENDO ITENS DA LISTA


# pop() remover elementos 

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após o pop: ', lista)

# remove() voce diz qual o elemento que quer remover

lista.remove(3)

print('Lista após o remove: ', lista)


# >>>> OUTRAS COISAS QUE PODEMOS FAZER COM A LISTA


# count() contador de elementos

print('Quantidade de 2 na lista: ', lista.count(2))

# index() ele te diz o indice de um elemento

print('Qual é o indice do elemento 12? ', lista.index(12))

# sort() Serve para ordenarmos a lista

lista.sort()

print(lista)

#sort() decrescente com "reverse = true"

lista.sort(reverse = True)

print(lista)


# >> FUNÇÕES PARA LISTAS 

# len() conta a quantidade de elementos na lista

print(len(lista))

# sum() soma todos os elementos dentro da lista

print(sum(lista))

# max() maior valor

print('Maior valor da lista', max(lista))

# min() menor valor

print('Menor valor da lista', min(lista))
