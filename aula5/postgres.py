# #!/usr/bin/env python3

# import psycopg2
# import MySQLdb

# from orm import Banco

# try:
#     con_psql = psycopg2.con_psqlnect('host=localhost dbname=projeto user=admin password=4linux')
#     cur = con_psql.cursor()

#     banco_psql = Banco(cur,con_psql)

#     # conexao com mysql
#     con_mysql = MySQLdb.connect('host=localhost,db=projeto,user=admin,passwd=4linux)
# except Exception as e:
#     print(e)
#     exit()

# try:
#     #banco_psql.inserir('Daniel','Programador Python')

#     #print(banco_psql.seleciona_todos('scripts'))

#     #print(banco_psql.seleciona_primeiro('scripts'))

#     #banco_psql.delete('scripts','nome','Daniel')
#     #print(banco_psql.seleciona_todos('scripts'))
#     pass
# except Exception as e: 
#     con_psql.rollback()
#     con_psql.rollback()
#     print(e)




#!/usr/bin/env python3

import psycopg2
import MySQLdb

from orm import Banco

try:
    #conexao postgres
    con_psql = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con_psql.cursor()

    banco_psql = Banco(con_psql,cur)

    #conexao com mysql
    con_mysql = MySQLdb.connect(host='hostname',db='projeto',
                                user='admin',passwd='4linux')
except Exception as e:
    print(e)
    exit()

try:
    # print(banco_psql.seleciona_todos('s'))
    # print(banco_psql.seleciona_primeiro('s'))
    #banco_psql.delete('s','nome','Daniel')
    #print(banco_psql.seleciona_todos('s'))
except Exception as e:
    con_psql.rollback()
    con_mysql.rollback()
    print(e)

