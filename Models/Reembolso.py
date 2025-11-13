# Models/Reembolso.py

class Reembolso:
    def __init__(self, reembolso_id, seguro_auto, planos_de_seguro, valor):
        self._reembolso_id = reembolso_id
        self._seguro_auto = seguro_auto
        self._planos_de_seguro = planos_de_seguro
        self._valor = valor

    # --- Getters ---
    def get_reembolso_id(self):
        return self._reembolso_id

    def get_seguro_auto(self):
        return self._seguro_auto

    def get_planos_de_seguro(self):
        return self._planos_de_seguro

    def get_valor(self):
        return self._valor

    # --- Setters ---
    def set_reembolso_id(self, reembolso_id):
        self._reembolso_id = reembolso_id

    def set_seguro_auto(self, seguro_auto):
        self._seguro_auto = seguro_auto

    def set_planos_de_seguro(self, planos_de_seguro):
        self._planos_de_seguro = planos_de_seguro

    def set_valor(self, valor):
        self._valor = valor