import sqlite3
from Models.PlanoSeguro import PlanoSeguro

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    return conexao

def criarTabelaPlanoSeguro():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS planos_seguro (
                nome_plano_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_plano VARCHAR(255),
                valor_total REAL,
                valor_parcela REAL,
                detalhes VARCHAR(255)
            );
        """)
        conexao.commit()
        print("Tabela 'planos_seguro' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'planos_seguro': {e}")
    finally:
        conexao.close()

def incluirPlanoSeguro(plano):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO planos_seguro (nome_plano, valor_total, valor_parcela, detalhes) 
            VALUES (?, ?, ?, ?)
        """, (plano.get_nome_plano(), plano.get_valor_total(), plano.get_valor_parcela(), plano.get_detalhes()))
        conexao.commit()
        print("Plano de Seguro inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir Plano de Seguro: {e}")
    finally:
        conexao.close()

def consultarPlanosSeguro():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM planos_seguro')
        rows = cursor.fetchall()
        
        dados_planos = []
        colunas = ["nome_plano_id", "nome_plano", "valor_total", "valor_parcela", "detalhes"]
        
        for row in rows:
            plano_dict = dict(zip(colunas, row))
            dados_planos.append(plano_dict)
        
        return dados_planos
    except sqlite3.Error as e:
        print(f"Erro ao consultar planos_seguro: {e}")
        return []
    finally:
        conexao.close()

def consultarPlanoPorId(plano_id):
    """
    Consulta e retorna os dados de um plano específico pelo ID.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM planos_seguro WHERE nome_plano_id = ?', (plano_id,))
        row = cursor.fetchone()
        
        if row:
            colunas = ["nome_plano_id", "nome_plano", "valor_total", "valor_parcela", "detalhes"]
            plano_dict = dict(zip(colunas, row))
            return plano_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar plano por ID: {e}")
        return None
    finally:
        conexao.close()
    
def excluirPlanoSeguro(plano_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM planos_seguro WHERE nome_plano_id = ?", (plano_id,))
        conexao.commit()
        print(f"Plano de Seguro com ID {plano_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Plano de Seguro: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarPlanoSeguro(plano):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE planos_seguro 
            SET nome_plano = ?, valor_total = ?, valor_parcela = ?, detalhes = ?
            WHERE nome_plano_id = ?
        ''', (
            plano.get_nome_plano(), 
            plano.get_valor_total(), 
            plano.get_valor_parcela(), 
            plano.get_detalhes(), 
            plano.get_nome_plano_id()
        ))
        conexao.commit()
        print(f"Plano de Seguro com ID {plano.get_nome_plano_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Plano de Seguro: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaPlanoSeguro()
    print("\n--- Consultando Planos de Seguro ---")
    planos = consultarPlanosSeguro()
    for p in planos:
        print(p)