import streamlit as st
import pandas as pd
import Controllers.ApoliceController as apoliceController
from Models.Apolice import Apolice

def show_apolice_page():
    st.title('Cadastro de Apólices')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Apólice")
        with st.form(key="incluir_apolice"):
            proposta_id = st.number_input("ID da Proposta (vincular):", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                apolice = Apolice(None, proposta_id)
                apoliceController.incluirApolice(apolice)
                st.success("Apólice incluída com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Apólices")
        dados = apoliceController.consultarApolices()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhuma apólice cadastrada.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Apólice")
        dados = apoliceController.consultarApolices()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            apolice_id = st.number_input("ID da Apólice para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    apoliceController.excluirApolice(apolice_id)
                    st.success("Apólice excluída com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhuma apólice cadastrada.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Apólice")
        dados = apoliceController.consultarApolices()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            apolice_id = st.number_input("ID da Apólice para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['apolice_id'] == apolice_id), None)

            if item:
                with st.form(key="alterar_apolice"):
                    proposta_id = st.number_input("ID da Proposta:", min_value=1, step=1, value=item['proposta_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        apolice = Apolice(apolice_id, proposta_id)
                        apoliceController.alterarApolice(apolice)
                        st.success("Apólice alterada com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhuma apólice selecionada com o ID fornecido.")
        else:
            st.info("Nenhuma apólice cadastrada.")