import sqlite3
from Models.Reembolso import Reembolso

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaReembolso():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reembolso (
                reembolso_id INTEGER PRIMARY KEY AUTOINCREMENT,
                seguro_auto VARCHAR(255),
                planos_de_seguro VARCHAR(255),
                valor REAL
            );
        """)
        conexao.commit()
        print("Tabela 'reembolso' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'reembolso': {e}")
    finally:
        conexao.close()

def incluirReembolso(reembolso):
    """
    Inclui um novo reembolso e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO reembolso (seguro_auto, planos_de_seguro, valor) 
            VALUES (?, ?, ?)
        """, (reembolso.get_seguro_auto(), reembolso.get_planos_de_seguro(), reembolso.get_valor()))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Reembolso inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Reembolso: {e}")
        return None
    finally:
        conexao.close()

def consultarReembolsos():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM reembolso')
        rows = cursor.fetchall()
        
        dados_reembolsos = []
        colunas = ["reembolso_id", "seguro_auto", "planos_de_seguro", "valor"]
        
        for row in rows:
            reembolso_dict = dict(zip(colunas, row))
            dados_reembolsos.append(reembolso_dict)
        
        return dados_reembolsos
    except sqlite3.Error as e:
        print(f"Erro ao consultar reembolso: {e}")
        return []
    finally:
        conexao.close()

def consultarReembolsoPorId(reembolso_id):
    """
    Consulta e retorna os dados de um reembolso específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM reembolso WHERE reembolso_id = ?', (reembolso_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["reembolso_id", "seguro_auto", "planos_de_seguro", "valor"]
            reembolso_dict = dict(zip(colunas, row))
            return reembolso_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar reembolso por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirReembolso(reembolso_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM reembolso WHERE reembolso_id = ?", (reembolso_id,))
        conexao.commit()
        print(f"Reembolso com ID {reembolso_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Reembolso: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarReembolso(reembolso):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE reembolso 
            SET seguro_auto = ?, planos_de_seguro = ?, valor = ?
            WHERE reembolso_id = ?
        ''', (
            reembolso.get_seguro_auto(), 
            reembolso.get_planos_de_seguro(), 
            reembolso.get_valor(), 
            reembolso.get_reembolso_id()
        ))
        conexao.commit()
        print(f"Reembolso com ID {reembolso.get_reembolso_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Reembolso: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaReembolso()
    print("\n--- Consultando Reembolsos ---")
    reembolsos = consultarReembolsos()
    for r in reembolsos:
        print(r)