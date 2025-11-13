import sqlite3
from Models.SeguroVida import SeguroVida

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaSeguroVida():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seguro_vida (
                seguro_vida_id INTEGER PRIMARY KEY AUTOINCREMENT,
                atividade VARCHAR(255),
                endereco_id INTEGER,
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        """)
        conexao.commit()
        print("Tabela 'seguro_vida' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'seguro_vida': {e}")
    finally:
        conexao.close()

def incluirSeguroVida(seguro):
    """
    Inclui um novo seguro de vida e retorna o ID do registro inserido.
    Retorna o ID em caso de sucesso, ou None em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO seguro_vida (atividade, endereco_id) 
            VALUES (?, ?)
        """, (
            seguro.get_atividade(), 
            seguro.get_endereco_id()
        ))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"Seguro de Vida inserido com sucesso! ID: {novo_id}")
        return novo_id
    except sqlite3.Error as e:
        print(f"Erro ao inserir Seguro de Vida: {e}")
        return None
    finally:
        conexao.close()

def consultarSegurosVida():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM seguro_vida')
        rows = cursor.fetchall()
        
        dados_seguros = []
        colunas = ["seguro_vida_id", "atividade", "endereco_id"]
        
        for row in rows:
            seguro_dict = dict(zip(colunas, row))
            dados_seguros.append(seguro_dict)
        
        return dados_seguros
    except sqlite3.Error as e:
        print(f"Erro ao consultar seguro_vida: {e}")
        return []
    finally:
        conexao.close()
    
def excluirSeguroVida(seguro_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM seguro_vida WHERE seguro_vida_id = ?", (seguro_id,))
        conexao.commit()
        print(f"Seguro de Vida com ID {seguro_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Seguro de Vida: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarSeguroVida(seguro):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE seguro_vida 
            SET atividade = ?, endereco_id = ?
            WHERE seguro_vida_id = ?
        ''', (
            seguro.get_atividade(), 
            seguro.get_endereco_id(), 
            seguro.get_seguro_vida_id()
        ))
        conexao.commit()
        print(f"Seguro de Vida com ID {seguro.get_seguro_vida_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Seguro de Vida: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaSeguroVida()
    print("\n--- Consultando Seguros de Vida ---")
    seguros = consultarSegurosVida()
    for s in seguros:
        print(s)