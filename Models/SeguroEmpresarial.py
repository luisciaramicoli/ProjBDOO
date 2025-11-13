# Models/SeguroEmpresarial.py

class SeguroEmpresarial:
    def __init__(self, seguro_empresarial_id, atividade, endereco_id):
        self._seguro_empresarial_id = seguro_empresarial_id
        self._atividade = atividade
        self._endereco_id = endereco_id

    # --- Getters ---
    def get_seguro_empresarial_id(self):
        return self._seguro_empresarial_id

    def get_atividade(self):
        return self._atividade

    def get_endereco_id(self):
        return self._endereco_id

    # --- Setters ---
    def set_seguro_empresarial_id(self, seguro_empresarial_id):
        self._seguro_empresarial_id = seguro_empresarial_id

    def set_atividade(self, atividade):
        self._atividade = atividade

    def set_endereco_id(self, endereco_id):
        self._endereco_id = endereco_id