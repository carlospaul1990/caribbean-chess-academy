import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import base64
import os

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA (LIGHT MODE MODERNO + MOBILE-FIRST)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Caribbean Chess Academy | Futuras Estrellas V2",
    page_icon="♔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "vista_cca" not in st.session_state:
    st.session_state.vista_cca = "torneo"

# -----------------------------------------------------------------------------
# LOGO DE CARIBBEAN CHESS ACADEMY
# -----------------------------------------------------------------------------
def get_cca_logo_html():
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return f'<img src="data:image/png;base64,{data}" class="cca-logo-img" alt="Caribbean Chess Academy">'
    
    return """
    <div class="cca-logo-vector">
        <svg viewBox="0 0 220 230" width="130" height="135" xmlns="http://www.w3.org/2000/svg">
            <path d="M105,12 H115 V22 H125 V32 H115 V42 H105 V32 H95 V22 H105 Z" fill="#D90429"/>
            <path d="M84,48 C84,42 136,42 136,48 L128,82 H136 C140,82 140,92 136,92 H127 L142,152 C148,158 148,170 142,175 H78 C72,170 72,158 78,152 L93,92 H84 C80,92 80,82 84,82 H92 Z" fill="#D90429"/>
            <circle cx="110" cy="112" r="15" fill="#FFFFFF"/>
            <path d="M101,126 H119 L124,158 C128,162 128,170 124,175 H96 C92,170 92,162 96,158 Z" fill="#FFFFFF"/>
            <path d="M103,112 C101,108 105,103 110,104 C115,103 119,108 117,112 C119,116 115,120 110,119 C105,120 101,116 103,112 Z" fill="none" stroke="#0F1E36" stroke-width="1.8"/>
            <path d="M110,104 V119 M104,111 H116" stroke="#0F1E36" stroke-width="1.3"/>
            <text x="110" y="191" text-anchor="middle" font-family="Montserrat, sans-serif" font-size="7.2" font-weight="700" letter-spacing="1.2" fill="#0F1E36">CONSTRUYENDO MENTES BRILLANTES</text>
            <text x="110" y="209" text-anchor="middle" font-family="Cinzel, serif" font-size="15.5" font-weight="700" fill="#0F1E36">CARIBBEAN CHESS</text>
            <text x="110" y="222" text-anchor="middle" font-family="Montserrat, sans-serif" font-size="8.5" font-weight="600" letter-spacing="4" fill="#475569">ACADEMY</text>
        </svg>
    </div>
    """

# -----------------------------------------------------------------------------
# CSS EDITORIAL MODERNO (FONDO BLANCO PURO + AZUL MARINO + ROJO + DORADO)
# -----------------------------------------------------------------------------
CSS_LIGHT_MODERNO = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Montserrat:wght@500;600;700;800;900&display=swap');

:root {
    --bg-white: #FFFFFF;
    --bg-soft: #F8FAFC;
    --navy: #0F1E36;
    --navy-light: #1E3A5F;
    --red-king: #D90429;
    --gold: #EAB308;
    --border-light: #E2E8F0;
    --text-dark: #0F172A;
    --text-muted: #475569;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 5.5rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 1080px !important;
}

.stApp {
    background-color: var(--bg-white);
    background-image: 
        radial-gradient(circle at 0% 0%, rgba(217, 4, 41, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 100% 10%, rgba(15, 30, 54, 0.05) 0%, transparent 45%);
    color: var(--text-dark);
    font-family: 'Montserrat', sans-serif;
}

#MainMenu, footer, header {visibility: hidden;}

.hero-white-card {
    background: #FFFFFF;
    border: 1.5px solid var(--border-light);
    border-top: 6px solid var(--red-king);
    border-radius: 22px 22px 0 0;
    border-bottom: none;
    padding: 1.8rem 1.8rem 1.2rem 1.8rem;
    box-shadow: 0 12px 35px rgba(15, 30, 54, 0.06);
    display: flex;
    align-items: center;
    gap: 24px;
}

.cca-logo-img {
    width: 145px;
    height: auto;
    object-fit: contain;
    flex-shrink: 0;
}

.cca-logo-vector {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pill-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #FEF2F2;
    border: 1px solid #FECACA;
    color: var(--red-king);
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-main-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 2.65rem;
    font-weight: 900;
    line-height: 1.02;
    color: var(--navy);
    margin: 0;
    letter-spacing: -0.5px;
    text-transform: uppercase;
}

.hero-main-title span {
    color: var(--red-king);
}

.hero-v2-tag {
    display: inline-block;
    background: var(--gold);
    color: var(--navy);
    font-weight: 900;
    font-size: 1.1rem;
    padding: 2px 10px;
    border-radius: 8px;
    vertical-align: middle;
    margin-left: 6px;
    box-shadow: 0 4px 10px rgba(234, 179, 8, 0.35);
}

.hero-subtitle {
    background: var(--navy);
    color: #FFFFFF;
    display: inline-block;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-top: 10px;
    text-transform: uppercase;
}

.hero-subtitle strong {
    color: var(--gold);
}

.nav-prompt {
    text-align: center;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--text-muted);
    text-transform: uppercase;
    margin: 0.6rem 0 0.5rem 0;
}

