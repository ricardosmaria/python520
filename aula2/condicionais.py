
#!/usr/bin/python3

#carro = input('digite qual o caminho a ser seguido: ')

#a = 'engarrafado'
#b = 'livre'

# se a == 'engarrafado':
#     print('melhor ir pela b')
# else:
#     print('indo pelo caminho a') exemplo fraco

##
## Estrutura confdicional simples
##

# nome = input('digite seu nome: ')
# sobrenome = input('digite seu sobrenome: ').strip().title()

 #if nome == 'Daniel':
 #    print('Olá professor')
 #print('Seja bem vindo')

##
## EStrutura condicional composta
##

# if nome == 'daniel':
#     print(f'bemvindo professor{nome}')
# else:
#     print(f'bemvindo aluno {nome}')
# print('voce pode utilizar a plataforma')

##
## exercicio condicional composto
##

# criar uma variavel idade onde recebe uma
# idade via linha de comando, validar se essa
# pessoa pode beber ou nao, caso possa, atribuir
# ao valor de uma variável embriagado o valor true, senao false


# idade = int(input('digite sua idade: '))
    
#     if idade >= '18':
#      embriagado = True
#  else:
#      embriagado = False
# print(embriagado)

##
## comparando condicoes
##

# if nome == 'Daniel' and sobrenome == 'Silva':
#      print(f'bemvindo professor{nome}')
# else:
#      print(f'bemvindo aluno {nome}')
# print('voce pode utilizar a plataforma')

## criar uma validacao para que se a pessoa tiver carteira de
## motorista, ela possa dirigir. porem
## criar condicional para que a pessoa estiver embriagada,
## mostrar uma mensagem que ela nao pode dirigir

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     # If's validam se variável tem conteúdo
#     habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
#     if habilitacao == 'y':
#         habilitacao = True
#         bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
#         if bebeu:
#             embriagado = True
#             print('você nao pode dirigir')
#         else:
#             embriagado = False
#             print('Você pode dirigir')
#     else:
#         habilitacao = False
#         print('você esta proibido de dirigir')
# else:
#     print('Você está proibido de dirigir')


#
# coondicionais aninhadas
#

# nome = input('digite seu nome: ').strip().title()

# if nome == 'Daniel': 
#     print(f'Seu nome é muito bonito, {nome}')
# elif nome == 'Juliana':
#     print(f'Seu nome é muito legal {nome}')
# elif nome == 'Jorge':
#     print(f"Seu nome é muito feio, {nome} ")
# else:
#     print('Seu nome é normal, {nome} ')  


#criar uma validacao com elif para que se a idade for menor
#que 0 anos, a pessoa seja invalida

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     # If's validam se variável tem conteúdo
#     habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
#     if habilitacao == 'y':
#         habilitacao = True
#         bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
#         if bebeu:
#             embriagado = True
#             print('você nao pode dirigir')
#         else:
#             embriagado = False
#             print('Você pode dirigir')
#     else:
#         habilitacao = False
#         print('você esta proibido de dirigir')
# else:
#     print('Você está proibido de dirigir')