#!/usr/bin/env python3

class Banco():
    
    def __init__(self,cursor, conexao):
        try:
            self.conexao = conexao
            self.cursor = cursor
        except Exception as e:
            raise Exception(e)
    

    def __del__(self):
        self.cursor.close() 
        self.conexao.close()

    #criando crud - create, read, update, delete 
    def inserir(self, nome, conteudo):
        self.cursor.execute(f"INSERT INTO scripts(nome,conteudo) VALUES ('{nome}','{conteudo}')")
        self.conexao.commit()
        print('Inserido com sucesso!')

    def atualizar(self, tabela, valor, coluna_old, valor_old):
        self.cursor.execute(f"UPDATE {tabela} SET {coluna} = {valor} WHERE {coluna_old} = {valor_old}") 
        self.conexao.commit()
        print('Atualizado com sucesso!')

    def delete(self, tabela, coluna, valor):
        self.cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = {valor}")   
        self.conexao.commit()
        print('Deletado com sucesso!')

    def seleciona_todos(self):
        return self.cursor.fetchall()

    def seleciona_primeiro(self):
        return self.cursor.fetchone()
