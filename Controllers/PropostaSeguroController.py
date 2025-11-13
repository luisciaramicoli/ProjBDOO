import sqlite3
from Models.PropostaSeguro import PropostaSeguro

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaPropostaSeguro():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS propostas_seguro (
                propostas_seguro_id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                endereco_id INTEGER,
                seguro_auto_id INTEGER,
                seguro_residencial_id INTEGER,
                seguro_empresarial_id INTEGER,
                seguro_vida_id INTEGER,
                corretor_id INTEGER,
                nome_plano VARCHAR(255),
                valor_parcela REAL,
                num_parcela INTEGER,
                reebolso_fraquia_max VARCHAR(255),
                data_proposta DATE,
                forma_pagamento VARCHAR(255),
                numero_de_parcelas INTEGER,
                status_aprovacao BOOLEAN,
                numero_apolice BOOLEAN,
                vigencia_inicio DATE,
                vigencia_fim DATE,
                valor_total_pago REAL,
                cobertura_limite REAL,
                cobertura_premio REAL,
                valor_total_liquido REAL,
                valor_iof REAL,
                FOREIGN KEY (usuario_id) REFERENCES usuario (usuario_id),
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id),
                FOREIGN KEY (seguro_auto_id) REFERENCES seguro_auto (seguro_auto_id),
                FOREIGN KEY (seguro_residencial_id) REFERENCES seguro_residencial (seguro_residencial_id),
                FOREIGN KEY (seguro_empresarial_id) REFERENCES seguro_empresarial (seguro_empresarial_id),
                FOREIGN KEY (seguro_vida_id) REFERENCES seguro_vida (seguro_vida_id),
                FOREIGN KEY (corretor_id) REFERENCES corretores (id_corretor)
            );
        """)
        conexao.commit()
        print("Tabela 'propostas_seguro' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'propostas_seguro': {e}")
    finally:
        conexao.close()

def incluirPropostaSeguro(proposta):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO propostas_seguro (
                usuario_id, endereco_id, seguro_auto_id, seguro_residencial_id, 
                seguro_empresarial_id, seguro_vida_id, corretor_id, nome_plano, 
                valor_parcela, num_parcela, reebolso_fraquia_max, data_proposta, 
                forma_pagamento, numero_de_parcelas, status_aprovacao, numero_apolice, 
                vigencia_inicio, vigencia_fim, valor_total_pago, cobertura_limite, 
                cobertura_premio, valor_total_liquido, valor_iof
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            proposta.get_usuario_id(),
            proposta.get_endereco_id(),
            proposta.get_seguro_auto_id(),
            proposta.get_seguro_residencial_id(),
            proposta.get_seguro_empresarial_id(),
            proposta.get_seguro_vida_id(),
            proposta.get_corretor_id(),
            proposta.get_nome_plano(),
            proposta.get_valor_parcela(),
            proposta.get_num_parcela(),
            proposta.get_reebolso_fraquia_max(),
            proposta.get_data_proposta(),
            proposta.get_forma_pagamento(),
            proposta.get_numero_de_parcelas(),
            proposta.get_status_aprovacao(),
            proposta.get_numero_apolice(),
            proposta.get_vigencia_inicio(),
            proposta.get_vigencia_fim(),
            proposta.get_valor_total_pago(),
            proposta.get_cobertura_limite(),
            proposta.get_cobertura_premio(),
            proposta.get_valor_total_liquido(),
            proposta.get_valor_iof()
        ))
        conexao.commit()
        print("PropostaSeguro inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir PropostaSeguro: {e}")
    finally:
        conexao.close()

def _get_colunas_proposta():
    # Helper para garantir que a ordem das colunas esteja correta
    return [
        "propostas_seguro_id", "usuario_id", "endereco_id", "seguro_auto_id",
        "seguro_residencial_id", "seguro_empresarial_id", "seguro_vida_id",
        "corretor_id", "nome_plano", "valor_parcela", "num_parcela",
        "reebolso_fraquia_max", "data_proposta", "forma_pagamento",
        "numero_de_parcelas", "status_aprovacao", "numero_apolice",
        "vigencia_inicio", "vigencia_fim", "valor_total_pago",
        "cobertura_limite", "cobertura_premio", "valor_total_liquido", "valor_iof"
    ]

def consultarPropostasSeguro():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM propostas_seguro')
        rows = cursor.fetchall()
        
        dados_propostas = []
        colunas = _get_colunas_proposta()
        
        for row in rows:
            proposta_dict = dict(zip(colunas, row))
            dados_propostas.append(proposta_dict)
        
        return dados_propostas
    except sqlite3.Error as e:
        print(f"Erro ao consultar propostas_seguro: {e}")
        return []
    finally:
        conexao.close()

def consultarPropostasPorUsuarioId(usuario_id):
    """
    Consulta e retorna todas as propostas de um usuário específico.
    Retorna uma lista de dicionários.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM propostas_seguro WHERE usuario_id = ?', (usuario_id,))
        rows = cursor.fetchall()
        
        dados_propostas = []
        colunas = _get_colunas_proposta()
        
        for row in rows:
            proposta_dict = dict(zip(colunas, row))
            dados_propostas.append(proposta_dict)
        
        return dados_propostas
    except sqlite3.Error as e:
        print(f"Erro ao consultar propostas por usuário: {e}")
        return []
    finally:
        conexao.close()
    
