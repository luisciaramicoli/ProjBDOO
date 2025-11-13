# Models/Corretor.py

class Corretor:
    def __init__(self, id_corretor, nome_corretor, cnpj, endereco_id):
        self._id_corretor = id_corretor
        self._nome_corretor = nome_corretor
        self._cnpj = cnpj
        self._endereco_id = endereco_id

    # --- Getters ---
    def get_id_corretor(self):
        return self._id_corretor

    def get_nome_corretor(self):
        return self._nome_corretor

    def get_cnpj(self):
        return self._cnpj

    def get_endereco_id(self):
        return self._endereco_id

    # --- Setters ---
    def set_id_corretor(self, id_corretor):
        self._id_corretor = id_corretor

    def set_nome_corretor(self, nome_corretor):
        self._nome_corretor = nome_corretor

    def set_cnpj(self, cnpj):
        self._cnpj = cnpj

    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id