import sqlite3
import datetime

# Conecta ao banco de dados 'Seguro.db'
conexao = sqlite3.connect("Seguro.db")
cursor = conexao.cursor()

# --- 1. Criar Tabela (Versão Correta com Constraints) ---
# A estrutura é baseada no UsuarioController
try:
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS usuario (
                usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255),
                cpf VARCHAR(11) UNIQUE,
                data_nascimento DATE,
                telefone VARCHAR(10),
                email VARCHAR(255) UNIQUE,
                senha VARCHAR(255),
                endereco_id INTEGER,
                reset_token VARCHAR(255),
                reset_token_expiracao DATE,
                tus_code INTEGER,
                nome_social VARCHAR(255),
                FOREIGN KEY (endereco_id) REFERENCES enderecos (endereco_id)
            );
        '''
    )
    print("Tabela 'usuario' verificada/criada com sucesso.")

    # --- 2. Inserir Usuário Admin ---
    admin_email = "admin@seguro.com"
    admin_data = (
        "Administrador",
        "00000000000",  # CPF (deve ser único)
        datetime.date(2000, 1, 1), # Data de Nascimento
        "0000000000", # Telefone
        admin_email,
        "admin123", # Senha
        None, # endereco_id (NULL)
        None, # reset_token (NULL)
        None, # reset_token_expiracao (NULL)
        2,    # tus_code (Admin)
        "Admin" # nome_social
    )
    
    # INSERT OR IGNORE não falha se o email/cpf já existir
    cursor.execute(
        '''
        INSERT OR IGNORE INTO usuario (
            nome, cpf, data_nascimento, telefone, email, senha, 
            endereco_id, reset_token, reset_token_expiracao, tus_code, nome_social
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', admin_data
    )
    
    # Verifica se a inserção foi bem-sucedida
    if cursor.rowcount > 0:
        print(f"Usuário admin '{admin_email}' criado com sucesso.")
    else:
        print(f"Usuário admin '{admin_email}' já existe.")

    conexao.commit()

except sqlite3.Error as e:
    print(f"Erro ao inicializar tabela 'usuario' ou inserir admin: {e}")
    
finally:
    cursor.close()
    conexao.close()
    print("Conexão com Seguro.db fechada.")