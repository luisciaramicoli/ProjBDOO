import sqlite3
from Models.Apolice import Apolice

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    return conexao

def criarTabelaApolice():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS apolice (
                apolice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                proposta_id INTEGER
            );
        """)
        conexao.commit()
        print("Tabela 'apolice' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'apolice': {e}")
    finally:
        conexao.close()

def incluirApolice(apolice):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO apolice (proposta_id) VALUES (?)
        """, (apolice.get_proposta_id(),))
        conexao.commit()
        print("Apolice inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir Apolice: {e}")
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