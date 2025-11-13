import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS planos_seguro (
            nome_plano_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_plano VARCHAR(255),
            valor_total REAL,
            valor_parcela REAL,
            detalhes VARCHAR(255)
        );
    '''
)

cursor.close()
print("Tabela 'planos_seguro' criada com sucesso no banco de dados Seguro.db!")