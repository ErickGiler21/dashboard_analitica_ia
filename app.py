import streamlit as st

from dashboard_ia.data import load_csv, prepare
from dashboard_ia.styles import apply_styles
from dashboard_ia.views import (
    render_aprendizaje,
    render_comentarios,
    render_innovacion,
    render_participacion,
    render_reporte,
    render_sidebar,
    render_summary,
)


st.set_page_config(
    page_title="Panel de Analítica IA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()

selected_view = render_sidebar()
uploaded = st.session_state.get("csv_upload")

try:
    df = prepare(load_csv(uploaded))
except Exception as e:
    st.error(f"No se pudo cargar el panel: {e}")
    st.stop()

source = "Archivo CSV cargado" if uploaded else "Datos de ejemplo"

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
