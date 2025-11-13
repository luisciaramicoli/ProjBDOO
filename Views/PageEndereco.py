import streamlit as st
import pandas as pd
import Controllers.EnderecoController as enderecoController
from Models.Endereco import Endereco

def show_endereco_page():
    st.title('Cadastro de Endereços')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Endereço")
        with st.form(key="incluir_endereco"):
            cep = st.text_input("CEP (apenas números):", max_chars=8)
            logradouro = st.text_input("Logradouro:")
            numero = st.text_input("Número:")
            complemento = st.text_input("Complemento (opcional):")
            bairro = st.text_input("Bairro:")
            cidade = st.text_input("Cidade:")
            estado = st.text_input("Estado (UF):", max_chars=2)

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                endereco = Endereco(None, cep, logradouro, numero, complemento or None, bairro, cidade, estado)
                enderecoController.incluirEndereco(endereco)
                st.success("Endereço incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Endereços")
        dados = enderecoController.consultarEnderecos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum endereço cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Endereço")
        dados = enderecoController.consultarEnderecos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            endereco_id = st.number_input("ID do Endereço para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    enderecoController.excluirEndereco(endereco_id)
                    st.success("Endereço excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum endereço cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Endereço")
        dados = enderecoController.consultarEnderecos()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            endereco_id = st.number_input("ID do Endereço para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['endereco_id'] == endereco_id), None)

            if item:
                with st.form(key="alterar_endereco"):
                    cep = st.text_input("CEP:", value=item['cep'], max_chars=8)
                    logradouro = st.text_input("Logradouro:", value=item['logradouro'])
                    numero = st.text_input("Número:", value=item['numero'])
                    complemento = st.text_input("Complemento:", value=item['complemento'] or "")
                    bairro = st.text_input("Bairro:", value=item['bairro'])
                    cidade = st.text_input("Cidade:", value=item['cidade'])
                    estado = st.text_input("Estado (UF):", value=item['estado'], max_chars=2)

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        endereco = Endereco(endereco_id, cep, logradouro, numero, complemento or None, bairro, cidade, estado)
                        enderecoController.alterarEndereco(endereco)
                        st.success("Endereço alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum endereço selecionado com o ID fornecido.")
        else:
            st.info("Nenhum endereço cadastrado.")