import sqlite3
from Models.Endereco import Endereco

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaEndereco():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
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
        """)
        conexao.commit()
        print("Tabela 'enderecos' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'enderecos': {e}")
    finally:
        conexao.close()

def incluirEndereco(endereco):
    """
    Inclui um novo endereço e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO enderecos (
                cep, logradouro, numero, complemento, bairro, cidade, estado
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            endereco.get_cep(),
            endereco.get_logradouro(),
            endereco.get_numero(),
            endereco.get_complemento(),
            endereco.get_bairro(),
            endereco.get_cidade(),
            endereco.get_estado()
        ))
        conexao.commit()
        novo_id = cursor.lastrowid # Pega o ID do último item inserido
        print(f"Endereço inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Endereço: {e}")
        return None
    finally:
        conexao.close()

def consultarEnderecos():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM enderecos')
        rows = cursor.fetchall()
        
        dados_enderecos = []
        colunas = ["endereco_id", "cep", "logradouro", "numero", "complemento", "bairro", "cidade", "estado"]
        
        for row in rows:
            endereco_dict = dict(zip(colunas, row))
            dados_enderecos.append(endereco_dict)
        
        return dados_enderecos
    except sqlite3.Error as e:
        print(f"Erro ao consultar enderecos: {e}")
        return []
    finally:
        conexao.close()

def consultarEnderecoPorId(endereco_id):
    """
    Consulta e retorna os dados de um endereço específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM enderecos WHERE endereco_id = ?', (endereco_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["endereco_id", "cep", "logradouro", "numero", "complemento", "bairro", "cidade", "estado"]
            endereco_dict = dict(zip(colunas, row))
            return endereco_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar endereço por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirEndereco(endereco_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM enderecos WHERE endereco_id = ?", (endereco_id,))
        conexao.commit()
        print(f"Endereço com ID {endereco_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Endereço: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarEndereco(endereco):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE enderecos 
            SET 
                cep = ?,
                logradouro = ?,
                numero = ?,
                complemento = ?,
                bairro = ?,
                cidade = ?,
                estado = ?
            WHERE endereco_id = ?
        ''', (
            endereco.get_cep(),
            endereco.get_logradouro(),
            endereco.get_numero(),
            endereco.get_complemento(),
            endereco.get_bairro(),
            endereco.get_cidade(),
            endereco.get_estado(),
            endereco.get_endereco_id() # Este é o 'WHERE'
        ))
        conexao.commit()
        print(f"Endereço com ID {endereco.get_endereco_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Endereço: {e}")
    finally:
        if conexao:
            conexao.close()

# Bloco de inicialização
if __name__ == "__main__":
    criarTabelaEndereco()
    
    print("\n--- Consultando Endereços ---")
    enderecos = consultarEnderecos()
    for e in enderecos:
        print(e)