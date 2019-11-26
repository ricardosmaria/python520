#!/usr/bin/python3

#
# tratando excessoes
#
# print('Soma de dois valortes')
# numero1 = input('Digite um numero a ser somado: ') #excessao
# numero2 = input('Digite um numero a ser somado: ') #excessao
# print(numero1 + numero2)

# print('Soma de dois valortes')
# numero1 = int(input('Digite um numero a ser somado: '))
# numero2 = int(input('Digite um numero a ser somado: '))
# print(numero1 + numero2)

# try: #tente
#     print('Soma de dois valortes')
#     numero1 = int(input('Digite um numero a ser somado: '))
#     numero2 = int(input('Digite um numero a ser somado: '))
#     print(numero1 + numero2)
# except ValueError: #excessao
#     print('Insira somente numeros')

# try: #tente
#     print('Divisao de dois valortes')
#     numero1 = int(input('Digite um numero a ser dividido: '))
#     numero2 = int(input('Digite um numero a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError: #excessao
#     print('Insira somente numeros')
# except ZeroDivisionError:
#     numero2 = 0.1
#     print(numero1/numero2)
# except Exception as e:
#     print('Erro na execussao do programa',e)

# try: #tente
#     print('Divisao de dois valortes')
#     numero1 = int(input('Digite um numero a ser dividido: '))
#     numero2 = int(input('Digite um numero a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError: #excessao
#     print('Insira somente numeros')
# except ZeroDivisionError as e:
#     #numero2 = 0.1
#     print('Nao foi possivel fazer a divisao', e)
# except Exception as e:
#     print('Erro na execussao do programa',e)
# finally:
#     print('Saindo do Script')

#nulo = None


#
#lancando excessoes 
#

#try:
#    opcao  = int(input('Nao digite 5: '))
#        if opcao == 5:
#        raise ValueError('Eu falei para voce nao digitar 5')
#except ValueError as e:
#     print('Deu erro: ', e)
