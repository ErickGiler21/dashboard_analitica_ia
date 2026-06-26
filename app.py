import streamlit as st

from dashboard_ia.data import load_csv, prepare
from dashboard_ia.styles import apply_styles
from dashboard_ia.views import (
    render_aprendizaje,
    render_comentarios,
    render_innovacion,
    render_left_nav,
    render_open_nav_button,
    render_participacion,
    render_reporte,
    render_summary,
)


st.set_page_config(
    page_title="Panel de Analítica IA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()

if "left_nav_open" not in st.session_state:
    st.session_state.left_nav_open = True

uploaded = st.session_state.get("csv_upload")

try:
    df = prepare(load_csv(uploaded))
except Exception as e:
    st.error(f"No se pudo cargar el panel: {e}")
    st.stop()

source = "Archivo CSV cargado" if uploaded else "Datos de ejemplo"

if st.session_state.left_nav_open:
    nav_col, content_col = st.columns([0.24, 0.76], gap="large")
    with nav_col:
        st.markdown('<div class="custom-sidebar">', unsafe_allow_html=True)
        selected_view = render_left_nav()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    selected_view = render_open_nav_button()
    content_col = st.container()

with content_col:
    if selected_view == "📌 Resumen":
        render_summary(df, source)
    elif selected_view == "🧩 Participación":
        render_participacion(df)
    elif selected_view == "📘 Aprendizaje":
        render_aprendizaje(df)
    elif selected_view == "🎨 Innovación":
        render_innovacion(df)
    elif selected_view == "💬 Comentarios":
        render_comentarios(df)
    elif selected_view == "📄 Reporte":
        render_reporte(df)
