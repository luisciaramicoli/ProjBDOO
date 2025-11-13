import streamlit as st
import pandas as pd
import Controllers.CorretorController as corretorController
from Models.Corretor import Corretor

def show_corretor_page():
    st.title('Cadastro de Corretores')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Corretor")
        with st.form(key="incluir_corretor"):
            nome_corretor = st.text_input("Nome do Corretor:")
            cnpj = st.text_input("CNPJ (apenas números):", max_chars=14)
            endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                corretor = Corretor(None, nome_corretor, cnpj, endereco_id)
                corretorController.incluirCorretor(corretor)
                st.success("Corretor incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Corretores")
        dados = corretorController.consultarCorretores()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum corretor cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Corretor")
        dados = corretorController.consultarCorretores()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            corretor_id = st.number_input("ID do Corretor para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    corretorController.excluirCorretor(corretor_id)
                    st.success("Corretor excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum corretor cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Corretor")
        dados = corretorController.consultarCorretores()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            corretor_id = st.number_input("ID do Corretor para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['id_corretor'] == corretor_id), None)

            if item:
                with st.form(key="alterar_corretor"):
                    nome_corretor = st.text_input("Nome do Corretor:", value=item['nome_corretor'])
                    cnpj = st.text_input("CNPJ:", value=item['cnpj'], max_chars=14)
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        corretor = Corretor(corretor_id, nome_corretor, cnpj, endereco_id)
                        corretorController.alterarCorretor(corretor)
                        st.success("Corretor alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum corretor selecionado com o ID fornecido.")
        else:
            st.info("Nenhum corretor cadastrado.")