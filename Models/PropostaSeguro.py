# Models/PropostaSeguro.py

class PropostaSeguro:
    def __init__(self, propostas_seguro_id, usuario_id, endereco_id, seguro_auto_id, 
                 seguro_residencial_id, seguro_empresarial_id, seguro_vida_id, 
                 corretor_id, nome_plano, valor_parcela, num_parcela, 
                 reebolso_fraquia_max, data_proposta, forma_pagamento, 
                 numero_de_parcelas, status_aprovacao, numero_apolice, 
                 vigencia_inicio, vigencia_fim, valor_total_pago, 
                 cobertura_limite, cobertura_premio, valor_total_liquido, valor_iof):
        
        self._propostas_seguro_id = propostas_seguro_id
        self._usuario_id = usuario_id
        self._endereco_id = endereco_id
        self._seguro_auto_id = seguro_auto_id
        self._seguro_residencial_id = seguro_residencial_id
        self._seguro_empresarial_id = seguro_empresarial_id
        self._seguro_vida_id = seguro_vida_id
        self._corretor_id = corretor_id
        self._nome_plano = nome_plano
        self._valor_parcela = valor_parcela
        self._num_parcela = num_parcela
        self._reebolso_fraquia_max = reebolso_fraquia_max
        self._data_proposta = data_proposta
        self._forma_pagamento = forma_pagamento
        self._numero_de_parcelas = numero_de_parcelas
        self._status_aprovacao = status_aprovacao
        self._numero_apolice = numero_apolice
        self._vigencia_inicio = vigencia_inicio
        self._vigencia_fim = vigencia_fim
        self._valor_total_pago = valor_total_pago
        self._cobertura_limite = cobertura_limite
        self._cobertura_premio = cobertura_premio
        self._valor_total_liquido = valor_total_liquido
        self._valor_iof = valor_iof

    # --- Getters ---
    def get_propostas_seguro_id(self): return self._propostas_seguro_id
    def get_usuario_id(self): return self._usuario_id
    def get_endereco_id(self): return self._endereco_id
    def get_seguro_auto_id(self): return self._seguro_auto_id
    def get_seguro_residencial_id(self): return self._seguro_residencial_id
    def get_seguro_empresarial_id(self): return self._seguro_empresarial_id
    def get_seguro_vida_id(self): return self._seguro_vida_id
    def get_corretor_id(self): return self._corretor_id
    def get_nome_plano(self): return self._nome_plano
    def get_valor_parcela(self): return self._valor_parcela
    def get_num_parcela(self): return self._num_parcela
    def get_reebolso_fraquia_max(self): return self._reebolso_fraquia_max
    def get_data_proposta(self): return self._data_proposta
    def get_forma_pagamento(self): return self._forma_pagamento
    def get_numero_de_parcelas(self): return self._numero_de_parcelas
    def get_status_aprovacao(self): return self._status_aprovacao
    def get_numero_apolice(self): return self._numero_apolice
    def get_vigencia_inicio(self): return self._vigencia_inicio
    def get_vigencia_fim(self): return self._vigencia_fim
    def get_valor_total_pago(self): return self._valor_total_pago
    def get_cobertura_limite(self): return self._cobertura_limite
    def get_cobertura_premio(self): return self._cobertura_premio
    def get_valor_total_liquido(self): return self._valor_total_liquido
    def get_valor_iof(self): return self._valor_iof

    # --- Setters ---
    def set_propostas_seguro_id(self, v): self._propostas_seguro_id = v
    def set_usuario_id(self, v): self._usuario_id = v
    def set_endereco_id(self, v): self._endereco_id = v
    def set_seguro_auto_id(self, v): self._seguro_auto_id = v
    def set_seguro_residencial_id(self, v): self._seguro_residencial_id = v
    def set_seguro_empresarial_id(self, v): self._seguro_empresarial_id = v
    def set_seguro_vida_id(self, v): self._seguro_vida_id = v
    def set_corretor_id(self, v): self._corretor_id = v
    def set_nome_plano(self, v): self._nome_plano = v
    def set_valor_parcela(self, v): self._valor_parcela = v
    def set_num_parcela(self, v): self._num_parcela = v
    def set_reebolso_fraquia_max(self, v): self._reebolso_fraquia_max = v
    def set_data_proposta(self, v): self._data_proposta = v
    def set_forma_pagamento(self, v): self._forma_pagamento = v
    def set_numero_de_parcelas(self, v): self._numero_de_parcelas = v
    def set_status_aprovacao(self, v): self._status_aprovacao = v
    def set_numero_apolice(self, v): self._numero_apolice = v
    def set_vigencia_inicio(self, v): self._vigencia_inicio = v
    def set_vigencia_fim(self, v): self._vigencia_fim = v
    def set_valor_total_pago(self, v): self._valor_total_pago = v
    def set_cobertura_limite(self, v): self._cobertura_limite = v
    def set_cobertura_premio(self, v): self._cobertura_premio = v
    def set_valor_total_liquido(self, v): self._valor_total_liquido = v
    def set_valor_iof(self, v): self._valor_iof