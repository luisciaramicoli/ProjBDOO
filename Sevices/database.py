#Sevices/database.py
import sqlite3

server = ''
username = ''
password = ''
database = 'Empresa.db'
conexao = sqlite3.connect(database)
print("Banco de dados Empresa criado com sucesso!")