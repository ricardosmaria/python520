#!/usr/bin/python3

#
# parametros no python
#

''' Paramentros Python - titulo

Nesta aula nos analisamos como criar e documentar funcoes 

'''

def retorna_pessoa(nome,idade=99):
    print(f'Nome: {nome}\nidade: {idade}')

# retorna_pessoa(nome='Daniel', idade=19)

# especificar tipo de parametro e retorno

#anotaçoes de funcao

#def retorna_valor_int(inteiro : int, booleano : bool)-> int:
    ''' Funçao com anotação de tipo

    Se refere a funcao que possui tipos especificos e 
    mostram na sua sintaxe de construcao o que é necessário
    SEMPRE TEM QUE PULAR UMA LINHA'''

#     inteiro = int(inteiro)
#     return inteiro

# print(retorna_valor_int('i',False)

### args e kwargs
#print('olá','mundo',',','prazer','sou', 'daniel')

### criando uma funcao que recebe multiplos valores

# def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
#     print(parametros_estaticos,'paramentro estatico')
#     print(argumento_variavel)
#     # for argumento in argumento_variavel:
#     #     print(argumento)

# funcao_multi_valores('valor estatico obrigatorio',
#                     'daniel', 'andressa','joao','ana',
#                     'paula','lucas','leonardo','pedro')

## argumentos com palavra chave - kwargs

# def parametros_chave_valor(**dados):
#     if dados['nome']  == 'Daniel':
#         print('Acesso Negado')
#     else:
#         print('Permitido')
#     #print(dados)

# # execucao metodo1
# #print('Metodo1')
# parametros_chave_valor(nome = 'Daniel', sobrenome='Silva', 
#                         idade = 19, sexo='masculino')

# # execucao metodo2
# #print('Metodo2')
dados_requisicao = {'nome':'Daniel','Sobrenome':'Silva',
                    'profissao':'operador de empilhadeira'}

### decorador de funcao 

def mudaCor(retorno_funcao):
    def modificaAzul(retorno_funcao):
        return f'\033[94m{retorno_funcao}\033[0m'
    return modificaAzul     

#mudaCor(input('texto'))

@mudaCor
def log(texto):
    return texto

print(log('oi'))