def excluirPropostaSeguro(proposta_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM propostas_seguro WHERE propostas_seguro_id = ?", (proposta_id,))
        conexao.commit()
        print(f"PropostaSeguro com ID {proposta_id} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir PropostaSeguro: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarPropostaSeguro(proposta):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE propostas_seguro 
            SET 
                usuario_id = ?, endereco_id = ?, seguro_auto_id = ?, seguro_residencial_id = ?,
                seguro_empresarial_id = ?, seguro_vida_id = ?, corretor_id = ?, nome_plano = ?,
                valor_parcela = ?, num_parcela = ?, reebolso_fraquia_max = ?, data_proposta = ?,
                forma_pagamento = ?, numero_de_parcelas = ?, status_aprovacao = ?, numero_apolice = ?,
                vigencia_inicio = ?, vigencia_fim = ?, valor_total_pago = ?, cobertura_limite = ?,
                cobertura_premio = ?, valor_total_liquido = ?, valor_iof = ?
            WHERE propostas_seguro_id = ?
        ''', (
            proposta.get_usuario_id(),
            proposta.get_endereco_id(),
            proposta.get_seguro_auto_id(),
            proposta.get_seguro_residencial_id(),
            proposta.get_seguro_empresarial_id(),
            proposta.get_seguro_vida_id(),
            proposta.get_corretor_id(),
            proposta.get_nome_plano(),
            proposta.get_valor_parcela(),
            proposta.get_num_parcela(),
            proposta.get_reebolso_fraquia_max(),
            proposta.get_data_proposta(),
            proposta.get_forma_pagamento(),
            proposta.get_numero_de_parcelas(),
            proposta.get_status_aprovacao(),
            proposta.get_numero_apolice(),
            proposta.get_vigencia_inicio(),
            proposta.get_vigencia_fim(),
            proposta.get_valor_total_pago(),
            proposta.get_cobertura_limite(),
            proposta.get_cobertura_premio(),
            proposta.get_valor_total_liquido(),
            proposta.get_valor_iof(),
            proposta.get_propostas_seguro_id() # Este é o 'WHERE'
        ))
        conexao.commit()
        print(f"PropostaSeguro com ID {proposta.get_propostas_seguro_id()} alterada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar PropostaSeguro: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criarTabelaPropostaSeguro()
    print("\n--- Consultando Propostas de Seguro ---")
    propostas = consultarPropostasSeguro()
    for p in propostas:
        print(p)