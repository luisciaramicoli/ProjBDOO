import streamlit as st
import sys
from pathlib import Path
import importlib
import Controllers.UsuarioController as usuarioController
import Controllers.EnderecoController as enderecoController
import Controllers.PropostaSeguroController as propostaController
import Controllers.PlanoSeguroController as planoController
import Controllers.SeguroAutoController as autoController
import Controllers.SeguroResidencialController as residencialController
import Controllers.SeguroEmpresarialController as empresarialController
import Controllers.SeguroVidaController as vidaController
import Controllers.CorretorController as corretorController
from Models.Usuario import Usuario
from Models.Endereco import Endereco
from Models.PropostaSeguro import PropostaSeguro
from Models.SeguroAuto import SeguroAuto
from Models.SeguroResidencial import SeguroResidencial
from Models.SeguroEmpresarial import SeguroEmpresarial
from Models.SeguroVida import SeguroVida
import datetime
import pandas as pd
from styles import apply_styles

# 1. Configuração ABSOLUTA PRIMEIRO
st.set_page_config(
    page_title="Sistema de Seguros",
    layout="wide",
    initial_sidebar_state="auto"
)

# Aplicar estilos profissionais
st.markdown(apply_styles(), unsafe_allow_html=True)

# 2. Configuração de imports DEPOIS da configuração
sys.path.append(str(Path(__file__).parent))

# 3. Dicionário de páginas disponíveis para o Admin
PAGES_ADMIN = {
    "Usuários": ("Views.PageUsuario", "show_usuario_page"),
    "Endereços": ("Views.PageEndereco", "show_endereco_page"),
    "Seguros Auto": ("Views.PageSeguroAuto", "show_seguro_auto_page"),
    "Seguros Residenciais": ("Views.PageSeguroResidencial", "show_seguro_residencial_page"),
    "Seguros Empresariais": ("Views.PageSeguroEmpresarial", "show_seguro_empresarial_page"),
    "Seguros de Vida": ("Views.PageSeguroVida", "show_seguro_vida_page"),
    "Corretores": ("Views.PageCorretor", "show_corretor_page"),
    "Planos de Seguro": ("Views.PagePlanoSeguro", "show_plano_seguro_page"),
    "Reembolsos": ("Views.PageReembolso", "show_reembolso_page"),
    "Propostas de Seguro": ("Views.PagePropostaSeguro", "show_proposta_seguro_page"),
    "Apólices": ("Views.PageApolice", "show_apolice_page")
}

# 4. Dicionário de páginas disponíveis para o Cliente
PAGES_CLIENT = {
    "Minhas Propostas": "show_client_propostas",
    "Solicitar Proposta": "show_solicitar_proposta",
    "Meus Dados": "show_client_meus_dados"
}

# 5. Função para carregar páginas de forma dinâmica (ADMIN)
def load_admin_page(page_name):
    """Carrega um módulo de página de admin dinamicamente"""
    try:
        module_path, func_name = PAGES_ADMIN[page_name]
        module = importlib.import_module(module_path)
        return getattr(module, func_name)
        
    except (ImportError, AttributeError, KeyError) as e:
        st.error(f"Erro ao carregar a página {page_name}: {e}")
        st.warning("Verifique o dicionário PAGES_ADMIN no main.py e os nomes das funções nas Views.")
        return None

# ===============================================
# 6. FUNÇÕES DO PORTAL DO CLIENTE
# ===============================================

def get_current_user_data():
    """Busca e armazena em cache os dados do usuário logado."""
    user_data = usuarioController.consultarUsuarioPorEmail(st.session_state['user_email'])
    if not user_data:
        st.error("Não foi possível carregar seus dados. Por favor, faça login novamente.")
        st.session_state.clear()
        st.rerun()
        return None, None
    
    usuario_id = user_data['usuario_id']
    endereco_id = user_data.get('endereco_id')
    return usuario_id, endereco_id, user_data

