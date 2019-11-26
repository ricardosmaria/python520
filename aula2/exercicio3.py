#!/usr/bin/python3

#
# exercicio de excessoes
#
# criar uma tela de cadastro de usuario em uma lista 
# essa tela nao pode aceitar figuras publicas que geram polemica
# ex = Bolsonaro, Lula, Adolf Hitler, Frota
# Esse loop é infinito, onde so acaba quando colocado uma figura 
# publica

# #arrays de nomes de figura publica
# bolsonaro = ['bolsonaro', 'bozo', 'bolsonario',
#             'borsalino','bonoliro', 'facista']
# lula = ['lula','mula','9 dedos','nove dedos',
#         'ladrao','luladrao']
# hitler = ['adolf hitler','hitler','fuhr','bigodin',
#             'nazista','argentino' ]
# tiririca = ['tiririca','palhaco','florentina']

# #atribuiindo todas as figuras publicas para uma lista
# figuras_publicas = [bolsonaro, lula, hitler, tiririca]

# #requisicao pelo nome
# lista_nomes []
# try 
# while True:
# #requisicao pelo nome
#     nome = input('Digite um nome: ')

# #para cada figura publica vou valçidar o nome digitado

#         for figura in figuras_publicas:
#             for apelido in figura_lista:
#                 if nome in apelido:
#                 cad_figura_publica = True 
#             break
#         else:
#             cad_figura_publica = False

# #criando logica para cadastro
# if cad_figuras_publica:
#     print('lancando erro cadastro de figuras')
# elif nome == 'visualizar':
#     for nome_cdastrado iin lista_nomes:
#         print(nome_cadastrado, end= '.')
# else:
#     print('cadastro realizado')
#     lista de nomes.append(nome)

# #visualizar nomes
# print(lista_nomes)
# except Exception:
#     print('você cadastrou uma figura publica ')
   

##################
####CORRETO3######
##################

#!/usr/bin/python3

#######
## Exercicio de excessões
#######

# Criar uma tela de cadastro de usuário em uma lista
# Essa tela não pode aceitar figuras públicas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Tiririca
# Esse Loop é infinito, onde só acaba quando colocado uma figura
# pública

# Arrays de nomes de figura publica
bolsonaro = [
    'bolsonaro',
    'bozo',
    'bolsanario',
    'borsalino',
    'bonoliro',
    'facista'
    ]
lula = [
    'lula',
    'mula',
    '9 dedos',
    'nove dedos',
    'ladrão',
    'luladrão'
    ]
hitler = [
    'adolf hitler',
    'hitler',
    'fuhr',
    'bigodin',
    'nazista',
    'argentino'
]
tiririca = [
    'tiririca',
    'palhaço',
    'tiririca',
    'florentina'
]

#Atribuindo todas as figuras públicas para uma lista
figuras_publicas = [bolsonaro, lula, hitler, tiririca]

for figura in figuras_publicas:
    with open('politicos.txt','w')
#print(figuras_publicas)


#definindo lista de nomes
lista_nomes = []

# try:
#     while True:
#         #requisição pelo nome
#         nome = input('Digite um nome: ').lower().strip()

#         # para cada figura publica, vou validar o nome digitado
#         for apelido in figuras_publicas:
#             if nome in apelido:
#                 cad_figura_publica = True
#                 break
#             else:
#                 cad_figura_publica = False
#         #Criando lógica para cadastro
#         if cad_figura_publica:
#             raise ValueError('Você tentou inserir uma figura pública')
#             #print('Lançando erro Cadastro de figuras')
#         elif nome in lista_nomes:
#             print('nome Já existe')
#         elif nome == 'visualizar':
#             for nome_cadastrado in lista_nomes:
#                 print(nome_cadastrado,end=', ')
#             print('\n')
#         else:
#             print('\n'*100)
#             print('Cadastro Realizado')
#             lista_nomes.append(nome)

# except Exception:
#     print('Você tentou cadastrar uma figura pública')
#     print(lista_nomes)