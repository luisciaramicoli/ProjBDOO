import sqlite3
from Models.Corretor import Corretor

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaCorretor():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS corretores (
                id_corretor INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_corretor VARCHAR(255),
                cnpj VARCHAR(14),
                endereco_id INTEGER,
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        """)
        conexao.commit()
        print("Tabela 'corretores' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'corretores': {e}")
    finally:
        conexao.close()

def incluirCorretor(corretor):
    """
    Inclui um novo corretor e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO corretores (nome_corretor, cnpj, endereco_id) VALUES (?, ?, ?)
        """, (corretor.get_nome_corretor(), corretor.get_cnpj(), corretor.get_endereco_id()))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Corretor inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Corretor: {e}")
        return None
    finally:
        conexao.close()

def consultarCorretores():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM corretores')
        rows = cursor.fetchall()
        
        dados_corretores = []
        colunas = ["id_corretor", "nome_corretor", "cnpj", "endereco_id"]
        
        for row in rows:
            corretor_dict = dict(zip(colunas, row))
            dados_corretores.append(corretor_dict)
        
        return dados_corretores
    except sqlite3.Error as e:
        print(f"Erro ao consultar corretores: {e}")
        return []
    finally:
        conexao.close()

def consultarCorretorPorId(corretor_id):
    """
    Consulta e retorna os dados de um corretor específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM corretores WHERE id_corretor = ?', (corretor_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["id_corretor", "nome_corretor", "cnpj", "endereco_id"]
            corretor_dict = dict(zip(colunas, row))
            return corretor_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar corretor por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirCorretor(corretor_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM corretores WHERE id_corretor = ?", (corretor_id,))
        conexao.commit()
        print(f"Corretor com ID {corretor_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Corretor: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarCorretor(corretor):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE corretores 
            SET nome_corretor = ?, cnpj = ?, endereco_id = ?
            WHERE id_corretor = ?
        ''', (corretor.get_nome_corretor(), corretor.get_cnpj(), corretor.get_endereco_id(), corretor.get_id_corretor()))
        conexao.commit()
        print(f"Corretor com ID {corretor.get_id_corretor()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Corretor: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaCorretor()
    print("\n--- Consultando Corretores ---")
    corretores = consultarCorretores()
    for c in corretores:
        print(c)
