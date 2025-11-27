import streamlit as st
import pandas as pd
import Controllers.UsuarioController as usuarioController
from Models.Usuario import Usuario
import datetime

def show_usuario_page():
    st.title('Cadastro de Usuários')

    menu_op = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if menu_op == "Incluir":
        st.subheader("Incluir Usuário")
        with st.form(key="incluir_usuario"):
            nome = st.text_input("Nome:")
            cpf = st.text_input("CPF (apenas números):", max_chars=11)
            data_nascimento = st.date_input("Data de Nascimento:", value=datetime.date(2000, 1, 1))
            telefone = st.text_input("Telefone (apenas números):", max_chars=10)
            email = st.text_input("Email:")
            senha = st.text_input("Senha:", type="password")
            endereco_id = st.number_input("ID Endereço:", min_value=1, step=1)
            reset_token = st.text_input("Reset Token (opcional):")
            reset_token_expiracao = st.date_input("Expiração Token (opcional):", value=None)
            tus_code = st.number_input("TUS Code:", min_value=0, step=1)
            nome_social = st.text_input("Nome Social (opcional):")

            submit_button = st.form_submit_button(label='Incluir')

            if submit_button:
                token_exp = reset_token_expiracao if reset_token_expiracao else None
                token = reset_token if reset_token else None
                social = nome_social if nome_social else None

                usuario = Usuario(None, nome, cpf, data_nascimento, telefone, email, senha, 
                                  endereco_id, token, token_exp, tus_code, social)
                usuarioController.incluirUsuario(usuario)
                st.success("Usuário incluído com sucesso!")

    elif menu_op == "Consultar":
        st.subheader("Consultar Usuários")
        dados = usuarioController.consultarUsuarios()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
        else:
            st.info("Nenhum usuário cadastrado.")

    elif menu_op == "Excluir":
        st.subheader("Excluir Usuário")
        dados = usuarioController.consultarUsuarios()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            usuario_id = st.number_input("ID do Usuário para excluir:", min_value=1, step=1)
            if st.button("Excluir"):
                try:
                    usuarioController.excluirUsuario(usuario_id)
                    st.success("Usuário excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir: {e}")
        else:
            st.info("Nenhum usuário cadastrado.")

    elif menu_op == "Alterar":
        st.subheader("Alterar Usuário")
        dados = usuarioController.consultarUsuarios()
        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df, width=1000)
            
            usuario_id = st.number_input("ID do Usuário para alterar:", min_value=1, step=1)
            item = next((d for d in dados if d['usuario_id'] == usuario_id), None)

            if item:
                with st.form(key="alterar_usuario"):
                    nome = st.text_input("Nome:", value=item['nome'])
                    cpf = st.text_input("CPF:", value=item['cpf'], max_chars=11)
                    
                    data_nasc_val = datetime.date.today() if not item['data_nascimento'] else datetime.datetime.strptime(item['data_nascimento'], '%Y-%m-%d').date()
                    data_nascimento = st.date_input("Data de Nascimento:", value=data_nasc_val)
                    
                    telefone = st.text_input("Telefone:", value=item['telefone'], max_chars=10)
                    email = st.text_input("Email:", value=item['email'])
                    senha = st.text_input("Nova Senha (deixe em branco para manter):", type="password")
                    endereco_id = st.number_input("ID Endereço:", min_value=1, step=1, value=item['endereco_id'])
                    
                    reset_token = st.text_input("Reset Token:", value=item['reset_token'] or "")
                    
                    data_exp_val = None if not item['reset_token_expiracao'] else datetime.datetime.strptime(item['reset_token_expiracao'], '%Y-%m-%d').date()
                    reset_token_expiracao = st.date_input("Expiração Token:", value=data_exp_val)

                    tus_code = st.number_input("TUS Code:", min_value=0, step=1, value=item['tus_code'])
                    nome_social = st.text_input("Nome Social:", value=item['nome_social'] or "")

                    submit_button = st.form_submit_button(label='Alterar')

                    if submit_button:
                        senha_final = senha if senha else item['senha']
                        
                        usuario = Usuario(usuario_id, nome, cpf, data_nascimento, telefone, email, senha_final, 
                                          endereco_id, reset_token or None, reset_token_expiracao or None, 
                                          tus_code, nome_social or None)
                        usuarioController.alterarUsuario(usuario)
                        st.success("Usuário alterado com sucesso!")
                        st.rerun()
            else:
                st.warning("Nenhum usuário selecionado com o ID fornecido.")
        else:
            st.info("Nenhum usuário cadastrado.")