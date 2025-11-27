#!/usr/bin/env python3
# populate_database.py - Script para popular o banco de dados com dados de exemplo

import sys
from pathlib import Path
import datetime

# Adicionar o diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

from Models.Endereco import Endereco
from Models.Usuario import Usuario
from Models.Corretor import Corretor
from Models.SeguroAuto import SeguroAuto
from Models.SeguroResidencial import SeguroResidencial
from Models.SeguroEmpresarial import SeguroEmpresarial
from Models.SeguroVida import SeguroVida
from Models.PlanoSeguro import PlanoSeguro
from Models.PropostaSeguro import PropostaSeguro
from Models.Apolice import Apolice
from Models.Reembolso import Reembolso

from Controllers import (
    EnderecoController, UsuarioController, CorretorController,
    SeguroAutoController, SeguroResidencialController, SeguroEmpresarialController,
    SeguroVidaController, PlanoSeguroController, PropostaSeguroController,
    ApoliceController, ReembolsoController
)

def criar_tabelas():
    """Cria todas as tabelas do banco de dados"""
    print("📊 Criando tabelas...")
    EnderecoController.criarTabelaEndereco()
    UsuarioController.criarTabelaUsuario()
    SeguroAutoController.criarTabelaSeguroAuto()
    SeguroResidencialController.criarTabelaSeguroResidencial()
    SeguroEmpresarialController.criarTabelaSeguroEmpresarial()
    SeguroVidaController.criarTabelaSeguroVida()
    PlanoSeguroController.criarTabelaPlanoSeguro()
    PropostaSeguroController.criarTabelaPropostaSeguro()
    ApoliceController.criarTabelaApolice()
    CorretorController.criarTabelaCorretor()
    ReembolsoController.criarTabelaReembolso()
    print("✅ Tabelas criadas com sucesso!\n")

def popular_enderecos():
    """Popula a tabela de endereços"""
    print("📍 Inserindo endereços...")
    enderecos = [
        ("01310100", "Avenida Paulista", "1000", "Apto 1001", "Consolação", "São Paulo", "SP"),
        ("04543132", "Rua Oscar Freire", "500", None, "Pinheiros", "São Paulo", "SP"),
        ("22250040", "Avenida Atlântica", "3000", "Apto 1200", "Copacabana", "Rio de Janeiro", "RJ"),
        ("30140071", "Avenida Getúlio Vargas", "1500", None, "Funcionários", "Belo Horizonte", "MG"),
        ("50030350", "Rua Pinto Bandeira", "800", "Apto 405", "Bom Fim", "Porto Alegre", "RS"),
        ("08550400", "Avenida Brasil", "2500", None, "Tatuapé", "São Paulo", "SP"),
        ("25960140", "Rua XV de Novembro", "456", None, "Centro", "Petrópolis", "RJ"),
        ("60115170", "Rua José de Alencar", "789", "Loja 2", "Centro", "Fortaleza", "CE"),
    ]
    
    endereco_ids = []
    for cep, logradouro, numero, complemento, bairro, cidade, estado in enderecos:
        endereco = Endereco(None, cep, logradouro, numero, complemento, bairro, cidade, estado)
        novo_id = EnderecoController.incluirEndereco(endereco)
        endereco_ids.append(novo_id)
    
    print(f"✅ {len(endereco_ids)} endereços inseridos!\n")
    return endereco_ids

def popular_usuarios(endereco_ids):
    """Popula a tabela de usuários"""
    print("👥 Inserindo usuários...")
    usuarios = [
        ("Carlos Eduardo Silva", "12345678901", datetime.date(1985, 3, 15), "1198765432", "carlos@example.com", "senha123", 2),  # Admin
        ("Ana Paula Costa", "98765432101", datetime.date(1990, 7, 22), "1187654321", "ana@example.com", "senha123", 1),  # Cliente
        ("Roberto Gomes", "11122233344", datetime.date(1988, 11, 5), "1176543210", "roberto@example.com", "senha123", 1),  # Cliente
        ("Juliana Oliveira", "55566677788", datetime.date(1992, 2, 14), "1165432109", "juliana@example.com", "senha123", 1),  # Cliente
        ("Marcos Antonio", "99988877766", datetime.date(1987, 9, 30), "1154321098", "marcos@example.com", "senha123", 1),  # Cliente
        ("Beatriz Fernandes", "33344455566", datetime.date(1995, 6, 8), "1143210987", "beatriz@example.com", "senha123", 1),  # Cliente
    ]
    
    usuario_ids = []
    for i, (nome, cpf, data_nasc, telefone, email, senha, tus_code) in enumerate(usuarios):
        usuario = Usuario(
            None, nome, cpf, data_nasc, telefone, email, senha,
            endereco_ids[i % len(endereco_ids)], None, None, tus_code, None
        )
        novo_id = UsuarioController.incluirUsuario(usuario)
        usuario_ids.append(novo_id)
    
    print(f"✅ {len(usuario_ids)} usuários inseridos!\n")
    return usuario_ids

