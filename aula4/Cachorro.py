#!/usr/bin/env python3

class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
    #    print('Estou vivo!!')
        pass

    def viver(self):
        print('Estou vivo')

class Cachorro(Animal):
    '''Abstracao de um cachorro

    Cria um cachorro, baseado nos conceitos definidos em sala'''

    _DNA = 'Cachorro'

    def __init__(self, nome, idade, cor, raca='Vira-lata', porte='Médio'):
        
        #parametros Obrigatorios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor 
        self.raca = raca
        self.porte = porte
        
        # Atributos padrao para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.focinho = True # valores unicos como true e false
        self.lingua = True  # 
        self.olhos = 2
        self.rabo = True    # 

        print(f'Cachorro {nome}, Construido com sucesso!')


    # o que o cachorro faz metodos

    def latir(self):
        if self.lingua:
            print(f'{self.nome} Au Au Au...')

    def comer(self):
            print('Comendo...')

    def cheirar(self):
        if self.focinho:
            print('Cheirando...')

    def cagar(self):
        print('Cagando...')

    def dormir(self):
        print('Dormindo...')

    def __del__(self):
        print(f'Descanse em paz {self.nome}')

    def __str__(self):
        return 'Controi um cachorro'




#rex = Animal()
# rex = Cachorro()
# rex.viver()
# rex.latir()


