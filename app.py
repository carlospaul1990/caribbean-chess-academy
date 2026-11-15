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
# LOGO DE CARIBBEAN CHESS ACADEMY (CARGA LOCAL O VECTORIAL DE ALTA PRECISIÓN)
# -----------------------------------------------------------------------------
def get_cca_logo_html():
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return f'<img src="data:image/png;base64,{data}" class="cca-logo-img" alt="Caribbean Chess Academy">'
    
    # Réplica vectorial limpia del Rey Rojo con el Peón y Cerebro en su interior
    return """
    <div class="cca-logo-vector">
        <svg viewBox="0 0 220 230" width="130" height="135" xmlns="http://www.w3.org/2000/svg">
            <!-- Cruz Superior del Rey -->
            <path d="M105,12 H115 V22 H125 V32 H115 V42 H105 V32 H95 V22 H105 Z" fill="#D90429"/>
            <!-- Corona y Cuerpo del Rey Rojo -->
            <path d="M84,48 C84,42 136,42 136,48 L128,82 H136 C140,82 140,92 136,92 H127 L142,152 C148,158 148,170 142,175 H78 C72,170 72,158 78,152 L93,92 H84 C80,92 80,82 84,82 H92 Z" fill="#D90429"/>
            <!-- Silueta Blanca del Peón Interior -->
            <circle cx="110" cy="112" r="15" fill="#FFFFFF"/>
            <path d="M101,126 H119 L124,158 C128,162 128,170 124,175 H96 C92,170 92,162 96,158 Z" fill="#FFFFFF"/>
            <!-- Detalle del Cerebro dentro de la cabeza del Peón -->
            <path d="M103,112 C101,108 105,103 110,104 C115,103 119,108 117,112 C119,116 115,120 110,119 C105,120 101,116 103,112 Z" fill="none" stroke="#0F1E36" stroke-width="1.8"/>
            <path d="M110,104 V119 M104,111 H116" stroke="#0F1E36" stroke-width="1.3"/>
            <!-- Textos Institucionales -->
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
    --gold-bg: #FEF9C3;
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

/* HERO BANNER SOBRE BLANCO DE ALTO IMPACTO */
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

/* NAVEGACIÓN PRINCIPAL MODERNA (ALTO CONTRASTE SOBRE BLANCO) */
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

/* TARJETAS DE DATOS CLAVE (KPIs DEL TORNEO) */
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

/* TARJETAS DE CATEGORÍAS ELO */
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

/* TARJETAS DE CRONOGRAMA DE RONDAS */
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

/* ESTILOS DEL FORMULARIO SOBRE FONDO BLANCO */
[data-testid="stForm"] {
    background: #FFFFFF !important;
    border: 1.5px solid #CBD5E1 !important;
    border-top: 5px solid var(--navy) !important;
    border-radius: 18px !important;
    padding: 1.6rem !important;
    box-shadow: 0 12px 32px rgba(15, 30, 54, 0.07) !important;
}

[data-testid="stForm"] label p {
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

[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #D90429 0%, #A4031F 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.9rem 1.2rem !important;
    margin-top: 0.6rem !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    box-shadow: 0 8px 20px rgba(217, 4, 41, 0.3) !important;
}

[data-testid="stFormSubmitButton"] button p {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* BARRA FLOTANTE INFERIOR WHATSAPP */
.sticky-bottom-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-top: 1px solid #E2E8F0;
    padding: 10px 16px;
    z-index: 9999;
    display: flex;
    justify-content: center;
}

.sticky-wa-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    max-width: 600px;
    background: linear-gradient(90deg, #16A34A 0%, #15803D 100%);
    color: #FFFFFF !important;
    text-decoration: none;
    font-weight: 800;
    font-size: 0.92rem;
    padding: 13px 18px;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(22, 163, 74, 0.32);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ADAPTACIÓN MÓVIL (< 768px) */
@media (max-width: 768px) {
    .hero-white-card {
        flex-direction: column;
        text-align: center;
        padding: 1.4rem 1rem 1rem 1rem;
        gap: 12px;
    }
    .cca-logo-img {
        width: 115px;
    }
    .hero-main-title {
        font-size: 1.95rem;
    }
    .kpi-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .kpi-grid .kpi-box:last-child {
        grid-column: span 2;
    }
    div.stButton > button[kind="secondary"],
    div.stButton > button[kind="primary"] {
        font-size: 0.85rem !important;
        padding: 0.75rem 0.4rem !important;
    }
}
</style>
"""

