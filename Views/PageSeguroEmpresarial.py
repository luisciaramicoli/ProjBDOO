import streamlit as st
import pandas as pd
import Controllers.SeguroEmpresarialController as seguroEmpresarialController
from Models.SeguroEmpresarial import SeguroEmpresarial

def show_seguro_empresarial_page():
    st.title('Cadastro de Seguros Empresariais')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Seguro Empresarial")
        with st.form(key="incluir_seguro_empresarial"):
            atividade = st.text_input("Atividade (Ex: Comércio, Indústria):")
            endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                seguro = SeguroEmpresarial(None, atividade, endereco_id)
                seguroEmpresarialController.incluirSeguroEmpresarial(seguro)
                st.success("Seguro Empresarial incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Seguros Empresariais")
        dados = seguroEmpresarialController.consultarSegurosEmpresariais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum Seguro Empresarial cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Seguro Empresarial")
        dados = seguroEmpresarialController.consultarSegurosEmpresariais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Empresarial para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    seguroEmpresarialController.excluirSeguroEmpresarial(seguro_id)
                    st.success("Seguro Empresarial excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum Seguro Empresarial cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Seguro Empresarial")
        dados = seguroEmpresarialController.consultarSegurosEmpresariais()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Empresarial para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['seguro_empresarial_id'] == seguro_id), None)

            if item:
                with st.form(key="alterar_seguro_empresarial"):
                    atividade = st.text_input("Atividade:", value=item['atividade'])
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        seguro = SeguroEmpresarial(seguro_id, atividade, endereco_id)
                        seguroEmpresarialController.alterarSeguroEmpresarial(seguro)
                        st.success("Seguro Empresarial alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum Seguro Empresarial selecionado com o ID fornecido.")
        else:
            st.info("Nenhum Seguro Empresarial cadastrado.")