def popular_corretores(endereco_ids):
    """Popula a tabela de corretores"""
    print("🤝 Inserindo corretores...")
    corretores = [
        ("João Correia Silva", "12345678901234"),
        ("Maria Correia Santos", "23456789012345"),
        ("Pedro Correia Costa", "34567890123456"),
        ("Fernanda Correia Lima", "45678901234567"),
    ]
    
    corretor_ids = []
    for i, (nome, cnpj) in enumerate(corretores):
        corretor = Corretor(None, nome, cnpj, endereco_ids[i % len(endereco_ids)])
        novo_id = CorretorController.incluirCorretor(corretor)
        corretor_ids.append(novo_id)
    
    print(f"✅ {len(corretor_ids)} corretores inseridos!\n")
    return corretor_ids

def popular_planos():
    """Popula a tabela de planos de seguro"""
    print("📋 Inserindo planos de seguro...")
    planos = [
        ("Plano Básico Auto", 1200.00, 100.00, "Cobertura contra roubo e reparos"),
        ("Plano Intermediário Auto", 2400.00, 200.00, "Cobertura completa com franquia reduzida"),
        ("Plano Premium Auto", 3600.00, 300.00, "Cobertura máxima sem franquia"),
        ("Plano Básico Residencial", 600.00, 50.00, "Cobertura básica para residência"),
        ("Plano Completo Residencial", 1800.00, 150.00, "Cobertura completa para residência"),
        ("Plano Empresarial Pequeno", 2400.00, 200.00, "Para pequenas empresas"),
        ("Plano Empresarial Médio", 4800.00, 400.00, "Para médias empresas"),
        ("Plano Vida Básico", 1200.00, 100.00, "Proteção familiar básica"),
        ("Plano Vida Premium", 3600.00, 300.00, "Proteção familiar completa"),
    ]
    
    plano_ids = []
    for nome, valor_total, valor_parcela, detalhes in planos:
        plano = PlanoSeguro(None, nome, valor_total, valor_parcela, detalhes)
        novo_id = PlanoSeguroController.incluirPlanoSeguro(plano)
        plano_ids.append(novo_id)
    
    print(f"✅ {len(plano_ids)} planos inseridos!\n")
    return plano_ids

def popular_seguros_auto(endereco_ids):
    """Popula a tabela de seguros auto"""
    print("🚗 Inserindo seguros auto...")
    seguros = [
        ("ABC1234", "Honda Civic", 2022),
        ("DEF5678", "Toyota Corolla", 2021),
        ("GHI9012", "Volkswagen Golf", 2023),
        ("JKL3456", "Ford Fiesta", 2020),
        ("MNO7890", "Chevrolet Onix", 2022),
    ]
    
    seguro_ids = []
    for i, (placa, modelo, ano) in enumerate(seguros):
        seguro = SeguroAuto(None, placa, modelo, ano, endereco_ids[i % len(endereco_ids)])
        novo_id = SeguroAutoController.incluirSeguroAuto(seguro)
        seguro_ids.append(novo_id)
    
    print(f"✅ {len(seguro_ids)} seguros auto inseridos!\n")
    return seguro_ids

def popular_seguros_residencial(endereco_ids):
    """Popula a tabela de seguros residenciais"""
    print("🏠 Inserindo seguros residenciais...")
    seguros = [
        "Apartamento",
        "Casa",
        "Casa em Condomínio",
        "Apartamento",
        "Casa",
    ]
    
    seguro_ids = []
    for i, tipo in enumerate(seguros):
        seguro = SeguroResidencial(None, tipo, endereco_ids[i % len(endereco_ids)])
        novo_id = SeguroResidencialController.incluirSeguroResidencial(seguro)
        seguro_ids.append(novo_id)
    
    print(f"✅ {len(seguro_ids)} seguros residenciais inseridos!\n")
    return seguro_ids

