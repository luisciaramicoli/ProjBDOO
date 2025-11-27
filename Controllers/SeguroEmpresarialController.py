import sqlite3
from Models.SeguroEmpresarial import SeguroEmpresarial

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaSeguroEmpresarial():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seguro_empresarial (
                seguro_empresarial_id INTEGER PRIMARY KEY AUTOINCREMENT,
                atividade VARCHAR(255),
                endereco_id INTEGER,
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        """)
        conexao.commit()
        print("Tabela 'seguro_empresarial' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'seguro_empresarial': {e}")
    finally:
        conexao.close()

def incluirSeguroEmpresarial(seguro):
    """
    Inclui um novo seguro empresarial e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO seguro_empresarial (atividade, endereco_id) 
            VALUES (?, ?)
        """, (
            seguro.get_atividade(), 
            seguro.get_endereco_id()
        ))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Seguro Empresarial inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Seguro Empresarial: {e}")
        return None
    finally:
        conexao.close()

def consultarSegurosEmpresariais():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_empresarial')
        rows = cursor.fetchall()
        
        dados_seguros = []
        colunas = ["seguro_empresarial_id", "atividade", "endereco_id"]
        
        for row in rows:
            seguro_dict = dict(zip(colunas, row))
            dados_seguros.append(seguro_dict)
        
        return dados_seguros
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro_empresarial: {e}")
        return []
    finally:
        conexao.close()

def consultarSeguroEmpresarialPorId(seguro_id):
    """
    Consulta e retorna os dados de um seguro empresarial específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_empresarial WHERE seguro_empresarial_id = ?', (seguro_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["seguro_empresarial_id", "atividade", "endereco_id"]
            seguro_dict = dict(zip(colunas, row))
            return seguro_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro empresarial por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirSeguroEmpresarial(seguro_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM seguro_empresarial WHERE seguro_empresarial_id = ?", (seguro_id,))
        conexao.commit()
        print(f"Seguro Empresarial com ID {seguro_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Seguro Empresarial: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarSeguroEmpresarial(seguro):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE seguro_empresarial 
            SET atividade = ?, endereco_id = ?
            WHERE seguro_empresarial_id = ?
        ''', (
            seguro.get_atividade(), 
            seguro.get_endereco_id(), 
            seguro.get_seguro_empresarial_id()
        ))
        conexao.commit()
        print(f"Seguro Empresarial com ID {seguro.get_seguro_empresarial_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Seguro Empresarial: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaSeguroEmpresarial()
    print("\n--- Consultando Seguros Empresariais ---")
    seguros = consultarSegurosEmpresariais()
    for s in seguros:
        print(s)