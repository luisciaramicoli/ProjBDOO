# styles.py - Configuração de estilos CSS para Streamlit

def apply_styles():
    """Aplica estilos CSS personalizados à aplicação com paleta azul sóbria"""
    
    styles = """
    <style>
    /* ===== CONFIGURAÇÕES GERAIS ===== */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* ===== BODY E BACKGROUND ===== */
    body {
        background: linear-gradient(135deg, #1e3a5f 0%, #2c5aa0 100%);
        min-height: 100vh;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1d2d 0%, #1a2f42 100%);
        border-right: 2px solid #2c5aa0;
    }
    
    [data-testid="stSidebar"] label {
        color: #e8f0fa;
        font-weight: 600;
        font-size: 15px;
        margin-top: 15px;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: #1a2f42;
        border: 2px solid #2c5aa0;
        border-radius: 8px;
        color: #e8f0fa;
    }
    
    /* ===== MAIN CONTAINER ===== */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1e3a5f 0%, #2c5aa0 100%);
    }
    
    /* ===== BOTÕES ===== */
    .stButton > button {
        background: linear-gradient(90deg, #2c5aa0 0%, #1e3a5f 100%);
        color: #ffffff;
        border: 2px solid #3d6bb3;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        padding: 10px 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(44, 90, 160, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        background: linear-gradient(90deg, #3d6bb3 0%, #2c5aa0 100%);
        box-shadow: 0 6px 16px rgba(44, 90, 160, 0.5);
    }
    
    /* ===== FORMULÁRIOS ===== */
    .stForm {
        background: #000D38;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(44, 90, 160, 0.2);
    }
    
    .stForm label {
        color: #ffffff;
        font-weight: 600;
        font-size: 14px;
    }
    
    .stForm input,
    .stForm select,
    .stForm textarea {
        background-color: #ffffff !important;
        border: 2px solid #2c5aa0 !important;
        border-radius: 8px;
        color: #1e3a5f !important;
        font-size: 14px;
        padding: 10px 12px;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input,
    .stPasswordInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
        border: 2px solid #2c5aa0 !important;
    }
    
    .stForm input:focus,
    .stForm select:focus,
    .stForm textarea:focus {
        border-color: #2c5aa0;
        box-shadow: 0 0 0 3px rgba(44, 90, 160, 0.15);
    }
    
    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        color: #e8f0fa;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    h1 {
        font-size: 32px;
        color: #ffffff;
        border-bottom: 3px solid #2c5aa0;
        padding-bottom: 10px;
    }
    
    h2 {
        font-size: 24px;
        border-bottom: 2px solid #3d6bb3;
        padding-bottom: 10px;
    }
    
    h3 {
        font-size: 18px;
        color: #d1dce8;
    }
    
    /* ===== DIVIDERS ===== */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #2c5aa0, transparent);
        margin: 20px 0;
    }
    
    /* ===== ALERTAS ===== */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid #2c5aa0;
        padding: 12px 15px;
        background-color: linear-gradient(135deg, rgba(232, 240, 250, 0.95) 0%, rgba(220, 230, 245, 0.95) 100%);
        color: #1e3a5f;
    }
    
    .stAlert > div:first-child {
        font-weight: 600;
    }
    
    /* ===== DATAFRAME / TABELAS ===== */
    .stDataFrame {
        background: linear-gradient(135deg, rgba(232, 240, 250, 0.98) 0%, rgba(220, 230, 245, 0.98) 100%) !important;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(44, 90, 160, 0.15);
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .stDataFrame [data-testid="stDataFrameContainer"] {
        background: linear-gradient(135deg, rgba(232, 240, 250, 0.98) 0%, rgba(220, 230, 245, 0.98) 100%) !important;
        border-radius: 10px;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .dataframe {
        background: transparent !important;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .dataframe thead {
        background: linear-gradient(90deg, #2c5aa0 0%, #1e3a5f 100%);
        color: #ffffff;
    }
    
    .dataframe th {
        background: linear-gradient(90deg, #2c5aa0 0%, #1e3a5f 100%);
        color: #ffffff;
        font-weight: 600;
        padding: 12px 10px;
        border: none;
    }
    
    .dataframe td {
        background: transparent;
        color: #1e3a5f;
        padding: 10px;
        border: none;
        border-bottom: 1px solid rgba(44, 90, 160, 0.1);
    }
    
    .dataframe tbody tr:hover {
        background: rgba(44, 90, 160, 0.08);
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        border-bottom: 2px solid rgba(44, 90, 160, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(232, 240, 250, 0.2);
        border-radius: 8px 8px 0 0;
        color: #e8f0fa;
        padding: 12px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(44, 90, 160, 0.5);
        border-bottom: 3px solid #3d6bb3;
    }
    
    /* ===== SELECTBOX ===== */
    [data-baseweb="select"] {
        background-color: rgba(232, 240, 250, 0.9);
        border-radius: 8px;
        border: 2px solid #d1dce8;
    }
    
    [data-baseweb="select"] input {
        color: #1e3a5f;
    }
    
    /* ===== CARDS/CONTAINERS ===== */
    .stContainer {
        background: linear-gradient(135deg, rgba(232, 240, 250, 0.95) 0%, rgba(220, 230, 245, 0.95) 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        margin-bottom: 20px;
        border: 1px solid rgba(44, 90, 160, 0.15);
    }
    
    /* ===== SPINNER/LOADER ===== */
    .stSpinner {
        color: #3d6bb3;
    }
    
    /* ===== SUCCESS/ERROR MESSAGES ===== */
    [data-testid="stAlert"] {
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* ===== TEXT ===== */
    p, span {
        color: #e8f0fa;
    }
    
    .stMarkdown p {
        line-height: 1.6;
        color: #e8f0fa;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2c5aa0;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #3d6bb3;
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        h1 {
            font-size: 24px;
        }
        
        h2 {
            font-size: 20px;
        }
        
        .stForm {
            padding: 15px;
        }
    }
    </style>
    """
    
    return styles


def get_color_palette():
    """Retorna a paleta de cores sóbria e azul da aplicação"""
    return {
        'primary': '#2c5aa0',
        'secondary': '#3d6bb3',
        'dark': '#1e3a5f',
        'darker': '#0f1d2d',
        'light': '#e8f0fa',
        'lighter': '#dcf5f5',
        'white': '#ffffff',
        'success': '#059669',
        'warning': '#d97706',
        'error': '#dc2626',
        'info': '#2563eb'
    }
