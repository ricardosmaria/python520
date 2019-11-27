# #!/usr/bin/python3

# #
# # Exercicio Funcoes
# #

# # criar uma funcao de soma que retorna a soma de 2 valores
# # criar uma funcao de subtracao que retorna a subtracao de 2 valores
# # criar uma funcao de multiplicacao que retorna a multiplicacao de 2 valores
# # criar uma funcao que gera raiz quadradade um numero x

# def soma(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mult(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     if n2 == 0:
#         raise ZeroDivisionError('nao tem como cara')
#     return n1 / n2

# def raizQuadr(n1):
#     if n1 < 0:
#        #rase ValueError('nao tem como fazer isso com esse numero')
       
#        n1 **= 0.5
#     else:
#         return n1 ** 0,5
# n1 = input('digite o primeiro num: ')
# n2 = input('digite o segundo num: ')
# resultado = soma(int(n1),int(n2)
# print(resultado)


#### corrigido pelo instrutor

#!/usr/bin/python3

#######
## Exercício Funções
#######

# Criar um função de soma que retorna a soma de 2 valores
# Criar um função de subtração que retorna a subtração de 2 valores
# Criar um função de multiplicação que retorna a multiplicação de 2 valores
# Criar um função de Divisão que retorna a Divisão de 2 valores
# Criar uma função que gera raiz quadrada de um número x

#!/usr/bin/python3

#######
## Exercício Funções
#######

# Criar um função de soma que retorna a soma de 2 valores
# Criar um função de subtração que retorna a subtração de 2 valores
# Criar um função de multiplicação que retorna a multiplicação de 2 valores
# Criar um função de Divisão que retorna a Divisão de 2 valores
# Criar uma função que gera raiz quadrada de um número x


#!/usr/bin/python3

#######
## Exercício Funções
#######

# Criar um função de soma que retorna a soma de 2 valores
# Criar um função de subtração que retorna a subtração de 2 valores
# Criar um função de multiplicação que retorna a multiplicação de 2 valores
# Criar um função de Divisão que retorna a Divisão de 2 valores
# Criar uma função que gera raiz quadrada de um número x


def soma(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Não tem como cara')
    else:
        return n1 / n2

def raizQuadrada(n1):
    if n1 < 0:
        #raise ValueError('Não tem como fazer isso com esse número')
        n1 **= 0.5
        return complex(n1)
    else:
        return n1 ** 0.5

n1 = input('Digite o primeiro numero: ')
n2 = input('Digite o segundo numero: ')
resultado = soma(int(n1),int(n2))
print(resultado)










