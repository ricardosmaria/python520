#!/usr/bin/python3

#
# manipulando arquivos com Python
#


# abrir um arquivo para modificacao
# metodo nao recomendado

# ponteiro = open('nomedarquivo.txt','r+') #abre um ponteiro para escrita de arquivos
#                                         #, o modo utilizado é o read plus (r+)( que serve para)
#                                         # leitura e escrita. possuimos varios modos de acesso,
#                                         #  por exemplo:
#                                         # w = sobrescrito 
#                                         # r = somente leitura
#                                         # + = abre um arqu. para atualizacao (acrescenta e modifica)
#                                         # a = complemento
#                                         # x =  criacao
#                                         # este metodo ñ e recomendado pq o ponteiro sempre necessita 
#                                         # ser encerrado com close, isso foi substituido com a adicao
#                                         # do comando with (mostraremos em breve)
# ponteiro.write('Olá Mundo\n\n')
# ponteiro.close()

### metodo usual ###

with open('nomedoarquivo2.txt','a') as arquivo:
    arquivo.write('ola mundo\n')
    arquivo.writelines(['banana\n','maca\n'])
#arquivo em modo de leitura
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.read()

print(letras)