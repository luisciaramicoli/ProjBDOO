# Models/SeguroAuto.py

class SeguroAuto:
    def __init__(self, seguro_auto_id, placa, modelo, ano, endereco_id):
        self._seguro_auto_id = seguro_auto_id
        self._placa = placa
        self._modelo = modelo
        self._ano = ano
        self._endereco_id = endereco_id

    # --- Getters ---
    def get_seguro_auto_id(self):
        return self._seguro_auto_id

    def get_placa(self):
        return self._placa

    def get_modelo(self):
        return self._modelo

    def get_ano(self):
        return self._ano

    def get_endereco_id(self):
        return self._endereco_id

    # --- Setters ---
    def set_seguro_auto_id(self, seguro_auto_id):
        self._seguro_auto_id = seguro_auto_id

    def set_placa(self, placa):
        self._placa = placa

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_ano(self, ano):
        self._ano = ano

    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id