def popular_seguros_empresarial(endereco_ids):
    """Popula a tabela de seguros empresariais"""
    print("🏢 Inserindo seguros empresariais...")
    seguros = [
        "Comércio Varejista",
        "Indústria Manufatureira",
        "Serviços Profissionais",
        "Comércio Atacadista",
    ]
    
    seguro_ids = []
    for i, atividade in enumerate(seguros):
        seguro = SeguroEmpresarial(None, atividade, endereco_ids[i % len(endereco_ids)])
        novo_id = SeguroEmpresarialController.incluirSeguroEmpresarial(seguro)
        seguro_ids.append(novo_id)
    
    print(f"✅ {len(seguro_ids)} seguros empresariais inseridos!\n")
    return seguro_ids

def popular_seguros_vida(endereco_ids):
    """Popula a tabela de seguros de vida"""
    print("❤️ Inserindo seguros de vida...")
    seguros = [
        "Gerente de Vendas",
        "Analista de Sistemas",
        "Professora",
        "Empresário",
        "Servidor Público",
    ]
    
    seguro_ids = []
    for i, profissao in enumerate(seguros):
        seguro = SeguroVida(None, profissao, endereco_ids[i % len(endereco_ids)])
        novo_id = SeguroVidaController.incluirSeguroVida(seguro)
        seguro_ids.append(novo_id)
    
    print(f"✅ {len(seguro_ids)} seguros de vida inseridos!\n")
    return seguro_ids

def popular_propostas(usuario_ids, endereco_ids, seguro_auto_ids, corretor_ids, plano_ids):
    """Popula a tabela de propostas de seguro"""
    print("📝 Inserindo propostas de seguro...")
    
    propostas_ids = []
    hoje = datetime.date.today()
    
    # Proposta 1: Seguro Auto para Cliente 1
    proposta = PropostaSeguro(
        None, usuario_ids[1], endereco_ids[0], seguro_auto_ids[0], None, None, None,
        corretor_ids[0], "Plano Intermediário Auto", 200.00, 1, None,
        hoje, "Cartão de Crédito", 12, True, False,
        hoje, hoje + datetime.timedelta(days=365),
        2400.00, 2400.00, 0.0, 2400.00, 177.12
    )
    novo_id = PropostaSeguroController.incluirPropostaSeguro(proposta)
    propostas_ids.append(novo_id)
    
    # Proposta 2: Seguro Residencial para Cliente 2
    proposta = PropostaSeguro(
        None, usuario_ids[2], endereco_ids[1], None, 1, None, None,
        corretor_ids[1], "Plano Completo Residencial", 150.00, 1, None,
        hoje, "Boleto", 12, True, False,
        hoje, hoje + datetime.timedelta(days=365),
        1800.00, 1800.00, 0.0, 1800.00, 132.84
    )
    novo_id = PropostaSeguroController.incluirPropostaSeguro(proposta)
    propostas_ids.append(novo_id)
    
    # Proposta 3: Seguro Auto para Cliente 3
    proposta = PropostaSeguro(
        None, usuario_ids[3], endereco_ids[2], seguro_auto_ids[1], None, None, None,
        corretor_ids[2], "Plano Básico Auto", 100.00, 1, None,
        hoje - datetime.timedelta(days=30), "Cartão de Crédito", 12, True, False,
        hoje - datetime.timedelta(days=30), hoje + datetime.timedelta(days=335),
        1200.00, 1200.00, 0.0, 1200.00, 88.56
    )
    novo_id = PropostaSeguroController.incluirPropostaSeguro(proposta)
    propostas_ids.append(novo_id)
    
    # Proposta 4: Seguro Empresarial para Cliente 4
    proposta = PropostaSeguro(
        None, usuario_ids[4], endereco_ids[3], None, None, 1, None,
        corretor_ids[3], "Plano Empresarial Médio", 400.00, 1, None,
        hoje - datetime.timedelta(days=60), "Transferência", 12, True, False,
        hoje - datetime.timedelta(days=60), hoje + datetime.timedelta(days=305),
        4800.00, 4800.00, 0.0, 4800.00, 354.24
    )
    novo_id = PropostaSeguroController.incluirPropostaSeguro(proposta)
    propostas_ids.append(novo_id)
    
    # Proposta 5: Seguro de Vida para Cliente 5
    proposta = PropostaSeguro(
        None, usuario_ids[5], endereco_ids[4], None, None, None, 1,
        corretor_ids[0], "Plano Vida Premium", 300.00, 1, None,
        hoje - datetime.timedelta(days=15), "Cartão de Crédito", 12, True, False,
        hoje - datetime.timedelta(days=15), hoje + datetime.timedelta(days=350),
        3600.00, 3600.00, 0.0, 3600.00, 265.68
    )
    novo_id = PropostaSeguroController.incluirPropostaSeguro(proposta)
    propostas_ids.append(novo_id)
    
    print(f"✅ {len(propostas_ids)} propostas inseridas!\n")
    return propostas_ids

