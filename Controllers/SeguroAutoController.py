import sqlite3
from Models.SeguroAuto import SeguroAuto

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaSeguroAuto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seguro_auto (
                seguro_auto_id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa VARCHAR(10),
                modelo VARCHAR(255),
                ano INTEGER(5),
                endereco_id INTEGER, 
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        """)
        conexao.commit()
        print("Tabela 'seguro_auto' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'seguro_auto': {e}")
    finally:
        conexao.close()

def incluirSeguroAuto(seguro):
    """
    Inclui um novo seguro auto e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO seguro_auto (placa, modelo, ano, endereco_id) 
            VALUES (?, ?, ?, ?)
        """, (
            seguro.get_placa(), 
            seguro.get_modelo(), 
            seguro.get_ano(), 
            seguro.get_endereco_id()
        ))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Seguro Auto inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Seguro Auto: {e}")
        return None
    finally:
        conexao.close()

def consultarSegurosAuto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_auto')
        rows = cursor.fetchall()
        
        dados_seguros = []
        colunas = ["seguro_auto_id", "placa", "modelo", "ano", "endereco_id"]
        
        for row in rows:
            seguro_dict = dict(zip(colunas, row))
            dados_seguros.append(seguro_dict)
        
        return dados_seguros
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro_auto: {e}")
        return []
    finally:
        conexao.close()

def consultarSeguroAutoPorId(seguro_id):
    """
    Consulta e retorna os dados de um seguro auto específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_auto WHERE seguro_auto_id = ?', (seguro_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["seguro_auto_id", "placa", "modelo", "ano", "endereco_id"]
            seguro_dict = dict(zip(colunas, row))
            return seguro_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro auto por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirSeguroAuto(seguro_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM seguro_auto WHERE seguro_auto_id = ?", (seguro_id,))
        conexao.commit()
        print(f"Seguro Auto com ID {seguro_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Seguro Auto: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarSeguroAuto(seguro):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE seguro_auto 
            SET placa = ?, modelo = ?, ano = ?, endereco_id = ?
            WHERE seguro_auto_id = ?
        ''', (
            seguro.get_placa(), 
            seguro.get_modelo(), 
            seguro.get_ano(), 
            seguro.get_endereco_id(), 
            seguro.get_seguro_auto_id()
        ))
        conexao.commit()
        print(f"Seguro Auto com ID {seguro.get_seguro_auto_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Seguro Auto: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaSeguroAuto()
    print("\n--- Consultando Seguros Auto ---")
    seguros = consultarSegurosAuto()
    for s in seguros:
        print(s)