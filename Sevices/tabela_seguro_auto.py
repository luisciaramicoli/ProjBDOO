import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS seguro_auto (
            seguro_auto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa VARCHAR(10),
            modelo VARCHAR(255),
            ano INTEGER(5),
            endereco_id INTEGER
        );
    '''
)

cursor.close()
print("Tabela 'seguro_auto' criada com sucesso no banco de dados Seguro.db!")