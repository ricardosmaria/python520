#!/usr/bin/python3

#
# escopo de variaveis e globais 
#


#variavel no escopo global
variavel = 3

def muda_variavel():
    #variavel = 2 # variavel no escopo local
    global variavel
    variavel = 2 #escopo global
    print(variavel)

muda_variavel()

print(variavel)