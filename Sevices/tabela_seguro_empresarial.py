import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS seguro_empresarial (
            seguro_empresarial_id INTEGER PRIMARY KEY AUTOINCREMENT,
            atividade VARCHAR(255),
            endereco_id INTEGER
        );
    '''
)

cursor.close()
print("Tabela 'seguro_empresarial' criada com sucesso no banco de dados Seguro.db!")