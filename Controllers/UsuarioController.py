import sqlite3
from Models.Usuario import Usuario

def conectaBD():
    conexao = sqlite3.connect("Seguro.db")
    # Ativa o uso de chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criarTabelaUsuario():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
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
        """)
        conexao.commit()
        print("Tabela 'usuario' verificada/criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela 'usuario': {e}")
    finally:
        conexao.close()

def incluirUsuario(usuario):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuario (
                nome, cpf, data_nascimento, telefone, email, senha, 
                endereco_id, reset_token, reset_token_expiracao, tus_code, nome_social
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            usuario.get_nome(),
            usuario.get_cpf(),
            usuario.get_data_nascimento(),
            usuario.get_telefone(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_endereco_id(),
            usuario.get_reset_token(),
            usuario.get_reset_token_expiracao(),
            usuario.get_tus_code(),
            usuario.get_nome_social()
        ))
        conexao.commit()
        print("Usuário inserido com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade ao inserir usuário (CPF ou Email podem já existir): {e}")
        raise e # Propaga o erro para o main.py tratar
    except sqlite3.Error as e:
        print(f"Erro ao inserir usuário: {e}")
        raise e
    finally:
        conexao.close()

def consultarUsuarios():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM usuario')
        rows = cursor.fetchall()
        
        dados_usuarios = []
        # Nomes das colunas conforme a tabela
        colunas = [
            "usuario_id", "nome", "cpf", "data_nascimento", "telefone", 
            "email", "senha", "endereco_id", "reset_token", 
            "reset_token_expiracao", "tus_code", "nome_social"
        ]
        
        for row in rows:
            usuario_dict = dict(zip(colunas, row))
            dados_usuarios.append(usuario_dict)
        
        return dados_usuarios
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuários: {e}")
        return []
    finally:
        conexao.close()
    
def excluirUsuario(usuario_id):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuario WHERE usuario_id = ?", (usuario_id,))
        conexao.commit()
        print(f"Usuário com ID {usuario_id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarUsuario(usuario):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE usuario 
            SET 
                nome = ?,
                cpf = ?,
                data_nascimento = ?,
                telefone = ?,
                email = ?,
                senha = ?,
                endereco_id = ?,
                reset_token = ?,
                reset_token_expiracao = ?,
                tus_code = ?,
                nome_social = ?
            WHERE usuario_id = ?
        ''', (
            usuario.get_nome(),
            usuario.get_cpf(),
            usuario.get_data_nascimento(),
            usuario.get_telefone(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_endereco_id(),
            usuario.get_reset_token(),
            usuario.get_reset_token_expiracao(),
            usuario.get_tus_code(),
            usuario.get_nome_social(),
            usuario.get_usuario_id() # Este é o 'WHERE'
        ))
        conexao.commit()
        print(f"Usuário com ID {usuario.get_usuario_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar usuário: {e}")
    finally:
        if conexao:
            conexao.close()

def checarLogin(email, senha):
    """
    Verifica se o email e a senha correspondem a um usuário.
    Retorna (True, tus_code) em caso de sucesso, ou (False, None) em caso de falha.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "SELECT tus_code FROM usuario WHERE email = ? AND senha = ?", 
            (email, senha)
        )
        resultado = cursor.fetchone() # Pega apenas o primeiro resultado
        
        if resultado:
            return True, resultado[0] # Retorna True e o tus_code
        else:
            return False, None # Login falhou
            
    except sqlite3.Error as e:
        print(f"Erro ao checar login: {e}")
        return False, None
    finally:
        conexao.close()

def consultarUsuarioPorEmail(email):
    """
    Consulta e retorna todos os dados de um usuário pelo email.
    Retorna um dicionário com os dados ou None se não encontrar.
    """
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM usuario WHERE email = ?', (email,))
        row = cursor.fetchone()
        
        if row:
            colunas = [
                "usuario_id", "nome", "cpf", "data_nascimento", "telefone", 
                "email", "senha", "endereco_id", "reset_token", 
                "reset_token_expiracao", "tus_code", "nome_social"
            ]
            usuario_dict = dict(zip(colunas, row))
            return usuario_dict
        else:
            return None
            
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuário por email: {e}")
        return None
    finally:
        conexao.close()


# Bloco de inicialização (bom para verificar a tabela ao iniciar)
if __name__ == "__main__":
    criarTabelaUsuario()
    
    print("\n--- Consultando Usuários ---")
    usuarios = consultarUsuarios()
    for u in usuarios:
        print(u)