div.stButton > button[kind="secondary"] {
    background: #F8FAFC !important;
    color: var(--navy) !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 14px !important;
    padding: 0.85rem 0.5rem !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.4px !important;
    text-transform: uppercase !important;
    box-shadow: 0 2px 8px rgba(15, 30, 54, 0.04) !important;
    transition: all 0.2s ease !important;
}

div.stButton > button[kind="secondary"]:hover {
    border-color: var(--navy) !important;
    background: #F1F5F9 !important;
    transform: translateY(-2px);
}

div.stButton > button[kind="primary"] {
    background: var(--navy) !important;
    color: #FFFFFF !important;
    border: 2px solid var(--navy) !important;
    border-bottom: 4px solid var(--red-king) !important;
    border-radius: 14px !important;
    padding: 0.85rem 0.5rem !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.4px !important;
    text-transform: uppercase !important;
    box-shadow: 0 8px 20px rgba(15, 30, 54, 0.22) !important;
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    margin-bottom: 1.2rem;
}

.kpi-box {
    background: #FFFFFF;
    border: 1.5px solid var(--border-light);
    border-radius: 14px;
    padding: 14px 10px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(15, 30, 54, 0.04);
    transition: transform 0.2s;
}

.kpi-box:hover {
    transform: translateY(-3px);
    border-color: var(--red-king);
}

.kpi-icon {
    font-size: 1.5rem;
    margin-bottom: 4px;
}

.kpi-title {
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.kpi-val {
    font-size: 0.95rem;
    font-weight: 800;
    color: var(--navy);
    margin-top: 2px;
}

.cat-card {
    background: #FFFFFF;
    border: 1.5px solid var(--border-light);
    border-left: 6px solid var(--red-king);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 12px rgba(15, 30, 54, 0.04);
}

.cat-title {
    font-size: 1.25rem;
    font-weight: 900;
    color: var(--navy);
}

.cat-title span {
    color: var(--red-king);
}

.cat-badge {
    background: var(--navy);
    color: var(--gold);
    font-size: 0.72rem;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 6px;
    text-transform: uppercase;
}

.elo-alert {
    background: #FEF2F2;
    border: 1.5px solid #FCA5A5;
    color: #991B1B;
    border-radius: 12px;
    padding: 12px 14px;
    font-size: 0.85rem;
    font-weight: 800;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 8px;
}

.round-row {
    background: #FFFFFF;
    border: 1.5px solid var(--border-light);
    border-radius: 14px;
    padding: 12px 16px;
    margin-bottom: 9px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 3px 10px rgba(15, 30, 54, 0.03);
}

.round-day {
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--red-king);
    text-transform: uppercase;
}

.round-date {
    font-size: 0.98rem;
    font-weight: 800;
    color: var(--navy);
}

.round-badge {
    background: var(--navy);
    color: #FFFFFF;
    padding: 6px 12px;
    border-radius: 10px;
    text-align: right;
}

.round-num {
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--gold);
    text-transform: uppercase;
}

.round-time {
    font-size: 0.95rem;
    font-weight: 800;
}

[data-testid="stForm"] {
    background: #FFFFFF !important;
    border: 1.5px solid #CBD5E1 !important;
    border-top: 5px solid var(--navy) !important;
    border-radius: 18px !important;
    padding: 1.6rem !important;
    box-shadow: 0 12px 32px rgba(15, 30, 54, 0.07) !important;
}

[data-testid="stForm"] label p,
[data-testid="stFileUploader"] label p {
    color: var(--navy) !important;
    font-weight: 800 !important;
    font-size: 0.88rem !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #F8FAFC !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 12px !important;
    color: var(--navy) !important;
    min-height: 46px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="select"] > div:focus-within {
    border-color: var(--red-king) !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(217, 4, 41, 0.12) !important;
}

[data-testid="stFileUploader"] section {
    background-color: #F8FAFC !important;
    border: 2px dashed #94A3B8 !important;
    border-radius: 14px !important;
    padding: 14px !important;
    transition: all 0.2s ease !important;
}

[data-testid="stFileUploader"] section:hover {
    border-color: var(--red-king) !important;
    background-color: #FEF2F2 !important;
}

[data-testid="stFileUploader"] button {
    background-color: var(--navy) !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    border: none !important;
}

[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #D90429 0%, #A4031F 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.95rem 1.2rem !important;
    margin-top: 0.8rem !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    box-shadow: 0 8px 20px rgba(217, 4, 41, 0.3) !important;
}

[data-
