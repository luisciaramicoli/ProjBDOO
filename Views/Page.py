import streamlit as st
from Views.PageUsuario import show_usuario_page
from Views.PageEndereco import show_endereco_page
from Views.PageSeguroAuto import show_seguro_auto_page
from Views.PageSeguroResidencial import show_seguro_residencial_page
from Views.PageSeguroEmpresarial import show_seguro_empresarial_page
from Views.PageSeguroVida import show_seguro_vida_page
from Views.PageCorretor import show_corretor_page
from Views.PagePlanoSeguro import show_plano_seguro_page
from Views.PageReembolso import show_reembolso_page
from Views.PagePropostaSeguro import show_proposta_seguro_page
from Views.PageApolice import show_apolice_page

# Configuração da página
st.set_page_config(layout="wide")

# Menu principal
st.sidebar.title("Menu Principal - Seguradora")
pagina = st.sidebar.selectbox("Selecione a Tabela", [
    "Usuários", 
    "Endereços", 
    "Seguros Auto",
    "Seguros Residenciais",
    "Seguros Empresariais",
    "Seguros de Vida",
    "Corretores",
    "Planos de Seguro",
    "Reembolsos",
    "Propostas de Seguro",
    "Apólices"
])

# Navegação entre as páginas
if pagina == "Usuários":
    show_usuario_page()
elif pagina == "Endereços":
    show_endereco_page()
elif pagina == "Seguros Auto":
    show_seguro_auto_page()
elif pagina == "Seguros Residenciais":
    show_seguro_residencial_page()
elif pagina == "Seguros Empresariais":
    show_seguro_empresarial_page()
elif pagina == "Seguros de Vida":
    show_seguro_vida_page()
elif pagina == "Corretores":
    show_corretor_page()
elif pagina == "Planos de Seguro":
    show_plano_seguro_page()
elif pagina == "Reembolsos":
    show_reembolso_page()
elif pagina == "Propostas de Seguro":
    show_proposta_seguro_page()
elif pagina == "Apólices":
    show_apolice_page()