def show_client_propostas():
    """Exibe as propostas de seguro do cliente logado."""
    st.header("Minhas Propostas de Seguro")
    
    usuario_id, _, _ = get_current_user_data()
    if not usuario_id:
        return

    propostas = propostaController.consultarPropostasPorUsuarioId(usuario_id)
    
    if propostas:
        df = pd.DataFrame(propostas)
        st.dataframe(df)
        
        st.subheader("Detalhes da Proposta")
        proposta_selecionada_id = st.selectbox(
            "Selecione uma proposta para ver os detalhes:", 
            options=[p['propostas_seguro_id'] for p in propostas], 
            format_func=lambda x: f"Proposta ID: {x}"
        )
        
        proposta_detalhe = next((p for p in propostas if p['propostas_seguro_id'] == proposta_selecionada_id), None)
        
        if proposta_detalhe:
            status = "Aprovada" if proposta_detalhe['status_aprovacao'] else "Em Análise"
            st.write(f"**Plano:** {proposta_detalhe['nome_plano']}")
            st.write(f"**Status:** {status}")
            st.write(f"**Valor da Parcela:** R$ {proposta_detalhe['valor_parcela']:.2f}")
            st.write(f"**Vigência:** {proposta_detalhe['vigencia_inicio']} a {proposta_detalhe['vigencia_fim']}")
    else:
        st.info("Você ainda não possui nenhuma proposta de seguro.")

