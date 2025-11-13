import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS apolice (
            apolice_id INTEGER PRIMARY KEY AUTOINCREMENT,
            proposta_id INTEGER
        );
    '''
)

cursor.close()
print("Tabela 'apolice' criada com sucesso no banco de dados Seguro.db!")