st.markdown(CSS_LIGHT_MODERNO, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATOS OFICIALES DEL TORNEO FUTURAS ESTRELLAS V2
# -----------------------------------------------------------------------------
RONDAS_TORNEO = [
    {"dia": "Sábado", "fecha": "9 Enero 2027", "ronda": "1ra Ronda", "hora": "2:00 PM"},
    {"dia": "Sábado", "fecha": "9 Enero 2027", "ronda": "2da Ronda", "hora": "4:00 PM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027", "ronda": "3ra Ronda", "hora": "9:00 AM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027", "ronda": "4ta Ronda", "hora": "2:00 PM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027", "ronda": "5ta Ronda", "hora": "4:00 PM"},
]

def generar_ics_futuras_estrellas():
    return (
        "BEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "BEGIN:VEVENT\n"
        "DTSTART:20270109T140000\n"
        "DTEND:20270110T180000\n"
        "SUMMARY:Torneo Futuras Estrellas V2 - Caribbean Chess Academy\n"
        "DESCRIPTION:Torneo de Ajedrez Clásico Infantil (Ritmo 60m+30s, Válido FIDE). Categorías Sub-1600, Sub-1800 y Up-1801. Inscripción RD$650.\n"
        "LOCATION:Acrópolis Business Mall, Distrito Nacional, Santo Domingo\n"
        "END:VEVENT\n"
        "END:VCALENDAR"
    )

# -----------------------------------------------------------------------------
# HERO BANNER SOBRE FONDO BLANCO + RELOJ EN VIVO
# -----------------------------------------------------------------------------
logo_html = get_cca_logo_html()

st.markdown(
    f"""
    <div class="hero-white-card">
        {logo_html}
        <div style="flex: 1;">
            <div class="pill-badge">★ ¡Ven y demuestra tu talento en el tablero! • Válido FIDE</div>
            <h1 class="hero-main-title">FUTURAS <span>ESTRELLAS</span> <span class="hero-v2-tag">V2</span></h1>
            <div class="hero-subtitle">★ TORNEO DE AJEDREZ CLÁSICO INFANTIL • <strong>9 Y 10 ENERO 2027</strong> ★</div>
            <p style="color: #475569; font-size: 0.9rem; margin-top: 10px; margin-bottom: 0; font-weight: 500;">
                Organizado por <strong>Caribbean Chess Academy</strong> en <strong>Acrópolis Business Mall</strong>, Distrito Nacional.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

RELOJ_MODERNO_HTML = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        background: transparent;
        font-family: 'Montserrat', sans-serif;
    }
    .timer-bar {
        background: #0F1E36;
        border: 1.5px solid #0F1E36;
        border-radius: 0 0 22px 22px;
        padding: 14px 16px 16px 16px;
        box-shadow: 0 12px 30px rgba(15, 30, 54, 0.14);
    }
    .timer-title {
        font-size: 0.72rem;
        color: #EAB308;
        font-weight: 800;
        text-align: center;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        max-width: 520px;
        margin: 0 auto;
    }
    .box {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 9px 4px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .num {
        font-size: 1.65rem;
        font-weight: 900;
        color: #0F1E36;
        line-height: 1;
        font-variant-numeric: tabular-nums;
    }
    .num.sec {
        color: #D90429;
    }
    .lbl {
        font-size: 0.62rem;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 3px;
        font-weight: 800;
    }
</style>
</head>
<body>
    <div class="timer-bar">
        <div class="timer-title">⏳ Inicio 1ra Ronda • Sábado 9 de Enero 2027 (2:00 PM)</div>
        <div class="grid">
            <div class="box"><div class="num" id="d">--</div><div class="lbl">Días</div></div>
            <div class="box"><div class="num" id="h">--</div><div class="lbl">Horas</div></div>
            <div class="box"><div class="num" id="m">--</div><div class="lbl">Min</div></div>
            <div class="box"><div class="num sec" id="s">--</div><div class="lbl">Seg</div></div>
        </div>
    </div>

    <script>
        const targetDate = new Date("2027-01-09T14:00:00-04:00").getTime();

        function updateTimer() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance <= 0) {
                document.getElementById("d").innerText = "00";
                document.getElementById("h").innerText = "00";
                document.getElementById("m").innerText = "00";
                document.getElementById("s").innerText = "00";
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("d").innerText = String(days).padStart(2, '0');
            document.getElementById("h").innerText = String(hours).padStart(2, '0');
            document.getElementById("m").innerText = String(minutes).padStart(2, '0');
            document.getElementById("s").innerText = String(seconds).padStart(2, '0');
        }

        updateTimer();
        setInterval(updateTimer, 1000);
    </script>
</body>
</html>
"""

components.html(RELOJ_MODERNO_HTML, height=128)

# -----------------------------------------------------------------------------
# NAVEGACIÓN PRINCIPAL MODERNA (3 PESTAÑAS DE ALTO CONTRASTE)
# -----------------------------------------------------------------------------
st.markdown('<div class="nav-prompt">Explora la información oficial del torneo</div>', unsafe_allow_html=True)

nav1, nav2, nav3 = st.columns(3, gap="small")

with nav1:
    if st.button(
        "♔ DETALLES Y CATEGORÍAS",
        type="primary" if st.session_state.vista_cca == "torneo" else "secondary",
        use_container_width=True
    ):
        st.session_state.vista_cca = "torneo"
        st.rerun()

with nav2:
    if st.button(
        "📅 RONDAS Y HORARIOS",
        type="primary" if st.session_state.vista_cca == "rondas" else "secondary",
        use_container_width=True
    ):
        st.session_state.vista_cca = "rondas"
        st.rerun()

with nav3:
    if st.button(
        "📝 INSCRIPCIÓN (RD$650)",
        type="primary" if st.session_state.vista_cca == "inscripcion" else "secondary",
        use_container_width=True
    ):
        st.session_state.vista_cca = "inscripcion"
        st.rerun()

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# =============================================================================
# VISTA 1: DETALLES TÉCNICOS, CATEGORÍAS Y PREMIOS
# =============================================================================
if st.session_state.vista_cca == "torneo":
    # 5 Bloques de Información Clave (extraídos directamente del flyer)
    st.markdown(
        """
        <div class="kpi-grid">
            <div class="kpi-box">
                <div class="kpi-icon">⏱️</div>
                <div class="kpi-title">Ritmo Clásico</div>
                <div class="kpi-val">60 Min + 30 Seg</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-icon">🌐</div>
                <div class="kpi-title">Aval Oficial</div>
                <div class="kpi-val">Rating FIDE</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-icon">🎁</div>
                <div class="kpi-title">Premios Top 3</div>
                <div class="kpi-val">Gift Cards</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-icon">💵</div>
                <div class="kpi-title">Inscripción</div>
                <div class="kpi-val" style="color: #D90429;">RD$ 650</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-icon">📍</div>
                <div class="kpi-title">Sede Oficial</div>
                <div class="kpi-val">Acrópolis Mall</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_cat, col_info = st.columns([1.1, 1], gap="large")

    with col_cat:
        st.markdown("#### 🎯 Categorías por Rating ELO")
        st.markdown(
            """
            <div class="cat-card">
                <div>
                    <div class="cat-title">♟️ SUB <span>1600</span></div>
                    <div style="font-size: 0.78rem; color: #64748B; font-weight: 600;">Jugadores con ELO menor a 1600</div>
                </div>
                <div class="cat-badge">Clásico Infantil</div>
            </div>
            <div class="cat-card">
                <div>
                    <div class="cat-title">♞ SUB <span>1800</span></div>
                    <div style="font-size: 0.78rem; color: #64748B; font-weight: 600;">Jugadores con ELO entre 1600 y 1799</div>
                </div>
                <div class="cat-badge">Clásico Infantil</div>
            </div>
            <div class="cat-card">
                <div>
                    <div class="cat-title">♔ UP <span>1801</span></div>
                    <div style="font-size: 0.78rem; color: #64748B; font-weight: 600;">Jugadores con ELO de 1801 en adelante</div>
                </div>
                <div class="cat-badge">Élite Infantil</div>
            </div>
            <div class="elo-alert">
                ⚠️ Requisito Obligatorio: Todos los participantes deben tener ELO
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_info:
        st.markdown("#### 🏆 Premiación y Sede")
        st.markdown(
            """
            <div style="background: #FFFBEB; border: 1.5px solid #FDE68A; border-radius: 14px; padding: 16px; margin-bottom: 12px;">
                <div style="font-weight: 900; color: #92400E; font-size: 1rem;">🎁 PREMIOS ESPECIALES EN GIFT CARDS</div>
                <p style="color: #78350F; font-size: 0.86rem; margin-top: 6px; margin-bottom: 0; line-height: 1.45;">
                    Se otorgarán <strong>Gift Cards especiales para los 3 primeros lugares</strong> de cada categoría oficial (Sub-1600, Sub-1800 y Up-1801).
                </p>
            </div>
            <div style="background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 14px; padding: 16px;">
                <div style="font-weight: 900; color: #0F1E36; font-size: 0.98rem;">📍 UBICACIÓN DEL TORNEO</div>
                <p style="color: #475569; font-size: 0.86rem; margin-top: 6px; margin-bottom: 10px; line-height: 1.45;">
                    <strong>Acrópolis Business Mall</strong>, Av. Winston Churchill, Distrito Nacional, Santo Domingo.
                </p>
                <a href="https://maps.google.com/?q=Acropolis+Business+Mall+Santo+Domingo" target="_blank"
                   style="display: inline-block; background: #0F1E36; color: #FFFFFF; font-size: 0.78rem; font-weight: 800;
                          padding: 8px 14px; border-radius: 8px; text-decoration: none; text-transform: uppercase;">
                    🗺️ Abrir en Google Maps
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# =============================================================================
# VISTA 2: CRONOGRAMA DE RONDAS (SÁBADO 9 Y DOMINGO 10 ENERO 2027)
# =============================================================================
elif st.session_state.vista_cca == "rondas":
    st.markdown("#### 📅 Calendario Oficial de Rondas — Enero 2027")
    st.caption("Sistema Suizo a 5 rondas • Ritmo Clásico: 60 minutos + 30 segundos por jugada.")

    for r in RONDAS_TORNEO:
        st.markdown(
            f"""
            <div class="round-row">
                <div>
                    <div class="round-day">{r['dia']}</div>
                    <div class="round-date">{r['fecha']}</div>
                </div>
                <div class="round-badge">
                    <div class="round-num">{r['ronda']}</div>
                    <div class="round-time">🕒 {r['hora']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.download_button(
        label="📲 AGENDAR TORNEO COMPLETO EN MI CALENDARIO (.ICS)",
        data=generar_ics_futuras_estrellas(),
        file_name="futuras_estrellas_v2_caribbean_chess.ics",
        mime="text/calendar",
        use_container_width=True
    )

# =============================================================================
# VISTA 3: INSCRIPCIÓN RÁPIDA (RD$650)
# =============================================================================
elif st.session_state.vista_cca == "inscripcion":
    st.markdown("#### 📝 Formulario de Inscripción — Futuras Estrellas V2")
    st.caption("Costo de inscripción: **RD$650** • Recuerda que todos los participantes deben poseer ID/Rating ELO FIDE.")

    with st.form("form_cca"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            nombre = st.text_input("👤 Nombre Completo del Jugador *", placeholder="Ej. Mateo Gómez")
            id_fide = st.text_input("🌐 ID FIDE / ELO Actual (Obligatorio) *", placeholder="Ej. 6409876 (ELO: 1580)")
            categoria = st.selectbox(
                "🎯 Categoría por ELO *",
                ["Sub-1600", "Sub-1800", "Up-1801"]
            )
        with c2:
            telefono = st.text_input("📱 WhatsApp del Padre / Tutor *", placeholder="Ej. 849-555-0123")
            academia = st.text_input("♔ Academia / Club (Opcional)", placeholder="Ej. Caribbean Chess Academy")
            pago_info = st.selectbox(
                "💳 Método de Pago Preferido",
                ["Transferencia Bancaria", "Pago Presencial en Acrópolis"]
            )

        submit = st.form_submit_button("✅ GENERAR FICHA DE INSCRIPCIÓN", use_container_width=True)

    if submit:
        if not nombre or not telefono or not id_fide:
            st.error("⚠️ Por favor completa el nombre del jugador, su ID/ELO FIDE y el WhatsApp de contacto.")
        else:
            acad_txt = academia if academia else "Independiente"
            msg_wa = (
                f"*INSCRIPCIÓN FUTURAS ESTRELLAS V2 - CARIBBEAN CHESS ACADEMY*%0A"
                f"• *Jugador:* {urllib.parse.quote(nombre)}%0A"
                f"• *ID/ELO FIDE:* {urllib.parse.quote(id_fide)}%0A"
                f"• *Categoría:* {urllib.parse.quote(categoria)}%0A"
                f"• *Academia:* {urllib.parse.quote(acad_txt)}%0A"
                f"• *Pago (RD$650):* {urllib.parse.quote(pago_info)}%0A"
                f"• *Contacto:* {urllib.parse.quote(telefono)}"
            )
            st.success(f"✅ ¡Ficha lista para **{nombre}**! Envía tus datos al WhatsApp oficial para confirmar tu cupo:")
            st.link_button(
                "📲 ENVIAR INSCRIPCIÓN POR WHATSAPP (849-440-3222)",
                f"https://wa.me/18494403222?text={msg_wa}",
                use_container_width=True
            )

# -----------------------------------------------------------------------------
# BARRA FLOTANTE INFERIOR WHATSAPP (849-440-3222)
# -----------------------------------------------------------------------------
msg_directo = urllib.parse.quote("Hola Caribbean Chess Academy, deseo más información e inscribirme en el Torneo Futuras Estrellas V2 (9 y 10 de Enero 2027).")
st.markdown(
    f"""
    <div class="sticky-bottom-bar">
        <a href="https://wa.me/18494403222?text={msg_directo}" target="_blank" class="sticky-wa-btn">
            💬 MÁS INFORMACIÓN E INSCRIPCIONES • 849-440-3222
        </a>
    </div>
    """,
    unsafe_allow_html=True
)