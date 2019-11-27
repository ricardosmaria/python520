# #!/usr/bin/python3

# #
# # funcoes
# #

# # blocos de codigo pre-definidos para execução

# # def mostrar_hello_world():
# #     print('hello world')

# #     mostrar_hello_world()

# #criando uma estrutura de funcoes
# def menu():
#     print('Escolha a opção: ')
#     print('1 - registrar produto')
#     print('2 - consultar saldo do caixa')
#     print('3 - abrir caixa de mercado')
#     print('4 - fechamento')
#     return input('digite a opcao desejada: ')

# def registrar_produto():
#     print('produto registrado')

# def consultar_saldo():
#     print('saldo é R$ x')

# def abrir_caixa():
#     print('abrindo')

# def fechamento():
#     print('fechando')

# # opcao menu()
# # print(opcao)
 
#  #estrutura principal
# while True:
#     print("caixa registradora")
#     opcao = menu()
#     if opcao == '1':
#         registrar_produto()
#     elif opcao == '2':
#         consultar_saldo()
#     elif opcao == '3':
#         abrir_caixa()
#     elif opcao == '4':
#         fechamento()
#     else:
#         break
#     input()


#funcoes anonimas
# var = lambda x : x*2
# print(var(2))

# numeros = list(range(1,100))
# print(numeros)

# var = lambda x : x*2
# print(var(2))

# numeros = list(range(1,100))
# def dobro(x):
#     return x * 2

# print(list(map(dobro,numeros)))

# var = lambda x : x*2
# print(var(2))

# numeros = list(range(1,100))
# # def dobro(x):
# #     return x * 2

# print(list(map(lambda x : 3 * x,numeros)))



numeros = list(range(1,100))
# def dobro(x):
#     return x * 2

print(list(map(lambda x : 3 + x,numeros)))