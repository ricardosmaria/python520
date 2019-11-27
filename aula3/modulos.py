# #!/usr/bin/python3

# import modulos.calculadora as calc

# somar = calc.somar(1,2)
# print(somar)

# print(calc.subtrair(9,1))

# from modulos.calculadora import * #soamr, subtrair
# somar = somar(1,2)
# print(somar)

# print(subtrair(9,1))
# print(multiplicar(6,2))
# print(dividir(20,3))


import random       # modulo que trata de operacoes de aleatoriedade
import os           #possibilita usar funconalidades do so
import sys          #acessar variaveisde sistema e alguns paramet. especif.
import datetime     #cuida de data e hora
import json         #codiifica e/ou decodificar um arq. no format. json
import csv          #trabalha com planilhas

#print(os.listdir('/home/developer'))
# print(os.rename('nomeErrado.txt','nomeCerto.txt'))
#os.system('ls')
#os.system('systemctl restart apache2')
#os.system('systemctl start apache2')
#modulo sys
#print(sys.plataform)
#print(sys.builtin_module_names)
# print(sys.argv)
# sys.exit()
# print('hello')

# print(datetime.datetime.now())
# print(datetime.timedelta(7))
# print(datetime.time(14,0,0))
#####print(datetime.time(14,0,0)+ datetime.time(2,0,0)) ## deu erro
#print(datetime.date(2019,5,4))

# #### acesso pratico
# acesso = datetime.datetime(2019,1,22,00,00,00)
# atual = datetime.datetime(2019,1,22,1,1,00)

# print(acesso)
# print(atual)
# print(atual - acesso)

# if (atual - acesso).total.seconds() > 3600:
#     print('seu token expirou')
# else:
#     print('acesso liberado')

#print(random.randint(1,90))


### joson

print(json.dumps({
    "nome":"Daniel",
    "sobrenome":"silva"
}))

print(json.loads('{"nome":"Daniel","sobrenome":"silva"}',))