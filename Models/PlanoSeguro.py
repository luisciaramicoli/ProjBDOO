# Models/PlanoSeguro.py

class PlanoSeguro:
    def __init__(self, nome_plano_id, nome_plano, valor_total, valor_parcela, detalhes):
        self._nome_plano_id = nome_plano_id
        self._nome_plano = nome_plano
        self._valor_total = valor_total
        self._valor_parcela = valor_parcela
        self._detalhes = detalhes

    # --- Getters ---
    def get_nome_plano_id(self):
        return self._nome_plano_id

    def get_nome_plano(self):
        return self._nome_plano

    def get_valor_total(self):
        return self._valor_total

    def get_valor_parcela(self):
        return self._valor_parcela

    def get_detalhes(self):
        return self._detalhes

    # --- Setters ---
    def set_nome_plano_id(self, nome_plano_id):
        self._nome_plano_id = nome_plano_id

    def set_nome_plano(self, nome_plano):
        self._nome_plano = nome_plano

    def set_valor_total(self, valor_total):
        self._valor_total = valor_total

    def set_valor_parcela(self, valor_parcela):
        self._valor_parcela = valor_parcela

    def set_detalhes(self, detalhes):
        self._detalhes = detalhes