def popular_apolices(proposta_ids):
    """Popula a tabela de apólices"""
    print("📄 Inserindo apólices...")
    
    apolice_ids = []
    for proposta_id in proposta_ids:
        apolice = Apolice(None, proposta_id)
        novo_id = ApoliceController.incluirApolice(apolice)
        apolice_ids.append(novo_id)
    
    print(f"✅ {len(apolice_ids)} apólices inseridas!\n")
    return apolice_ids

def popular_reembolsos():
    """Popula a tabela de reembolsos"""
    print("💰 Inserindo reembolsos...")
    
    reembolsos = [
        ("Seguro Auto", "Plano Básico Auto", 500.00),
        ("Seguro Auto", "Plano Intermediário Auto", 750.00),
        ("Seguro Auto", "Plano Premium Auto", 1000.00),
        ("Seguro Residencial", "Plano Básico Residencial", 300.00),
        ("Seguro Residencial", "Plano Completo Residencial", 600.00),
        ("Seguro Empresarial", "Plano Empresarial Pequeno", 800.00),
        ("Seguro Empresarial", "Plano Empresarial Médio", 1500.00),
        ("Seguro Vida", "Plano Vida Básico", 1000.00),
        ("Seguro Vida", "Plano Vida Premium", 2000.00),
    ]
    
    reembolso_ids = []
    for seguro_tipo, plano_tipo, valor in reembolsos:
        reembolso = Reembolso(None, seguro_tipo, plano_tipo, valor)
        novo_id = ReembolsoController.incluirReembolso(reembolso)
        reembolso_ids.append(novo_id)
    
    print(f"✅ {len(reembolso_ids)} reembolsos inseridos!\n")
    return reembolso_ids

def main():
    """Função principal para popular o banco de dados"""
    print("\n" + "="*50)
    print("🔧 POPULANDO BANCO DE DADOS")
    print("="*50 + "\n")
    
    try:
        # Criar tabelas
        criar_tabelas()
        
        # Popular dados
        endereco_ids = popular_enderecos()
        usuario_ids = popular_usuarios(endereco_ids)
        corretor_ids = popular_corretores(endereco_ids)
        plano_ids = popular_planos()
        seguro_auto_ids = popular_seguros_auto(endereco_ids)
        seguro_res_ids = popular_seguros_residencial(endereco_ids)
        seguro_emp_ids = popular_seguros_empresarial(endereco_ids)
        seguro_vida_ids = popular_seguros_vida(endereco_ids)
        proposta_ids = popular_propostas(usuario_ids, endereco_ids, seguro_auto_ids, corretor_ids, plano_ids)
        apolice_ids = popular_apolices(proposta_ids)
        reembolso_ids = popular_reembolsos()
        
        print("="*50)
        print("✅ BANCO DE DADOS POPULADO COM SUCESSO!")
        print("="*50)
        print("\n📊 Resumo dos dados inseridos:")
        print(f"  • Endereços: {len(endereco_ids)}")
        print(f"  • Usuários: {len(usuario_ids)}")
        print(f"  • Corretores: {len(corretor_ids)}")
        print(f"  • Planos de Seguro: {len(plano_ids)}")
        print(f"  • Seguros Auto: {len(seguro_auto_ids)}")
        print(f"  • Seguros Residenciais: {len(seguro_res_ids)}")
        print(f"  • Seguros Empresariais: {len(seguro_emp_ids)}")
        print(f"  • Seguros de Vida: {len(seguro_vida_ids)}")
        print(f"  • Propostas: {len(proposta_ids)}")
        print(f"  • Apólices: {len(apolice_ids)}")
        print(f"  • Reembolsos: {len(reembolso_ids)}")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ Erro ao popular o banco de dados: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
