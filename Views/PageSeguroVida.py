import streamlit as st
import pandas as pd
import Controllers.SeguroVidaController as seguroVidaController
from Models.SeguroVida import SeguroVida

def show_seguro_vida_page():
    st.title('Cadastro de Seguros de Vida')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Seguro de Vida")
        with st.form(key="incluir_seguro_vida"):
            atividade = st.text_input("Atividade (Profissão/Risco):")
            endereco_id = st.number_input("ID Endereço (para correspondência):", min_value=1, step=1)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                seguro = SeguroVida(None, atividade, endereco_id)
                seguroVidaController.incluirSeguroVida(seguro)
                st.success("Seguro de Vida incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Seguros de Vida")
        dados = seguroVidaController.consultarSegurosVida()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum Seguro de Vida cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Seguro de Vida")
        dados = seguroVidaController.consultarSegurosVida()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro de Vida para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    seguroVidaController.excluirSeguroVida(seguro_id)
                    st.success("Seguro de Vida excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum Seguro de Vida cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Seguro de Vida")
        dados = seguroVidaController.consultarSegurosVida()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            seguro_id = st.number_input("ID do Seguro de Vida para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['seguro_vida_id'] == seguro_id), None)

            if item:
                with st.form(key="alterar_seguro_vida"):
                    atividade = st.text_input("Atividade:", value=item['atividade'])
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        seguro = SeguroVida(seguro_id, atividade, endereco_id)
                        seguroVidaController.alterarSeguroVida(seguro)
                        st.success("Seguro de Vida alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum Seguro de Vida selecionado com o ID fornecido.")
        else:
            st.info("Nenhum Seguro de Vida cadastrado.")