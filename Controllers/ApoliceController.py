import sqlite3
from Models.Apolice import Apolice

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaApolice():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS apolice (
                apolice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                proposta_id INTEGER,
                FOREIGN KEY (proposta_id) REFERENCES propostas_seguro (propostas_seguro_id)
            );
        """)
        conexao.commit()
        print("Tabela 'apolice' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'apolice': {e}")
    finally:
        conexao.close()

def incluirApolice(apolice):
    """
    Inclui uma nova apólice e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO apolice (proposta_id) VALUES (?)
        """, (apolice.get_proposta_id(),))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Apolice inserida com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Apolice: {e}")
        return None
    finally:
        conexao.close()

def consultarApolices():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM apolice')
        rows = cursor.fetchall()
        
        dados_apolices = []
        colunas = ["apolice_id", "proposta_id"]
        
        for row in rows:
            apolice_dict = dict(zip(colunas, row))
            dados_apolices.append(apolice_dict)
        
        return dados_apolices
    except sqlite3.Error as e:
        print(f"Erro ao consultar apolice: {e}")
        return []
    finally:
        conexao.close()

def consultarApoliceporId(apolice_id):
    """
    Consulta e retorna os dados de uma apólice específica pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM apolice WHERE apolice_id = ?', (apolice_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["apolice_id", "proposta_id"]
            apolice_dict = dict(zip(colunas, row))
            return apolice_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar apólice por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirApolice(apolice_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM apolice WHERE apolice_id = ?", (apolice_id,))
        conexao.commit()
        print(f"Apolice com ID {apolice_id} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Apolice: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarApolice(apolice):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE apolice 
            SET proposta_id = ?
            WHERE apolice_id = ?
        ''', (apolice.get_proposta_id(), apolice.get_apolice_id()))
        conexao.commit()
        print(f"Apolice com ID {apolice.get_apolice_id()} alterada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Apolice: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaApolice()
    print("\n--- Consultando Apólices ---")
    apolices = consultarApolices()
    for a in apolices:
        print(a)