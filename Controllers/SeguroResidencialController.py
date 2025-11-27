import sqlite3
from Models.SeguroResidencial import SeguroResidencial

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaSeguroResidencial():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seguro_residencial (
                seguro_residencial_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo VARCHAR(255),
                endereco_id INTEGER,
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        """)
        conexao.commit()
        print("Tabela 'seguro_residencial' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'seguro_residencial': {e}")
    finally:
        conexao.close()

def incluirSeguroResidencial(seguro):
    """
    Inclui um novo seguro residencial e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO seguro_residencial (tipo, endereco_id) 
            VALUES (?, ?)
        """, (
            seguro.get_tipo(), 
            seguro.get_endereco_id()
        ))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Seguro Residencial inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Seguro Residencial: {e}")
        return None
    finally:
        conexao.close()

def consultarSegurosResidenciais():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_residencial')
        rows = cursor.fetchall()
        
        dados_seguros = []
        colunas = ["seguro_residencial_id", "tipo", "endereco_id"]
        
        for row in rows:
            seguro_dict = dict(zip(colunas, row))
            dados_seguros.append(seguro_dict)
        
        return dados_seguros
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro_residencial: {e}")
        return []
    finally:
        conexao.close()

def consultarSeguroResidencialPorId(seguro_id):
    """
    Consulta e retorna os dados de um seguro residencial específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_residencial WHERE seguro_residencial_id = ?', (seguro_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["seguro_residencial_id", "tipo", "endereco_id"]
            seguro_dict = dict(zip(colunas, row))
            return seguro_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro residencial por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirSeguroResidencial(seguro_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM seguro_residencial WHERE seguro_residencial_id = ?", (seguro_id,))
        conexao.commit()
        print(f"Seguro Residencial com ID {seguro_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Seguro Residencial: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarSeguroResidencial(seguro):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE seguro_residencial 
            SET tipo = ?, endereco_id = ?
            WHERE seguro_residencial_id = ?
        ''', (
            seguro.get_tipo(), 
            seguro.get_endereco_id(), 
            seguro.get_seguro_residencial_id()
        ))
        conexao.commit()
        print(f"Seguro Residencial com ID {seguro.get_seguro_residencial_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Seguro Residencial: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaSeguroResidencial()
    print("\n--- Consultando Seguros Residenciais ---")
    seguros = consultarSegurosResidenciais()
    for s in seguros:
        print(s)