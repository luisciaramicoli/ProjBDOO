import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS enderecos (
            endereco_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cep VARCHAR(8),
            logradouro VARCHAR(255),
            numero VARCHAR(255),
            complemento VARCHAR(255),
            bairro VARCHAR(255),
            cidade VARCHAR(255),
            estado VARCHAR(255)
        );
    '''
)

cursor.close()
print("Tabela 'enderecos' criada com sucesso no banco de dados Seguro.db!")