import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS reembolso (
            reembolso_id INTEGER PRIMARY KEY AUTOINCREMENT,
            seguro_auto VARCHAR(255),
            planos_de_seguro VARCHAR(255),
            valor REAL
        );
    '''
)

cursor.close()
print("Tabela 'reembolso' criada com sucesso no banco de dados Seguro.db!")