import streamlit as st
import pandas as pd
import Controllers.PlanoSeguroController as planoSeguroController
from Models.PlanoSeguro import PlanoSeguro

def show_plano_seguro_page():
    st.title('Cadastro de Planos de Seguro')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Plano de Seguro")
        with st.form(key="incluir_plano"):
            nome_plano = st.text_input("Nome do Plano:")
            valor_total = st.number_input("Valor Total:", min_value=0.0, format="%.2f")
            valor_parcela = st.number_input("Valor da Parcela:", min_value=0.0, format="%.2f")
            detalhes = st.text_area("Detalhes:")

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                plano = PlanoSeguro(None, nome_plano, valor_total, valor_parcela, detalhes)
                planoSeguroController.incluirPlanoSeguro(plano)
                st.success("Plano de Seguro incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Planos de Seguro")
        dados = planoSeguroController.consultarPlanosSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum plano cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Plano de Seguro")
        dados = planoSeguroController.consultarPlanosSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            plano_id = st.number_input("ID do Plano para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    planoSeguroController.excluirPlanoSeguro(plano_id)
                    st.success("Plano de Seguro excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum plano cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Plano de Seguro")
        dados = planoSeguroController.consultarPlanosSeguro()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            plano_id = st.number_input("ID do Plano para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['nome_plano_id'] == plano_id), None)

            if item:
                with st.form(key="alterar_plano"):
                    nome_plano = st.text_input("Nome do Plano:", value=item['nome_plano'])
                    valor_total = st.number_input("Valor Total:", min_value=0.0, format="%.2f", value=item['valor_total'])
                    valor_parcela = st.number_input("Valor da Parcela:", min_value=0.0, format="%.2f", value=item['valor_parcela'])
                    detalhes = st.text_area("Detalhes:", value=item['detalhes'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        plano = PlanoSeguro(plano_id, nome_plano, valor_total, valor_parcela, detalhes)
                        planoSeguroController.alterarPlanoSeguro(plano)
                        st.success("Plano de Seguro alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum plano selecionado com o ID fornecido.")
        else:
            st.info("Nenhum plano cadastrado.")