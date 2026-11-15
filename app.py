import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import base64
import os

st.set_page_config(
    page_title="Caribbean Chess Academy | Torneos y Eventos",
    page_icon="♔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "vista_cca" not in st.session_state:
    st.session_state.vista_cca = "torneo"

def get_cca_logo_html():
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return (
            f'<img src="data:image/png;base64,{data}" '
            'class="cca-logo-img" alt="Caribbean Chess Academy">'
        )
    return (
        '<div class="cca-logo-vector">'
        '<svg viewBox="0 0 220 230" width="130" height="135">'
        '<path d="M105,12 H115 V22 H125 V32 H115 V42 '
        'H105 V32 H95 V22 H105 Z" fill="#D90429"/>'
        '<path d="M84,48 C84,42 136,42 136,48 L128,82 H136 '
        'C140,82 140,92 136,92 H127 L142,152 C148,158 148,170 '
        '142,175 H78 C72,170 72,158 78,152 L93,92 H84 '
        'C80,92 80,82 84,82 H92 Z" fill="#D90429"/>'
        '<circle cx="110" cy="112" r="15" fill="#FFFFFF"/>'
        '<path d="M101,126 H119 L124,158 C128,162 128,170 '
        '124,175 H96 C92,170 92,162 96,158 Z" fill="#FFFFFF"/>'
        '<path d="M103,112 C101,108 105,103 110,104 C115,103 '
        '119,108 117,112 C119,116 115,120 110,119 C105,120 '
        '101,116 103,112 Z" fill="none" stroke="#0F1E36" '
        'stroke-width="1.8"/>'
        '<path d="M110,104 V119 M104,111 H116" '
        'stroke="#0F1E36" stroke-width="1.3"/>'
        '<text x="110" y="191" text-anchor="middle" '
        'font-family="Montserrat, sans-serif" font-size="7.2" '
        'font-weight="700" letter-spacing="1.2" fill="#0F1E36">'
        'CONSTRUYENDO MENTES BRILLANTES</text>'
        '<text x="110" y="209" text-anchor="middle" '
        'font-family="Cinzel, serif" font-size="15.5" '
        'font-weight="700" fill="#0F1E36">CARIBBEAN CHESS</text>'
        '<text x="110" y="222" text-anchor="middle" '
        'font-family="Montserrat, sans-serif" font-size="8.5" '
        'font-weight="600" letter-spacing="4" fill="#475569">'
        'ACADEMY</text></svg></div>'
    )

st.markdown(
    "<style>"
    "@import url('https://fonts.googleapis.com/css2?"
    "family=Cinzel:wght@600;700&"
    "family=Montserrat:wght@500;600;700;800;900&display=swap');"
    ":root{--bg-white:#FFFFFF;--navy:#0F1E36;"
    "--red-king:#D90429;--gold:#EAB308;}"
    ".block-container{padding:1rem 1rem 5.5rem 1rem!important;"
    "max-width:1120px!important;}"
    ".stApp{background-color:#FFFFFF;"
    "background-image:radial-gradient(circle at 0% 0%,"
    "rgba(217,4,41,0.04) 0%,transparent 40%),"
    "radial-gradient(circle at 100% 10%,"
    "rgba(15,30,54,0.05) 0%,transparent 45%);"
    "color:#0F172A;font-family:'Montserrat',sans-serif;}"
    "#MainMenu,footer,header{visibility:hidden;}"
    ".hero-white-card{background:#FFFFFF;"
    "border:1.5px solid #E2E8F0;border-top:6px solid #D90429;"
    "border-radius:22px 22px 0 0;border-bottom:none;"
    "padding:1.6rem;box-shadow:0 12px 35px rgba(15,30,54,0.06);"
    "display:flex;align-items:center;gap:24px;}"
    ".cca-logo-img{width:145px;height:auto;"
    "object-fit:contain;flex-shrink:0;}"
    ".cca-logo-vector{flex-shrink:0;display:flex;"
    "align-items:center;justify-content:center;}"
    ".pill-badge{display:inline-flex;align-items:center;gap:6px;"
    "background:#FEF2F2;border:1px solid #FECACA;color:#D90429;"
    "padding:5px 14px;border-radius:999px;font-size:0.75rem;"
    "font-weight:800;letter-spacing:0.8px;"
    "text-transform:uppercase;margin-bottom:10px;}"
    ".hero-main-title{font-family:'Montserrat',sans-serif;"
    "font-size:2.55rem;font-weight:900;line-height:1.02;"
    "color:#0F1E36;margin:0;letter-spacing:-0.5px;"
    "text-transform:uppercase;}"
    ".hero-main-title span{color:#D90429;}"
    ".hero-v2-tag{display:inline-block;background:#EAB308;"
    "color:#0F1E36;font-weight:900;font-size:1.1rem;"
    "padding:2px 10px;border-radius:8px;vertical-align:middle;"
    "margin-left:6px;box-shadow:0 4px 10px rgba(234,179,8,0.35);}"
    ".hero-subtitle{background:#0F1E36;color:#FFFFFF;"
    "display:inline-block;padding:6px 14px;border-radius:8px;"
    "font-size:0.82rem;font-weight:700;letter-spacing:1px;"
    "margin-top:10px;text-transform:uppercase;}"
    ".hero-subtitle strong{color:#EAB308;}"
    ".nav-prompt{text-align:center;font-size:0.72rem;"
    "font-weight:800;letter-spacing:1.5px;color:#475569;"
    "text-transform:uppercase;margin:0.6rem 0 0.5rem 0;}"
    "div.stButton>button[kind='secondary']{"
    "background:#F8FAFC!important;color:#0F1E36!important;"
    "border:2px solid #CBD5E1!important;border-radius:14px!important;"
    "padding:0.85rem 0.4rem!important;"
    "font-family:'Montserrat',sans-serif!important;"
    "font-size:0.84rem!important;font-weight:800!important;"
    "text-transform:uppercase!important;}"
    "div.stButton>button[kind='primary']{"
    "background:#0F1E36!important;color:#FFFFFF!important;"
    "border:2px solid #0F1E36!important;"
    "border-bottom:4px solid #D90429!important;"
    "border-radius:14px!important;padding:0.85rem 0.4rem!important;"
    "font-family:'Montserrat',sans-serif!important;"
    "font-size:0.84rem!important;font-weight:800!important;"
    "text-transform:uppercase!important;"
    "box-shadow:0 8px 20px rgba(15,30,54,0.22)!important;}"
    ".kpi-grid{display:grid;grid-template-columns:repeat(5,1fr);"
    "gap:10px;margin-bottom:1.2rem;}"
    ".kpi-box{background:#FFFFFF;border:1.5px solid #E2E8F0;"
    "border-radius:14px;padding:14px 10px;text-align:center;"
    "box-shadow:0 4px 14px rgba(15,30,54,0.04);}"
    ".kpi-icon{font-size:1.5rem;margin-bottom:4px;}"
    ".kpi-title{font-size:0.68rem;font-weight:700;color:#475569;"
    "text-transform:uppercase;letter-spacing:0.5px;}"
    ".kpi-val{font-size:0.95rem;font-weight:800;color:#0F1E36;"
    "margin-top:2px;}"
    ".cat-card{background:#FFFFFF;border:1.5px solid #E2E8F0;"
    "border-left:6px solid #D90429;border-radius:14px;"
    "padding:16px;margin-bottom:12px;display:flex;"
    "justify-content:space-between;align-items:center;"
    "box-shadow:0 4px 12px rgba(15,30,54,0.04);}"
    ".cat-title{font-size:1.3rem;font-weight:900;color:#0F1E36;}"
    ".cat-title span{color:#D90429;}"
    ".cat-badge{background:#0F1E36;color:#EAB308;font-size:0.72rem;"
    "font-weight:800;padding:4px 10px;border-radius:6px;"
    "text-transform:uppercase;}"
    ".elo-alert{background:#FEF2F2;border:1.5px solid #FCA5A5;"
    "color:#991B1B;border-radius:12px;padding:12px 14px;"
    "font-size:0.85rem;font-weight:800;text-align:center;"
    "text-transform:uppercase;margin-top:10px;}"
    ".round-row{background:#FFFFFF;border:1.5px solid #E2E8F0;"
    "border-radius:14px;padding:12px 16px;margin-bottom:9px;"
    "display:flex;justify-content:space-between;align-items:center;"
    "box-shadow:0 3px 10px rgba(15,30,54,0.03);}"
    ".round-day{font-size:0.75rem;font-weight:800;color:#D90429;"
    "text-transform:
