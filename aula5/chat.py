#!/usr/bin/python3

import time

def cadastrar(nome,mensagem):
    dados = {'nome':nome, 'mensagem':mensagem, 'hora':time.strftime('%d/%m/%Y/%H:%M:%S')}
    
    db.chat.insert(dados) # modulo de insercao do mongodb

def lerMensagem():
    ultimo = [x for x in db.chat.find().sort('_id', DESCENDING)]
    while True:
        atual = [x for x in db.chat.find().sort('_id', DESCENDING)]
        if atual != ultimo:
            ultimo = atual
            print(f"[{atual[0]['hora']} {atual[0]['nome']} {atual[0]['mensagem']}")
        time.sleep(1)
