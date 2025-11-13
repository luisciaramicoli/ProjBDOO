import sqlite3

conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

cursor.execute(
    '''
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
            valor_iof REAL
        );
    '''
)

cursor.close()
print("Tabela 'propostas_seguro' criada com sucesso no banco de dados Seguro.db!")