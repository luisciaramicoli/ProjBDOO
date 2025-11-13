# Models/Endereco.py

class Endereco:
    def __init__(self, endereco_id, cep, logradouro, numero, complemento, bairro, cidade, estado):
        self._endereco_id = endereco_id
        self._cep = cep
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado

    # --- Getters ---
    def get_endereco_id(self):
        return self._endereco_id

    def get_cep(self):
        return self._cep

    def get_logradouro(self):
        return self._logradouro

    def get_numero(self):
        return self._numero

    def get_complemento(self):
        return self._complemento

    def get_bairro(self):
        return self._bairro

    def get_cidade(self):
        return self._cidade

    def get_estado(self):
        return self._estado

    # --- Setters ---
    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id

    def set_cep(self, cep):
        self._cep = cep

    def set_logradouro(self, logradouro):
        self._logradouro = logradouro

    def set_numero(self, numero):
        self._numero = numero

    def set_complemento(self, complemento):
        self._complemento = complemento

    def set_bairro(self, bairro):
        self._bairro = bairro

    def set_cidade(self, cidade):
        self._cidade = cidade

    def set_estado(self, estado):
        self._estado = estado