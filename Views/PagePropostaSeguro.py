import streamlit as st
import pandas as pd
import Controllers.PropostaSeguroController as propostaController
from Models.PropostaSeguro import PropostaSeguro
import datetime

def show_proposta_seguro_page():
    st.title('Cadastro de Propostas de Seguro')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Proposta de Seguro")
        with st.form(key="incluir_proposta"):
            col1, col2, col3 = st.columns(3)
            with col1:
                usuario_id = st.number_input("ID Usuário:", min_value=1, step=1)
                endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)
                seguro_auto_id = st.number_input("ID Seguro Auto (opcional):", min_value=0, step=1)
                seguro_residencial_id = st.number_input("ID Seguro Residencial (opcional):", min_value=0, step=1)
                seguro_empresarial_id = st.number_input("ID Seguro Empresarial (opcional):", min_value=0, step=1)
                seguro_vida_id = st.number_input("ID Seguro Vida (opcional):", min_value=0, step=1)
                corretor_id = st.number_input("ID Corretor:", min_value=1, step=1)
                nome_plano = st.text_input("Nome do Plano:")
                
            with col2:
                valor_parcela = st.number_input("Valor da Parcela:", min_value=0.0, format="%.2f")
                num_parcela = st.number_input("Número da Parcela Atual:", min_value=0, step=1)
                reebolso_fraquia_max = st.text_input("Reembolso Franquia Max:")
                data_proposta = st.date_input("Data da Proposta:", value=datetime.date.today())
                forma_pagamento = st.selectbox("Forma de Pagamento:", ["Cartão", "Boleto", "Pix"])
                numero_de_parcelas = st.number_input("Número Total de Parcelas:", min_value=1, step=1, value=12)
                vigencia_inicio = st.date_input("Início da Vigência:", value=datetime.date.today())
                vigencia_fim = st.date_input("Fim da Vigência:", value=datetime.date.today() + datetime.timedelta(days=365))

            with col3:
                valor_total_pago = st.number_input("Valor Total Pago:", min_value=0.0, format="%.2f")
                cobertura_limite = st.number_input("Limite da Cobertura:", min_value=0.0, format="%.2f")
                cobertura_premio = st.number_input("Prêmio da Cobertura:", min_value=0.0, format="%.2f")
                valor_total_liquido = st.number_input("Valor Líquido Total:", min_value=0.0, format="%.2f")
                valor_iof = st.number_input("Valor IOF:", min_value=0.0, format="%.2f")
                status_aprovacao = st.checkbox("Proposta Aprovada?")
                numero_apolice = st.checkbox("Número da Apólice Gerado?")

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                proposta = PropostaSeguro(
                    None, usuario_id, endereco_id, 
                    seguro_auto_id or None, seguro_residencial_id or None, 
                    seguro_empresarial_id or None, seguro_vida_id or None, 
                    corretor_id, nome_plano, valor_parcela, num_parcela, 
                    reebolso_fraquia_max, data_proposta, forma_pagamento, 
                    numero_de_parcelas, status_aprovacao, numero_apolice, 
                    vigencia_inicio, vigencia_fim, valor_total_pago, 
                    cobertura_limite, cobertura_premio, valor_total_liquido, valor_iof
                )
                propostaController.incluirPropostaSeguro(proposta)
                st.success("Proposta incluída com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Propostas de Seguro")
        dados = propostaController.consultarPropostasSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df)
        else:
            st.info("Nenhuma proposta cadastrada.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Proposta de Seguro")
        dados = propostaController.consultarPropostasSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df)
            
            proposta_id = st.number_input("ID da Proposta para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    propostaController.excluirPropostaSeguro(proposta_id)
                    st.success("Proposta excluída com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhuma proposta cadastrada.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Proposta de Seguro")
        dados = propostaController.consultarPropostasSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df)
            
            proposta_id = st.number_input("ID da Proposta para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['propostas_seguro_id'] == proposta_id), None)

            if item:
                with st.form(key="alterar_proposta"):
                    col1, col2, col3 = st.columns(3)
                    def parse_date(date_str, default=datetime.date.today()):
                        if not date_str:
                            return default
                        try:
                            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                        except (ValueError, TypeError):
                            return default

                    with col1:
                        usuario_id = st.number_input("ID Usuário:", min_value=1, step=1, value=item['usuario_id'])
                        endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])
                        seguro_auto_id = st.number_input("ID Seguro Auto (opcional):", min_value=0, step=1, value=item['seguro_auto_id'] or 0)
                        seguro_residencial_id = st.number_input("ID Seguro Residencial (opcional):", min_value=0, step=1, value=item['seguro_residencial_id'] or 0)
                        seguro_empresarial_id = st.number_input("ID Seguro Empresarial (opcional):", min_value=0, step=1, value=item['seguro_empresarial_id'] or 0)
                        seguro_vida_id = st.number_input("ID Seguro Vida (opcional):", min_value=0, step=1, value=item['seguro_vida_id'] or 0)
                        corretor_id = st.number_input("ID Corretor:", min_value=1, step=1, value=item['corretor_id'])
                        nome_plano = st.text_input("Nome do Plano:", value=item['nome_plano'])
                        
                    with col2:
                        valor_parcela = st.number_input("Valor da Parcela:", min_value=0.0, format="%.2f", value=item['valor_parcela'])
                        num_parcela = st.number_input("Número da Parcela Atual:", min_value=0, step=1, value=item['num_parcela'])
                        reebolso_fraquia_max = st.text_input("Reembolso Franquia Max:", value=item['reebolso_fraquia_max'])
                        data_proposta = st.date_input("Data da Proposta:", value=parse_date(item['data_proposta']))
                        forma_pagamento = st.selectbox("Forma de Pagamento:", ["Cartão", "Boleto", "Pix"], index=["Cartão", "Boleto", "Pix"].index(item['forma_pagamento'] or "Pix"))
                        numero_de_parcelas = st.number_input("Número Total de Parcelas:", min_value=1, step=1, value=item['numero_de_parcelas'])
                        vigencia_inicio = st.date_input("Início da Vigência:", value=parse_date(item['vigencia_inicio']))
                        vigencia_fim = st.date_input("Fim da Vigência:", value=parse_date(item['vigencia_fim']))

                    with col3:
                        valor_total_pago = st.number_input("Valor Total Pago:", min_value=0.0, format="%.2f", value=item['valor_total_pago'])
                        cobertura_limite = st.number_input("Limite da Cobertura:", min_value=0.0, format="%.2f", value=item['cobertura_limite'])
                        cobertura_premio = st.number_input("Prêmio da Cobertura:", min_value=0.0, format="%.2f", value=item['cobertura_premio'])
                        valor_total_liquido = st.number_input("Valor Líquido Total:", min_value=0.0, format="%.2f", value=item['valor_total_liquido'])
                        valor_iof = st.number_input("Valor IOF:", min_value=0.0, format="%.2f", value=item['valor_iof'])
                        status_aprovacao = st.checkbox("Proposta Aprovada?", value=bool(item['status_aprovacao']))
                        numero_apolice = st.checkbox("Número da Apólice Gerado?", value=bool(item['numero_apolice']))

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        proposta = PropostaSeguro(
                            proposta_id, usuario_id, endereco_id, 
                            seguro_auto_id or None, seguro_residencial_id or None, 
                            seguro_empresarial_id or None, seguro_vida_id or None, 
                            corretor_id, nome_plano, valor_parcela, num_parcela, 
                            reebolso_fraquia_max, data_proposta, forma_pagamento, 
                            numero_de_parcelas, status_aprovacao, numero_apolice, 
                            vigencia_inicio, vigencia_fim, valor_total_pago, 
                            cobertura_limite, cobertura_premio, valor_total_liquido, valor_iof
                        )
                        propostaController.alterarPropostaSeguro(proposta)
                        st.success("Proposta alterada com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhuma proposta selecionada com o ID fornecido.")
        else:
            st.info("Nenhuma proposta cadastrada.")