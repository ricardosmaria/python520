############
#26/11/2019#
############

########################
#operadores aritméticos#
########################

!/usr/bin/python3

#variaveis por nomenclatura podem ter no 
#maximo 16 caracteres
num1 = 6
num2 = 8

adicao = num1 + num2 
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
result_div_int = num1 // num2 #resultado da operacao
resto_div_int = num1 % num2   # resto da operacao

#operadores de forma abreviada
#pega o valor atual do numero  e realiza calculo
#atribuindo o resultado a variavel

numero = 1
numero += 3 # 1+3 numero = numero +3
numero -= 3 # 4-3 numero = numero -3
numero *= 4 # 1*4 numero = nuumero *4
numero /= 2 # 4/2 numero = numero /2
numero //= 2 # 2//2=1 numero = numero //2
numero %= 2 # 2%2 =0 numero = numero%2

##
## Operadores relacionais
##

#operadores relacionais servem para comparação entre fatores
#retorna valores booleanos

numero1 = 6
numero2 = 9
numero3 = float(6)

print(numero1 == nuumero2)   #false
print(numero1 /= numero2)    #diferenciacao true
print(numero1 < numero2)     #menor que true
print(numero1 <= numero2)    #menor igual true
print(numero1 > numero2)     #maior que false
print(numero1 >= numero2)    #maior igual false

print(numero1 is numero3)    #compara se estão alocados no 
                             #mesmo bloco de memoria true



lista1 = ['item1' , 'item2' , 'item3']
print('item1' in lista)      #compara a existencia de valores em lista true



