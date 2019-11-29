#!/usr/bin/env python3

import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
except Exception as e:
    print (e)
    exit()
cur = con.cursor()
try:
    cur.execute("INSERT into scripts(nome,conteudo) values ('Josivaldo','programador')")
    con.commit()
except Exception as e:
    con.rollback()
    print(e)
finally:
    cur.close()
    con.close()