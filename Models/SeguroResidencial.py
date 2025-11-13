# Models/SeguroResidencial.py

class SeguroResidencial:
    def __init__(self, seguro_residencial_id, tipo, endereco_id):
        self._seguro_residencial_id = seguro_residencial_id
        self._tipo = tipo
        self._endereco_id = endereco_id

    # --- Getters ---
    def get_seguro_residencial_id(self):
        return self._seguro_residencial_id

    def get_tipo(self):
        return self._tipo

    def get_endereco_id(self):
        return self._endereco_id

    # --- Setters ---
    def set_seguro_residencial_id(self, seguro_residencial_id):
        self._seguro_residencial_id = seguro_residencial_id

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id