def show_solicitar_proposta():
    """Formulário para o cliente solicitar uma nova proposta."""
    st.header("Solicitar Nova Proposta de Seguro")

    usuario_id, endereco_id, user_data = get_current_user_data()
    if not usuario_id:
        return
    
    # Etapa 1: Verificar Endereço
    if not endereco_id:
        st.warning("Você precisa cadastrar um endereço em 'Meus Dados' antes de solicitar uma proposta.")
        return

    # Carregar planos de seguro disponíveis
    planos_disponiveis = planoController.consultarPlanosSeguro()
    if not planos_disponiveis:
        st.error("Não há planos de seguro disponíveis no momento. Tente mais tarde.")
        return

    planos_opcoes = {f"{plano['nome_plano']} (R$ {plano['valor_parcela']:.2f}/mês)": plano['nome_plano_id'] for plano in planos_disponiveis}
    
    with st.form(key="solicitar_proposta_form"):
        st.subheader("1. Escolha o Tipo de Seguro")
        tipo_seguro = st.selectbox("Tipo de Seguro:", ["Seguro Auto", "Seguro Residencial", "Seguro Empresarial", "Seguro de Vida"])
        
        st.divider()
        st.subheader("2. Detalhes do Objeto Segurado")
        
        # Campos dinâmicos
        seguro_auto_id, seguro_residencial_id, seguro_empresarial_id, seguro_vida_id = None, None, None, None
        
        if tipo_seguro == "Seguro Auto":
            placa = st.text_input("Placa do Veículo:", max_chars=7)
            modelo = st.text_input("Modelo do Veículo (Ex: Toyota Corolla):")
            ano = st.number_input("Ano do Veículo:", min_value=1950, max_value=datetime.date.today().year + 1, value=datetime.date.today().year)
            
        elif tipo_seguro == "Seguro Residencial":
            tipo_residencia = st.selectbox("Tipo de Residência:", ["Casa", "Apartamento", "Casa em Condomínio"])
            
        elif tipo_seguro == "Seguro Empresarial":
            atividade = st.text_input("Atividade da Empresa (Ex: Comércio Varejista):")

        elif tipo_seguro == "Seguro de Vida":
            atividade = st.text_input("Sua Profissão Principal:")

        st.divider()
        st.subheader("3. Escolha o Plano")
        
        plano_selecionado_str = st.selectbox("Planos Disponíveis:", list(planos_opcoes.keys()))
        plano_id_selecionado = planos_opcoes[plano_selecionado_str]
        
        plano_obj = planoController.consultarPlanoPorId(plano_id_selecionado)
        if plano_obj:
            st.write(f"**Detalhes do Plano:** {plano_obj['detalhes']}")
            st.write(f"**Valor Total Anual:** R$ {plano_obj['valor_total']:.2f}")

        submit_button = st.form_submit_button("Enviar Solicitação")

        if submit_button:
            try:
                # 1. Criar o objeto de seguro específico e obter o ID
                if tipo_seguro == "Seguro Auto":
                    if not placa or not modelo or not ano:
                        st.error("Para Seguro Auto, preencha Placa, Modelo e Ano.")
                        return
                    seguro = SeguroAuto(None, placa, modelo, ano, endereco_id)
                    seguro_auto_id = autoController.incluirSeguroAuto(seguro)
                
                elif tipo_seguro == "Seguro Residencial":
                    seguro = SeguroResidencial(None, tipo_residencia, endereco_id)
                    seguro_residencial_id = residencialController.incluirSeguroResidencial(seguro)
                
                elif tipo_seguro == "Seguro Empresarial":
                    if not atividade:
                        st.error("Para Seguro Empresarial, preencha a Atividade.")
                        return
                    seguro = SeguroEmpresarial(None, atividade, endereco_id)
                    seguro_empresarial_id = empresarialController.incluirSeguroEmpresarial(seguro)
                
                elif tipo_seguro == "Seguro de Vida":
                    if not atividade:
                        st.error("Para Seguro de Vida, preencha sua Profissão.")
                        return
                    # Usamos o endereço do usuário para correspondência
                    seguro = SeguroVida(None, atividade, endereco_id) 
                    seguro_vida_id = vidaController.incluirSeguroVida(seguro)
                
                # 2. Obter um corretor válido
                corretores_lista = corretorController.consultarCorretores()
                if not corretores_lista:
                    st.error("Erro interno: Nenhum corretor disponível para processar a proposta.")
                    return
                
                # Seleciona o primeiro corretor disponível (pode ser aprimorado com lógica de distribuição)
                corretor_id_selecionado = corretores_lista[0]['id_corretor']

                # 3. Criar a Proposta de Seguro
                hoje = datetime.date.today()
                proposta = PropostaSeguro(
                    None, 
                    usuario_id=usuario_id, 
                    endereco_id=endereco_id, 
                    seguro_auto_id=seguro_auto_id, 
                    seguro_residencial_id=seguro_residencial_id, 
                    seguro_empresarial_id=seguro_empresarial_id, 
                    seguro_vida_id=seguro_vida_id, 
                    corretor_id=corretor_id_selecionado, 
                    nome_plano=plano_obj['nome_plano'], 
                    valor_parcela=plano_obj['valor_parcela'], 
                    num_parcela=0, 
                    reebolso_fraquia_max=None, 
                    data_proposta=hoje, 
                    forma_pagamento="Aguardando", 
                    numero_de_parcelas=12, 
                    status_aprovacao=False, # Começa como "Em Análise"
                    numero_apolice=False, 
                    vigencia_inicio=hoje, 
                    vigencia_fim=hoje + datetime.timedelta(days=365), 
                    valor_total_pago=0.0, 
                    cobertura_limite=plano_obj['valor_total'], # Exemplo
                    cobertura_premio=0.0, 
                    valor_total_liquido=plano_obj['valor_total'], 
                    valor_iof=plano_obj['valor_total'] * 0.0738 # Exemplo IOF 7.38%
                )
                
                novo_id_proposta = propostaController.incluirPropostaSeguro(proposta)
                if novo_id_proposta:
                    st.success("Proposta enviada com sucesso! Você pode acompanhá-la em 'Minhas Propostas'.")
                else:
                    st.error("Erro ao registrar a proposta. Verifique os dados e tente novamente.")

            except Exception as e:
                st.error(f"Erro ao criar proposta: {e}")


