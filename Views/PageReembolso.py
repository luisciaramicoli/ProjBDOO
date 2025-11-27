import streamlit as st
import pandas as pd
import Controllers.ReembolsoController as reembolsoController
from Models.Reembolso import Reembolso

def show_reembolso_page():
    st.title('Cadastro de Reembolsos')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Reembolso")
        with st.form(key="incluir_reembolso"):
            seguro_auto = st.text_input("ID Seguro Auto (referência):")
            planos_de_seguro = st.text_input("ID Plano de Seguro (referência):")
            valor = st.number_input("Valor do Reembolso:", min_value=0.0, format="%.2f")

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                reembolso = Reembolso(None, seguro_auto, planos_de_seguro, valor)
                reembolsoController.incluirReembolso(reembolso)
                st.success("Reembolso incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Reembolsos")
        dados = reembolsoController.consultarReembolsos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum reembolso cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Reembolso")
        dados = reembolsoController.consultarReembolsos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            reembolso_id = st.number_input("ID do Reembolso para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    reembolsoController.excluirReembolso(reembolso_id)
                    st.success("Reembolso excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum reembolso cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Reembolso")
        dados = reembolsoController.consultarReembolsos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            reembolso_id = st.number_input("ID do Reembolso para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['reembolso_id'] == reembolso_id), None)

            if item:
                with st.form(key="alterar_reembolso"):
                    seguro_auto = st.text_input("ID Seguro Auto (referência):", value=item['seguro_auto'])
                    planos_de_seguro = st.text_input("ID Plano de Seguro (referência):", value=item['planos_de_seguro'])
                    valor = st.number_input("Valor do Reembolso:", min_value=0.0, format="%.2f", value=item['valor'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        reembolso = Reembolso(reembolso_id, seguro_auto, planos_de_seguro, valor)
                        reembolsoController.alterarReembolso(reembolso)
                        st.success("Reembolso alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum reembolso selecionado com o ID fornecido.")
        else:
            st.info("Nenhum reembolso cadastrado.")
