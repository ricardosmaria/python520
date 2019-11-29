#!/usr/bin/env python3

import psycopg2
import MySQLdb

from orm import Banco

try:
    #conexao postgres
    con_psql = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con_psql.cursor()

    banco_psql = Banco(cur_psql, con_psql)

    #conexao com mysql
    con_mysql = MySQLdb.connect(host='127.0.0.1',db='scripts',
                                user='developer',passwd='4linux')


    cur_mysql = con_mysql.cursor()
    banco_psql = Banco(cur_mysql, con_mysql)

except Exception as e:
    print(e)
    exit()

try:
    # print(banco_psql.seleciona_todos('s'))
    # print(banco_psql.seleciona_primeiro('s'))
    #banco_psql.delete('s','nome','Daniel')
    #print(banco_psql.seleciona_todos('s'))

    banco_mysql.inserir('Daniel','Programador')
    print(banco_mysql.seleciona_todos('scipts'))
    #pass
except Exception as e:
    con_psql.rollback()
    con_mysql.rollback()
    print(e)