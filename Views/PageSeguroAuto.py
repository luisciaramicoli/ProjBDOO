import streamlit as st
import pandas as pd
import Controllers.SeguroAutoController as seguroAutoController
from Models.SeguroAuto import SeguroAuto

def show_seguro_auto_page():
    st.title('Cadastro de Seguros Auto')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Seguro Auto")
        with st.form(key="incluir_seguro_auto"):
            placa = st.text_input("Placa:", max_chars=10)
            modelo = st.text_input("Modelo:")
            ano = st.number_input("Ano:", min_value=1900, max_value=2100, step=1, value=2020)
            endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                seguro = SeguroAuto(None, placa, modelo, ano, endereco_id)
                seguroAutoController.incluirSeguroAuto(seguro)
                st.success("Seguro Auto incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Seguros Auto")
        dados = seguroAutoController.consultarSegurosAuto()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum Seguro Auto cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Seguro Auto")
        dados = seguroAutoController.consultarSegurosAuto()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Auto para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    seguroAutoController.excluirSeguroAuto(seguro_id)
                    st.success("Seguro Auto excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum Seguro Auto cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Seguro Auto")
        dados = seguroAutoController.consultarSegurosAuto()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro Auto para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['seguro_auto_id'] == seguro_id), None)

            if item:
                with st.form(key="alterar_seguro_auto"):
                    placa = st.text_input("Placa:", value=item['placa'], max_chars=10)
                    modelo = st.text_input("Modelo:", value=item['modelo'])
                    ano = st.number_input("Ano:", min_value=1900, max_value=2100, step=1, value=item['ano'])
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        seguro = SeguroAuto(seguro_id, placa, modelo, ano, endereco_id)
                        seguroAutoController.alterarSeguroAuto(seguro)
                        st.success("Seguro Auto alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum Seguro Auto selecionado com o ID fornecido.")
        else:
            st.info("Nenhum Seguro Auto cadastrado.")