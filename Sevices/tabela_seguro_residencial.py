import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS seguro_residencial (
            seguro_residencial_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(255),
            endereco_id INTEGER
        );
    '''
)

cursor.close()
print("Tabela 'seguro_residencial' criada com sucesso no banco de dados Seguro.db!")
