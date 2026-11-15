import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import base64
import io
import os

def obtener_rey_recortado(tamano=None):
    if not os.path.exists("logo.png"):
        return None
    try:
        from PIL import Image
        img = Image.open("logo.png").convert("RGBA")
        w, h = img.size
        # Recortar exclusivamente la figura del rey (eliminando texto inferior)
        solo_rey = img.crop((0, 0, w, int(h * 0.70)))
        bbox = solo_rey.getbbox()
        if bbox:
            solo_rey = solo_rey.crop(bbox)
        if tamano:
            lado = max(solo_rey.size)
            cuadrado = Image.new("RGBA", (lado, lado), (255, 255, 255, 0))
            cuadrado.paste(
                solo_rey,
                ((lado - solo_rey.width) // 2, (lado - solo_rey.height) // 2)
            )
            return cuadrado.resize((tamano, tamano), Image.LANCZOS)
        return solo_rey
    except Exception:
        return None

ICONO_PAGINA = obtener_rey_recortado(64) or (
    "logo.png" if os.path.exists("logo.png") else "♔"
)

st.set_page_config(
    page_title="Caribbean Chess Academy | Torneos y Eventos",
    page_icon=ICONO_PAGINA,
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "vista_cca" not in st.session_state:
    st.session_state.vista_cca = "torneo"

def get_cca_logo_html():
    rey_img = obtener_rey_recortado()
    if rey_img is not None:
        buf = io.BytesIO()
        rey_img.save(buf, format="PNG")
        data = base64.b64encode(buf.getvalue()).decode("utf-8")
        return (
            f'<img src="data:image/png;base64,{data}" '
            'class="cca-logo-img" alt="Caribbean Chess Academy">'
        )
    if os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        return (
            f'<img src="data:image/png;base64,{data}" '
            'class="cca-logo-img" alt="Caribbean Chess Academy">'
        )
    return """<div class="cca-logo-vector">
<svg viewBox="65 8 90 172" width="105" height="155">
<path d="M105,12 H115 V22 H125 V32 H115 V42 H105 V32 H95 V22 H105 Z" fill="#D90429"/>
<path d="M84,48 C84,42 136,42 136,48 L128,82 H136 C140,82 140,92 136,92 H127 L142,152 C148,158 148,170 142,175 H78 C72,170 72,158 78,152 L93,92 H84 C80,92 80,82 84,82 H92 Z" fill="#D90429"/>
<circle cx="110" cy="112" r="15" fill="#FFFFFF"/>
<path d="M101,126 H119 L124,158 C128,162 128,170 124,175 H96 C92,170 92,162 96,158 Z" fill="#FFFFFF"/>
<path d="M103,112 C101,108 105,103 110,104 C115,103 119,108 117,112 C119,116 115,120 110,119 C105,120 101,116 103,112 Z" fill="none" stroke="#0F1E36" stroke-width="1.8"/>
<path d="M110,104 V119 M104,111 H116" stroke="#0F1E36" stroke-width="1.3"/>
</svg></div>"""

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Montserrat:wght@500;600;700;800;900&display=swap');
:root{--bg-white:#FFFFFF;--navy:#0F1E36;--red-king:#D90429;--gold:#EAB308;}
.block-container{padding:1rem 1rem 5.5rem 1rem!important;max-width:1120px!important;}
.stApp{background-color:#FFFFFF;background-image:radial-gradient(circle at 0% 0%,rgba(217,4,41,0.04) 0%,transparent 40%),radial-gradient(circle at 100% 10%,rgba(15,30,54,0.05) 0%,transparent 45%);color:#0F172A;font-family:'Montserrat',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.hero-white-card{background:#FFFFFF;border:1.5px solid #E2E8F0;border-top:6px solid #D90429;border-radius:22px 22px 0 0;border-bottom:none;padding:1.6rem;box-shadow:0 12px 35px rgba(15,30,54,0.06);display:flex;align-items:center;gap:24px;}
.cca-logo-img{width:118px;max-height:155px;object-fit:contain;flex-shrink:0;}
.cca-logo-vector{flex-shrink:0;display:flex;align-items:center;justify-content:center;}
.pill-badge{display:inline-flex;align-items:center;gap:6px;background:#FEF2F2;border:1px solid #FECACA;color:#D90429;padding:5px 14px;border-radius:999px;font-size:0.75rem;font-weight:800;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:10px;}
.hero-main-title{font-family:'Montserrat',sans-serif;font-size:2.55rem;font-weight:900;line-height:1.02;color:#0F1E36;margin:0;letter-spacing:-0.5px;text-transform:uppercase;}
.hero-main-title span{color:#D90429;}
.hero-v2-tag{display:inline-block;background:#EAB308;color:#0F1E36;font-weight:900;font-size:1.1rem;padding:2px 10px;border-radius:8px;vertical-align:middle;margin-left:6px;box-shadow:0 4px 10px rgba(234,179,8,0.35);}
.hero-subtitle{background:#0F1E36;color:#FFFFFF;display:inline-block;padding:6px 14px;border-radius:8px;font-size:0.82rem;font-weight:700;letter-spacing:1px;margin-top:10px;text-transform:uppercase;}
.hero-subtitle strong{color:#EAB308;}
.nav-prompt{text-align:center;font-size:0.72rem;font-weight:800;letter-spacing:1.5px;color:#475569;text-transform:uppercase;margin:0.6rem 0 0.5rem 0;}
div.stButton>button[kind='secondary']{background:#F8FAFC!important;color:#0F1E36!important;border:2px solid #CBD5E1!important;border-radius:14px!important;padding:0.85rem 0.4rem!important;font-family:'Montserrat',sans-serif!important;font-size:0.84rem!important;font-weight:800!important;text-transform:uppercase!important;}
div.stButton>button[kind='primary']{background:#0F1E36!important;color:#FFFFFF!important;border:2px solid #0F1E36!important;border-bottom:4px solid #D90429!important;border-radius:14px!important;padding:0.85rem 0.4rem!important;font-family:'Montserrat',sans-serif!important;font-size:0.84rem!important;font-weight:800!important;text-transform:uppercase!important;box-shadow:0 8px 20px rgba(15,30,54,0.22)!important;}
.kpi-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:1.2rem;}
.kpi-box{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:14px;padding:14px 10px;text-align:center;box-shadow:0 4px 14px rgba(15,30,54,0.04);}
.kpi-icon{font-size:1.5rem;margin-bottom:4px;}
.kpi-title{font-size:0.68rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.5px;}
.kpi-val{font-size:0.95rem;font-weight:800;color:#0F1E36;margin-top:2px;}
.cat-card{background:#FFFFFF;border:1.5px solid #E2E8F0;border-left:6px solid #D90429;border-radius:14px;padding:14px 16px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 4px 12px rgba(15,30,54,0.04);}
.cat-title{font-size:1.25rem;font-weight:900;color:#0F1E36;}
.cat-title span{color:#D90429;}
.cat-badge{background:#0F1E36;color:#EAB308;font-size:0.72rem;font-weight:800;padding:4px 10px;border-radius:6px;text-transform:uppercase;}
.elo-note{background:#EFF6FF;border:1.5px solid #93C5FD;color:#1E3A8A;border-radius:12px;padding:12px 14px;font-size:0.84rem;font-weight:800;text-align:center;margin-top:10px;line-height:1.4;}
.round-row{background:#FFFFFF;border:1.5px solid #E2E8F0;border-radius:14px;padding:12px 16px;margin-bottom:9px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 3px 10px rgba(15,30,54,0.03);}
.round-day{font-size:0.75rem;font-weight:800;color:#D90429;text-transform:uppercase;}
.round-date{font-size:0.98rem;font-weight:800;color:#0F1E36;}
.round-badge{background:#0F1E36;color:#FFFFFF;padding:6px 12px;border-radius:10px;text-align:right;}
.round-num{font-size:0.7rem;font-weight:700;color:#EAB308;text-transform:uppercase;}
.round-time{font-size:0.95rem;font-weight:800;}
.event-card{background:#FFFFFF;border:1.5px solid #E2E8F0;border-left:6px solid #0F1E36;border-radius:16px;padding:16px;margin-bottom:10px;box-shadow:0 6px 18px rgba(15,30,54,0.05);}
.event-card.featured{border-left:6px solid #D90429;background:linear-gradient(135deg,#FFFFFF 0%,#FFF8F8 100%);}
.ev-tag{display:inline-block;background:#0F1E36;color:#EAB308;font-size:0.7rem;font-weight:800;padding:3px 10px;border-radius:6px;text-transform:uppercase;}
.ev-tag.red{background:#D90429;color:#FFFFFF;}
.ev-title{font-size:1.2rem;font-weight:900;color:#0F1E36;margin:6px 0 3px 0;}
.ev-meta{font-size:0.82rem;font-weight:700;color:#475569;margin-bottom:6px;}
.ev-desc{font-size:0.85rem;color:#334155;line-height:1.45;margin:0;}
[data-testid='stForm']{background:#FFFFFF!important;border:1.5px solid #CBD5E1!important;border-top:5px solid #0F1E36!important;border-radius:18px!important;padding:1.5rem!important;box-shadow:0 12px 32px rgba(15,30,54,0.07)!important;}
[data-testid='stForm'] label p,[data-testid='stFileUploader'] label p{color:#0F1E36!important;font-weight:800!important;font-size:0.88rem!important;}
div[data-baseweb='input']>div,div[data-baseweb='select']>div{background-color:#F8FAFC!important;border:1.5px solid #CBD5E1!important;border-radius:12px!important;color:#0F1E36!important;min-height:46px!important;}
[data-testid='stFileUploader'] section{background-color:#F8FAFC!important;border:2px dashed #94A3B8!important;border-radius:14px!important;padding:14px!important;}
[data-testid='stFileUploader'] button{background-color:#0F1E36!important;color:#FFFFFF!important;border-radius:8px!important;font-weight:700!important;}
[data-testid='stFormSubmitButton'] button{background:linear-gradient(135deg,#D90429 0%,#A4031F 100%)!important;color:#FFFFFF!important;border:none!important;border-radius:12px!important;padding:0.95rem 1.2rem!important;margin-top:0.8rem!important;font-family:'Montserrat',sans-serif!important;font-size:1.05rem!important;font-weight:800!important;text-transform:uppercase!important;box-shadow:0 8px 20px rgba(217,4,41,0.3)!important;}
[data-testid='stFormSubmitButton'] button p{color:#FFFFFF!important;font-weight:800!important;}
.sticky-bottom-bar{position:fixed;bottom:0;left:0;right:0;background:rgba(255,255,255,0.92);backdrop-filter:blur(12px);border-top:1px solid #E2E8F0;padding:10px 16px;z-index:9999;display:flex;justify-content:center;}
.sticky-wa-btn{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;max-width:600px;background:linear-gradient(90deg,#16A34A 0%,#15803D 100%);color:#FFFFFF!important;text-decoration:none;font-weight:800;font-size:0.92rem;padding:13px 18px;border-radius:12px;box-shadow:0 6px 18px rgba(22,163,74,0.32);text-transform:uppercase;}
@media(max-width:768px){.hero-white-card{flex-direction:column;text-align:center;padding:1.3rem 1rem 1rem 1rem;gap:12px;}.cca-logo-img{width:95px;max-height:125px;}.hero-main-title{font-size:1.95rem;}.kpi-grid{grid-template-columns:repeat(2,1fr);}.kpi-grid .kpi-box:last-child{grid-column:span 2;}div.stButton>button[kind='secondary'],div.stButton>button[kind='primary']{font-size:0.8rem!important;padding:0.75rem 0.4rem!important;}}
</style>""", unsafe_allow_html=True)

RONDAS_TORNEO = [
    {"dia": "Sábado", "fecha": "9 Enero 2027",
     "ronda": "1ra Ronda", "hora": "2:00 PM"},
    {"dia": "Sábado", "fecha": "9 Enero 2027",
     "ronda": "2da Ronda", "hora": "6:00 PM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027",
     "ronda": "3ra Ronda", "hora": "9:00 PM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027",
     "ronda": "4ta Ronda", "hora": "2:00 PM"},
    {"dia": "Domingo", "fecha": "10 Enero 2027",
     "ronda": "5ta Ronda", "hora": "6:00 PM"},
]

FUTUROS_EVENTOS = [
    {
        "mes": "ENERO 2027",
        "fecha_txt": "9 y 10 de Enero, 2027",
        "fecha_ics": "20270109",
        "titulo": "Torneo Futuras Estrellas V2 (Evento Estelar)",
        "formato": "Clásico Infantil • 60m + 30s • Válido FIDE",
        "sede": "Acrópolis Business Mall, Distrito Nacional",
        "detalle": """Categorías Sub-1600, Sub-1800 y Up-1801.
Jugadores sin ELO FIDE participan en Sub-1600.
Premios en Gift Cards para los 3 primeros lugares.
Inscripción RD$650.""",
        "destacado": True
    },
    {
        "mes": "FEBRERO 2027",
        "fecha_txt": "20 de Febrero, 2027",
        "fecha_ics": "20270220",
        "titulo": "Copa Blitz Independencia Caribbean Chess",
        "formato": "Blitz • 3m + 2s • Sub-1600, Sub-1800 y Up-1801",
        "sede": "Acrópolis Business Mall, Santo Domingo",
        "detalle": """Torneo relámpago a 9 rondas sistema suizo
con premiación en efectivo y medallas por categoría.""",
        "destacado": False
    },
    {
        "mes": "MARZO 2027",
        "fecha_txt": "13 y 14 de Marzo, 2027",
        "fecha_ics": "20270313",
        "titulo": "Abierto Rápido Mentes Brillantes",
        "formato": "Rápido • 15m + 10s • Válido FIDE Rápido",
        "sede": "Santo Domingo, Distrito Nacional",
        "detalle": """Competencia activa de fin de semana diseñada
para fogueo competitivo de jugadores escolares y federados.""",
        "destacado": False
    },
    {
        "mes": "ABRIL 2027",
        "fecha_txt": "17 y 18 de Abril, 2027",
        "fecha_ics": "20270417",
        "titulo": "Torneo Futuras Estrellas V3",
        "formato": "Clásico Infantil • 60m + 30s • Válido FIDE",
        "sede": "Acrópolis Business Mall, Distrito Nacional",
        "detalle": """Tercera edición del circuito infantil clásico
de Caribbean Chess Academy con ranking FIDE oficial.""",
        "destacado": False
    },
]

def generar_ics(titulo, fecha_str, sede, descripcion):
    desc_limpia = descripcion.replace("\n", " ")
    return (
        "BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\n"
        f"DTSTART;VALUE=DATE:{fecha_str}\n"
        f"SUMMARY:{titulo} - Caribbean Chess Academy\n"
        f"DESCRIPTION:{desc_limpia}\n"
        f"LOCATION:{sede}\n"
        "END:VEVENT\nEND:VCALENDAR"
    )

logo_html = get_cca_logo_html()
st.markdown(
    f"""<div class="hero-white-card">{logo_html}<div style="flex:1;">
<div class="pill-badge">★ ¡Ven y demuestra tu talento en el tablero! • Válido FIDE</div>
<h1 class="hero-main-title">FUTURAS <span>ESTRELLAS</span> <span class="hero-v2-tag">V2</span></h1>
<div class="hero-subtitle">★ TORNEO DE AJEDREZ CLÁSICO INFANTIL • <strong>9 Y 10 ENERO 2027</strong> ★</div>
<p style="color:#475569;font-size:0.9rem;margin:10px 0 0 0;font-weight:500;">
Organizado por <strong>Caribbean Chess Academy</strong> en <strong>Acrópolis Business Mall</strong>, Distrito Nacional.</p>
</div></div>""",
    unsafe_allow_html=True
)

RELOJ_HTML = """<!DOCTYPE html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0;padding:0;}
body{background:transparent;font-family:Montserrat,sans-serif;}
.timer-bar{background:#0F1E36;border-radius:0 0 22px 22px;padding:14px 16px 16px 16px;box-shadow:0 12px 30px rgba(15,30,54,0.14);}
.timer-title{font-size:0.72rem;color:#EAB308;font-weight:800;text-align:center;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;max-width:520px;margin:0 auto;}
.box{background:#FFFFFF;border-radius:12px;padding:9px 4px;text-align:center;}
.num{font-size:1.65rem;font-weight:900;color:#0F1E36;line-height:1;}
.num.sec{color:#D90429;}
.lbl{font-size:0.62rem;color:#64748B;text-transform:uppercase;margin-top:3px;font-weight:800;}
</style></head><body><div class="timer-bar">
<div class="timer-title">⏳ Inicio 1ra Ronda • Sábado 9 de Enero 2027 (2:00 PM)</div>
<div class="grid">
<div class="box"><div class="num" id="d">--</div><div class="lbl">Días</div></div>
<div class="box"><div class="num" id="h">--</div><div class="lbl">Horas</div></div>
<div class="box"><div class="num" id="m">--</div><div class="lbl">Min</div></div>
<div class="box"><div class="num sec" id="s">--</div><div class="lbl">Seg</div></div>
</div></div><script>
const targetDate=new Date("2027-01-09T14:00:00-04:00").getTime();
function updateTimer(){
const now=new Date().getTime();
const distance=targetDate-now;
if(distance<=0){return;}
document.getElementById("d").innerText=String(Math.floor(distance/(1000*60*60*24))).padStart(2,"0");
document.getElementById("h").innerText=String(Math.floor((distance%(1000*60*60*24))/(1000*60*60))).padStart(2,"0");
document.getElementById("m").innerText=String(Math.floor((distance%(1000*60*60))/(1000*60))).padStart(2,"0");
document.getElementById("s").innerText=String(Math.floor((distance%(1000*60))/1000)).padStart(2,"0");
}updateTimer();setInterval(updateTimer,1000);
</script></body></html>"""
components.html(RELOJ_HTML, height=128)

st.markdown(
    """<div class="nav-prompt">
    Explora la información del torneo y próximos eventos
    </div>""",
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4 = st.columns(4, gap="small")
with nav1:
    t1 = "primary" if st.session_state.vista_cca == "torneo" else "secondary"
    if st.button("♔ TORNEO V2", type=t1, use_container_width=True):
        st.session_state.vista_cca = "torneo"
        st.rerun()
with nav2:
    t2 = "primary" if st.session_state.vista_cca == "rondas" else "secondary"
    if st.button("📅 RONDAS V2", type=t2, use_container_width=True):
        st.session_state.vista_cca = "rondas"
        st.rerun()
with nav3:
    t3 = "primary" if st.session_state.vista_cca == "eventos" else "secondary"
    if st.button("🏆 FUTUROS EVENTOS", type=t3, use_container_width=True):
        st.session_state.vista_cca = "eventos"
        st.rerun()
with nav4:
    t4 = "primary" if st.session_state.vista_cca == "inscripcion" else "secondary"
    if st.button("📝 INSCRIPCIÓN", type=t4, use_container_width=True):
        st.session_state.vista_cca = "inscripcion"
        st.rerun()

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

if st.session_state.vista_cca == "torneo":
    st.markdown("""<div class="kpi-grid">
<div class="kpi-box"><div class="kpi-icon">⏱️</div><div class="kpi-title">Ritmo Clásico</div><div class="kpi-val">60 Min + 30 Seg</div></div>
<div class="kpi-box"><div class="kpi-icon">🌐</div><div class="kpi-title">Aval Oficial</div><div class="kpi-val">Rating FIDE</div></div>
<div class="kpi-box"><div class="kpi-icon">🎁</div><div class="kpi-title">Premios Top 3</div><div class="kpi-val">Gift Cards</div></div>
<div class="kpi-box"><div class="kpi-icon">💵</div><div class="kpi-title">Inscripción</div><div class="kpi-val" style="color:#D90429;">RD$ 650</div></div>
<div class="kpi-box"><div class="kpi-icon">📍</div><div class="kpi-title">Sede Oficial</div><div class="kpi-val">Acrópolis Mall</div></div>
</div>""", unsafe_allow_html=True)
    col_cat, col_info = st.columns([1.1, 1], gap="large")
    with col_cat:
        st.markdown("#### 🎯 Categorías Oficiales por Rating ELO")
        st.markdown("""<div class="cat-card"><div><div class="cat-title">♟️ SUB <span>1600</span></div><div style="font-size:0.8rem;color:#64748B;font-weight:600;margin-top:2px;">ELO menor a 1600 y jugadores sin ELO FIDE</div></div><div class="cat-badge">Clásico Infantil</div></div>
<div class="cat-card"><div><div class="cat-title">♞ SUB <span>1800</span></div><div style="font-size:0.8rem;color:#64748B;font-weight:600;margin-top:2px;">Jugadores con rating ELO entre 1600 y 1799</div></div><div class="cat-badge">Clásico Infantil</div></div>
<div class="cat-card"><div><div class="cat-title">♔ UP <span>1801</span></div><div style="font-size:0.8rem;color:#64748B;font-weight:600;margin-top:2px;">Jugadores con rating ELO de 1801 en adelante</div></div><div class="cat-badge">Élite Infantil</div></div>
<div class="elo-note">ℹ️ Nota: Los jugadores sin ELO FIDE solo pueden participar en la categoría Sub-1600.</div>""", unsafe_allow_html=True)
    with col_info:
        st.markdown("#### 🏆 Premiación y Sede")
        st.markdown("""<div style="background:#FFFBEB;border:1.5px solid #FDE68A;border-radius:14px;padding:16px;margin-bottom:12px;">
<div style="font-weight:900;color:#92400E;font-size:1rem;">🎁 PREMIOS ESPECIALES EN GIFT CARDS</div>
<p style="color:#78350F;font-size:0.86rem;margin:6px 0 0 0;line-height:1.45;">Se otorgarán <strong>Gift Cards especiales para los 3 primeros lugares</strong> de cada categoría oficial (Sub-1600, Sub-1800 y Up-1801).</p></div>
<div style="background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:14px;padding:16px;">
<div style="font-weight:900;color:#0F1E36;font-size:0.98rem;">📍 UBICACIÓN DEL TORNEO</div>
<p style="color:#475569;font-size:0.86rem;margin:6px 0 10px 0;line-height:1.45;"><strong>Acrópolis Business Mall</strong>, Av. Winston Churchill, Distrito Nacional, Santo Domingo.</p>
<a href="https://maps.google.com/?q=Acropolis+Business+Mall+Santo+Domingo" target="_blank" style="display:inline-block;background:#0F1E36;color:#FFFFFF;font-size:0.78rem;font-weight:800;padding:8px 14px;border-radius:8px;text-decoration:none;text-transform:uppercase;">🗺️ Abrir en Google Maps</a></div>""", unsafe_allow_html=True)

elif st.session_state.vista_cca == "rondas":
    st.markdown("#### 📅 Calendario Oficial de Rondas — Futuras Estrellas V2")
    st.caption(
        """Sistema Suizo a 5 rondas • Ritmo Clásico:
        60 minutos + 30 segundos por jugada."""
    )
    for r in RONDAS_TORNEO:
        st.markdown(
            f"""<div class="round-row"><div>
<div class="round-day">{r["dia"]}</div>
<div class="round-date">{r["fecha"]}</div></div>
<div class="round-badge"><div class="round-num">{r["ronda"]}</div>
<div class="round-time">🕒 {r["hora"]}</div></div></div>""",
            unsafe_allow_html=True
        )
    st.download_button(
        label="📲 AGENDAR TORNEO V2 EN MI CALENDARIO (.ICS)",
        data=generar_ics(
            "Torneo Futuras Estrellas V2",
            "20270109",
            "Acrópolis Business Mall, Santo Domingo",
            "Torneo Clásico Infantil 60m+30s válido FIDE."
        ),
        file_name="futuras_estrellas_v2_caribbean_chess.ics",
        mime="text/calendar",
        use_container_width=True
    )

elif st.session_state.vista_cca == "eventos":
    st.markdown(
        "#### 🏆 Calendario de Próximos Eventos — Caribbean Chess Academy"
    )
    st.caption(
        """Agenda nuestras próximas competencias oficiales
        y reserva tu participación con tiempo."""
    )
    opciones_mes = ["Todos los eventos"] + [e["mes"] for e in FUTUROS_EVENTOS]
    filtro_mes = st.selectbox(
        "Filtrar por mes:", opciones_mes, label_visibility="collapsed"
    )
    eventos_visibles = [
        e for e in FUTUROS_EVENTOS
        if filtro_mes == "Todos los eventos" or e["mes"] == filtro_mes
    ]

    for idx, ev in enumerate(eventos_visibles):
        clase_card = "event-card featured" if ev["destacado"] else "event-card"
        clase_tag = "ev-tag red" if ev["destacado"] else "ev-tag"
        st.markdown(
            f"""<div class="{clase_card}">
<span class="{clase_tag}">🗓️ {ev["fecha_txt"]}</span>
<div class="ev-title">{ev["titulo"]}</div>
<div class="ev-meta">♟️ {ev["formato"]} &nbsp;|&nbsp; 📍 {ev["sede"]}</div>
<p class="ev-desc">{ev["detalle"]}</p></div>""",
            unsafe_allow_html=True
        )
        b1, b2 = st.columns(2, gap="small")
        with b1:
            st.download_button(
                label="📅 Guardar Fecha (.ICS)",
                data=generar_ics(
                    ev["titulo"], ev["fecha_ics"], ev["sede"], ev["detalle"]
                ),
                file_name=f"evento_cca_{idx}.ics",
                mime="text/calendar",
                key=f"ics_ev_{idx}",
                use_container_width=True
            )
        with b2:
            texto_consulta = (
                f"Hola Caribbean Chess Academy, deseo información sobre: "
                f"{ev['titulo']} ({ev['fecha_txt']})."
            )
            msg_ev = urllib.parse.quote(texto_consulta)
            st.link_button(
                label="📲 Consultar por WhatsApp",
                url=f"https://wa.me/18494403222?text={msg_ev}",
                use_container_width=True
            )
        st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)

elif st.session_state.vista_cca == "inscripcion":
    st.markdown("#### 📝 Formulario de Inscripción Oficial")
    st.caption(
        """Costo de inscripción Futuras Estrellas V2: **RD$650** •
        Los jugadores sin ELO FIDE participan en **Sub-1600**."""
    )
    with st.form("form_cca"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            nombre = st.text_input(
                "👤 Nombre Completo del Jugador *",
                placeholder="Ej. Mateo Gómez"
            )
            torneo_sel = st.selectbox(
                "🏆 Evento / Torneo *",
                [e["titulo"] for e in FUTUROS_EVENTOS]
            )
            id_fide = st.text_input(
                "🌐 ID FIDE / ELO (Si aplica)",
                placeholder="Ej. 6409876 (ELO: 1580) o Sin ELO"
            )
        with c2:
            categoria = st.selectbox(
                "🎯 Categoría por ELO *",
                ["Sub-1600", "Sub-1800", "Up-1801"]
            )
            telefono = st.text_input(
                "📱 WhatsApp del Padre / Tutor *",
                placeholder="Ej. 849-555-0123"
            )
            pago_metodo = st.selectbox(
                "💳 Método de Pago Realizado *",
                [
                    "Transferencia Bancaria (RD$650)",
                    "Depósito Bancario (RD$650)"
                ]
            )
        st.markdown(
            "<hr style='margin:12px 0;border-color:#E2E8F0;'>",
            unsafe_allow_html=True
        )
        etiqueta_up = """📸 Adjuntar Comprobante de Pago (Obligatorio) *"""
        ayuda_up = """Sube una foto o captura de la transferencia."""
        comprobante = st.file_uploader(
            etiqueta_up,
            type=["png", "jpg", "jpeg", "webp", "pdf"],
            help=ayuda_up
        )
        boton_txt = """✅ VALIDAR COMPROBANTE Y GENERAR INSCRIPCIÓN"""
        submit = st.form_submit_button(
            boton_txt,
            use_container_width=True
        )

    if submit:
        if not nombre or not telefono:
            st.error(
                """⚠️ Completa el nombre del jugador y el WhatsApp."""
            )
        elif categoria in ["Sub-1800", "Up-1801"] and not id_fide.strip():
            st.error(
                """⚠️ Para Sub-1800 o Up-1801 debes indicar tu ID FIDE / ELO.
                Jugadores sin ELO deben inscribirse en Sub-1600."""
            )
        elif comprobante is None:
            st.error(
                """🚫 Comprobante obligatorio: sube una foto o captura
                del pago para completar tu inscripción."""
            )
        else:
            elo_txt = (
                id_fide.strip()
                if id_fide.strip()
                else "Sin ELO FIDE (Categoría Sub-1600)"
            )
            msg_wa = (
                f"*INSCRIPCIÓN CONFIRMADA - CARIBBEAN CHESS ACADEMY*%0A"
                f"• *Torneo:* {urllib.parse.quote(torneo_sel)}%0A"
                f"• *Jugador:* {urllib.parse.quote(nombre)}%0A"
                f"• *ID/ELO FIDE:* {urllib.parse.quote(elo_txt)}%0A"
                f"• *Categoría:* {urllib.parse.quote(categoria)}%0A"
                f"• *Pago:* {urllib.parse.quote(pago_metodo)}%0A"
                f"• *Comprobante:* Adjunto "
                f"({urllib.parse.quote(comprobante.name)})%0A"
                f"• *Contacto:* {urllib.parse.quote(telefono)}"
            )
            st.success(
                f"""✅ ¡Comprobante verificado ({comprobante.name}) y
                ficha lista para {nombre}!"""
            )
            if comprobante.type.startswith("image"):
                with st.expander(
                    "👁️ Ver vista previa del comprobante",
                    expanded=True
                ):
                    st.image(comprobante, width=260)
            st.info(
                """📲 Último paso: pulsa el botón verde abajo para abrir
                WhatsApp y adjunta esta misma imagen en el chat."""
            )
            st.link_button(
                "📲 ENVIAR FICHA POR WHATSAPP (849-440-3222)",
                f"https://wa.me/18494403222?text={msg_wa}",
                use_container_width=True
            )

texto_wa_fijo = (
    "Hola Caribbean Chess Academy, deseo más información "
    "sobre sus torneos y próximos eventos."
)
msg_directo = urllib.parse.quote(texto_wa_fijo)
st.markdown(
    f"""<div class="sticky-bottom-bar">
<a href="https://wa.me/18494403222?text={msg_directo}"
target="_blank" class="sticky-wa-btn">
💬 MÁS INFORMACIÓN E INSCRIPCIONES • 849-440-3222</a></div>""",
    unsafe_allow_html=True
)