def show_client_meus_dados():
    """Permite ao cliente visualizar e alterar seus dados cadastrais."""
    st.header("Meus Dados Cadastrais")
    
    usuario_id, endereco_id, user_data = get_current_user_data()
    if not usuario_id:
        return
    
    endereco_data = None
    if endereco_id:
        endereco_data = enderecoController.consultarEnderecoPorId(endereco_id)

    with st.form(key="meus_dados_form"):
        st.subheader("Dados Pessoais")
        
        # Converte a data de string para objeto date
        data_nasc_val = datetime.date.today()
        if user_data['data_nascimento']:
            try:
                data_nasc_val = datetime.datetime.strptime(user_data['data_nascimento'], '%Y-%m-%d').date()
            except ValueError:
                pass 

        nome = st.text_input("Nome:", value=user_data['nome'])
        cpf = st.text_input("CPF:", value=user_data['cpf'], disabled=True) 
        email = st.text_input("Email:", value=user_data['email'], disabled=True) 
        data_nascimento = st.date_input("Data de Nascimento:", value=data_nasc_val)
        telefone = st.text_input("Telefone:", value=user_data['telefone'])
        nome_social = st.text_input("Nome Social (opcional):", value=user_data.get('nome_social') or "")

        st.divider()
        st.subheader("Endereço")
        
        if endereco_data:
            cep = st.text_input("CEP:", value=endereco_data['cep'], max_chars=8)
            logradouro = st.text_input("Logradouro:", value=endereco_data['logradouro'])
            numero = st.text_input("Número:", value=endereco_data['numero'])
            complemento = st.text_input("Complemento (opcional):", value=endereco_data.get('complemento') or "")
            bairro = st.text_input("Bairro:", value=endereco_data['bairro'])
            cidade = st.text_input("Cidade:", value=endereco_data['cidade'])
            estado = st.text_input("Estado (UF):", value=endereco_data['estado'], max_chars=2)
        else:
            st.info("Você ainda não possui um endereço cadastrado.")
            cep = st.text_input("CEP:", max_chars=8)
            logradouro = st.text_input("Logradouro:")
            numero = st.text_input("Número:")
            complemento = st.text_input("Complemento (opcional):")
            bairro = st.text_input("Bairro:")
            cidade = st.text_input("Cidade:")
            estado = st.text_input("Estado (UF):", max_chars=2)

        st.divider()
        st.subheader("Segurança")
        senha_atual = st.text_input("Senha Atual (obrigatório para salvar):", type="password")
        nova_senha = st.text_input("Nova Senha (deixe em branco para não alterar):", type="password")
        
        submit_button = st.form_submit_button("Salvar Alterações")

        if submit_button:
            # 1. Verificar senha atual
            sucesso_login, _ = usuarioController.checarLogin(user_data['email'], senha_atual)
            if not sucesso_login:
                st.error("Senha atual incorreta. As alterações não foram salvas.")
                return

            # 2. Determinar a senha final
            senha_final = nova_senha if nova_senha else senha_atual

            # 3. Salvar ou Atualizar Endereço
            novo_endereco_id = endereco_id
            if not cep or not logradouro or not numero or not bairro or not cidade or not estado:
                st.warning("Para salvar um endereço, todos os campos (exceto complemento) são obrigatórios.")
            else:
                endereco_obj = Endereco(
                    endereco_id, cep, logradouro, numero, complemento or None, bairro, cidade, estado
                )
                if endereco_data:
                    enderecoController.alterarEndereco(endereco_obj)
                    novo_endereco_id = endereco_id
                else:
                    novo_endereco_id = enderecoController.incluirEndereco(endereco_obj)
                    if novo_endereco_id:
                        st.success(f"Novo endereço cadastrado com ID: {novo_endereco_id}")
                    else:
                        st.error("Falha ao cadastrar novo endereço.")
                        return # Não continua se falhar ao criar endereço

            # 4. Salvar Usuário
            usuario_obj = Usuario(
                usuario_id, nome, user_data['cpf'], data_nascimento, telefone, user_data['email'],
                senha_final, novo_endereco_id, user_data['reset_token'], 
                user_data['reset_token_expiracao'], user_data['tus_code'], nome_social or None
            )
            
            usuarioController.alterarUsuario(usuario_obj)
            st.success("Dados atualizados com sucesso!")
            st.rerun()


# ===============================================
# 7. FUNÇÕES PRINCIPAIS DA APLICAÇÃO
# ===============================================

