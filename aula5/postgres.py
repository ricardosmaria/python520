#!/usr/bin/env python3

import psycopg2

from orm import Banco

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()

    banco = Banco(cur,con)
except Exception as e:
    print(e)
    exit()

try:
    banco.inserir('Daniel','Programador Python')
except Exception as e:
    cur.rollback()
    print(e)