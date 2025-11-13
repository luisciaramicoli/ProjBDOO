# Models/Apolice.py

class Apolice:
    def __init__(self, apolice_id, proposta_id):
        self._apolice_id = apolice_id
        self._proposta_id = proposta_id

    # --- Getters ---
    def get_apolice_id(self):
        return self._apolice_id

    def get_proposta_id(self):
        return self._proposta_id

    # --- Setters ---
    def set_apolice_id(self, apolice_id):
        self._apolice_id = apolice_id

    def set_proposta_id(self, proposta_id):
        self._proposta_id = proposta_id