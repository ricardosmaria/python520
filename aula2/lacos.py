#!/usr/bin/python3

##
#laço while
## este laço executa enquanto uma condicao for verdadeira

# i = 0
# while( i < 10): # enquanto i for menor q 10
#     print(i)    # mostra valor de i
#     i+= 1       # soma 1
#                 #repete

    # controle de um loop while

    # i = 0
    # while(true)
    #     print('Teoricamente um loop infinito')
    #     i += 1
    #     if i == 3
    #         break

    


# i = 0
# while(True):
#     i += 1
#     if i == 3:
#         break
#     if i == 5:
#         continue
#     print('Teoricamente um loop infinito',i)

# #continue retoma do começo a execussão de um loop

# i = 100                 # interador regressivo
# while i > 0:
#     i -= 1
#     if i % 2 == 1:
#         continue
#     print(i)


#
# laço for
#
# percorre itens em determinado alcance de valores


# lista = []
# for i in range(1,100,1):   # começa do 1 vai  até o 100 de 2 em 2
#     lista.append(i)
#     print(lista)
# #percorre uma lista
# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[31m{i}\033[0m', 'par') #atrubui cor vermelha
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m', 'impar')   #atrubui cor verde

#percorrer um diconario

dicionario = {
    'nome':'Daniel',
    'sobrenome':'Silva'}

# for i in dicionario:
#     print(dicionario[i])

# for chave,valor in dicionario.items():
#     print(chave)
#     print(valor)


# enumerando itens de uma lista

#lista = ['item','item2','item3','item5','item6','item7']
#print(list(enumerate(lista)))
#opcao1
# for i in enumerate(lista):
#     print(i)
#opcao2
# for indice, valor in enumerate(lista):
#     print(indice)

#list compreension (compreencao de listas)

# lista = [x for x in range(0,1000,5)]
# print(lista)

