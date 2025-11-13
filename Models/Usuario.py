# Models/Usuario.py

class Usuario:
    def __init__(self, usuario_id, nome, cpf, data_nascimento, telefone, email, senha, 
                 endereco_id, reset_token, reset_token_expiracao, tus_code, nome_social):
        self._usuario_id = usuario_id
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone
        self._email = email
        self._senha = senha
        self._endereco_id = endereco_id
        self._reset_token = reset_token
        self._reset_token_expiracao = reset_token_expiracao
        self._tus_code = tus_code
        self._nome_social = nome_social

    # --- Getters ---
    def get_usuario_id(self):
        return self._usuario_id

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_data_nascimento(self):
        return self._data_nascimento

    def get_telefone(self):
        return self._telefone

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha

    def get_endereco_id(self):
        return self._endereco_id

    def get_reset_token(self):
        return self._reset_token

    def get_reset_token_expiracao(self):
        return self._reset_token_expiracao

    def get_tus_code(self):
        return self._tus_code

    def get_nome_social(self):
        return self._nome_social

    # --- Setters ---
    def set_usuario_id(self, usuario_id):
        self._usuario_id = usuario_id

    def set_nome(self, nome):
        self._nome = nome

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_email(self, email):
        self._email = email

    def set_senha(self, senha):
        self._senha = senha

    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id

    def set_reset_token(self, reset_token):
        self._reset_token = reset_token

    def set_reset_token_expiracao(self, reset_token_expiracao):
        self._reset_token_expiracao = reset_token_expiracao

    def set_tus_code(self, tus_code):
        self._tus_code = tus_code

    def set_nome_social(self, nome_social):
        self._nome_social = nome_social