def show_login_page():
    """Exibe a tela de login e cadastro."""
    st.title("Sistema de Gerenciamento de Seguros")

    login_tab, signup_tab = st.tabs(["Login", "Cadastre-se"])

    with login_tab:
        st.subheader("Login")
        with st.form(key="login_form"):
            email = st.text_input("Email:")
            senha = st.text_input("Senha:", type="password")
            submit_button = st.form_submit_button("Entrar")

            if submit_button:
                sucesso, tus_code = usuarioController.checarLogin(email, senha)
                
                if sucesso:
                    st.session_state['logged_in'] = True
                    st.session_state['user_email'] = email
                    st.session_state['tus_code'] = tus_code  
                    st.success("Login bem-sucedido! Redirecionando...")
                    st.rerun() 
                else:
                    st.error("Email ou senha inválidos.")

    with signup_tab:
        st.subheader("Cadastre-se")
        with st.form(key="signup_form"):
            nome = st.text_input("Nome Completo:")
            email_novo = st.text_input("Seu Email:")
            senha_nova = st.text_input("Crie uma Senha:", type="password")
            cpf = st.text_input("CPF (apenas números):", max_chars=11)
            data_nascimento = st.date_input("Data de Nascimento:", value=datetime.date(2000, 1, 1))
            telefone = st.text_input("Telefone (apenas números):", max_chars=10)
            
            signup_button = st.form_submit_button("Cadastrar")

            if signup_button:
                if nome and email_novo and senha_nova and cpf and data_nascimento and telefone:
                    novo_usuario = Usuario(
                        None, nome, cpf, data_nascimento, telefone, email_novo, senha_nova, 
                        None, None, None, 1, None # tus_code = 1 (Cliente), sem endereço
                    )
                    try:
                        usuarioController.incluirUsuario(novo_usuario)
                        st.success("Cadastro realizado com sucesso! Você já pode fazer o login.")
                    except Exception as e:
                        st.error(f"Erro ao cadastrar (Email ou CPF podem já existir): {e}")
                else:
                    st.warning("Por favor, preencha todos os campos.")


def show_admin_app():
    """Exibe a aplicação de administração (TUS Code = 2)."""
    st.title('Painel de Administração')
    
    with st.sidebar:
        st.title("Menu de Navegação")
        st.write(f"Logado como: {st.session_state['user_email']} (Admin)")
        
        if st.button("Logout"):
            st.session_state.clear() 
            st.rerun()
            
        st.divider()
        page_selection = st.selectbox("Selecione um Cadastro", list(PAGES_ADMIN.keys()))
    
    show_page = load_admin_page(page_selection)
    
    if show_page:
        show_page()

def show_client_app():
    """Exibe a aplicação do cliente (TUS Code != 2)."""
    st.title('Portal do Cliente')
    
    with st.sidebar:
        st.title("Menu do Cliente")
        st.write(f"Bem-vindo, {st.session_state['user_email']}")
        
        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()
        
        st.divider()
        page_selection = st.selectbox("Opções", list(PAGES_CLIENT.keys()))

    if page_selection in PAGES_CLIENT:
        func_to_run = globals()[PAGES_CLIENT[page_selection]]
        func_to_run()


# 8. Função principal
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['user_email'] = ""
        st.session_state['tus_code'] = None

    if st.session_state['logged_in']:
        if st.session_state['tus_code'] == 2:
            show_admin_app()
        else:
            show_client_app()
    else:
        show_login_page()

# 9. Ponto de entrada
if __name__ == "__main__":
    # Garante que as tabelas essenciais existem
    # Em produção, isso seria feito por um script de 'migration'
    try:
        enderecoController.criarTabelaEndereco()
        usuarioController.criarTabelaUsuario()
        autoController.criarTabelaSeguroAuto()
        residencialController.criarTabelaSeguroResidencial()
        empresarialController.criarTabelaSeguroEmpresarial()
        vidaController.criarTabelaSeguroVida()
        planoController.criarTabelaPlanoSeguro()
        propostaController.criarTabelaPropostaSeguro()
    except Exception as e:
        print(f"Erro ao inicializar tabelas: {e}")

    main()