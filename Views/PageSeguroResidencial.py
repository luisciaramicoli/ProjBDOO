import streamlit as st
import pandas as pd
import Controllers.SeguroResidencialController as seguroResidencialController
from Models.SeguroResidencial import SeguroResidencial

def show_seguro_residencial_page():
    st.title('Cadastro de Seguros Residenciais')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Seguro Residencial")
        with st.form(key="incluir_seguro_residencial"):
            tipo = st.text_input("Tipo (Ex: Apartamento, Casa):")
            endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                seguro = SeguroResidencial(None, tipo, endereco_id)
                seguroResidencialController.incluirSeguroResidencial(seguro)
                st.success("Seguro Residencial incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Seguros Residenciais")
        dados = seguroResidencialController.consultarSegurosResidenciais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum Seguro Residencial cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Seguro Residencial")
        dados = seguroResidencialController.consultarSegurosResidenciais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Residencial para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    seguroResidencialController.excluirSeguroResidencial(seguro_id)
                    st.success("Seguro Residencial excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum Seguro Residencial cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Seguro Residencial")
        dados = seguroResidencialController.consultarSegurosResidenciais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Residencial para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['seguro_residencial_id'] == seguro_id), None)

            if item:
                with st.form(key="alterar_seguro_residencial"):
                    tipo = st.text_input("Tipo:", value=item['tipo'])
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        seguro = SeguroResidencial(seguro_id, tipo, endereco_id)
                        seguroResidencialController.alterarSeguroResidencial(seguro)
                        st.success("Seguro Residencial alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum Seguro Residencial selecionado com o ID fornecido.")
        else:
            st.info("Nenhum Seguro Residencial cadastrado.")