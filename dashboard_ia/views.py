from html import escape

import streamlit as st

from .charts import show_criterios_innovacion, show_finalizacion, show_innovacion, show_mejora, show_pie, show_prepost
from .components import control_panel, metric_grid, pro_table, section, section_label, summary_insights, upload_panel
from .constants import CRITERIOS, NAV_OPTIONS
from .reports import recommendations, report_text


def render_sidebar():
    with st.sidebar:
        st.markdown(
            '<div class="brand"><div class="brand-icon">📊</div><div><div class="brand-title">Analítica IA</div><div class="brand-sub">Panel de control</div></div></div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="nav-label">Secciones</div>', unsafe_allow_html=True)
        selected_view = st.radio(
            "Secciones",
            NAV_OPTIONS,
            label_visibility="collapsed",
        )
        st.markdown("---")
        st.caption("Analítica educativa para Moodle")
    return selected_view


def render_quick_nav(selected_view):
    if (
        "quick_nav" not in st.session_state
        or st.session_state.get("_last_sidebar_view") != selected_view
    ):
        st.session_state.quick_nav = selected_view
        st.session_state._last_sidebar_view = selected_view

    with st.expander("☰ Navegación rápida", expanded=False):
        st.caption("Úsala solo si el panel izquierdo queda oculto en el navegador.")
        return st.radio(
            "Navegación rápida",
            NAV_OPTIONS,
            horizontal=True,
            label_visibility="collapsed",
            key="quick_nav",
        )


def render_summary_header():
    st.markdown(
        '<div class="main-title"><h1>Panel de Analítica Asistida por IA</h1><p>Seguimiento de participación, aprendizaje, innovación y satisfacción del curso.</p></div>',
        unsafe_allow_html=True,
    )


def render_summary_upload():
    with st.container(border=True):
        uploaded = upload_panel()
    return uploaded


def render_metrics(df):
    metric_grid(
        [
            ("Participantes", len(df), "👥", "Total registrados"),
            ("Finalización", f"{df['finalizacion'].mean():.1f}%", "📈", "Promedio del curso"),
            ("Mejora", f"{df['mejora_aprendizaje'].mean():.1f}", "⭐", "Postest - pretest"),
            ("Innovación", f"{df['indice_innovacion'].mean():.1f}/4", "💡", "Promedio de rúbrica"),
            ("Pretest", f"{df['pretest'].mean():.1f}", "📉", "Diagnóstico inicial"),
            ("Postest", f"{df['postest'].mean():.1f}", "🚀", "Evaluación final"),
            ("Satisfacción", f"{df['satisfaccion'].mean():.1f}/5" if "satisfaccion" in df else "N/D", "😊", "Percepción"),
            ("Usabilidad", f"{df['usabilidad'].mean():.1f}/5" if "usabilidad" in df else "N/D", "🛡️", "Facilidad de uso"),
        ]
    )


def render_summary(df, source):
    render_summary_header()

    section_label("Estado del archivo")
    control_panel(source, len(df))

    left_col, right_col = st.columns([0.34, 0.66])
    with left_col:
        render_summary_upload()
    with right_col:
        section_label("Indicadores principales")
        render_metrics(df)

    section_label("Lectura rápida")
    summary_insights(df, recommendations)

    with st.container(border=True):
        section("Vista rápida por participante", "Resumen compacto sin gráficos para revisar el estado general.")
        pro_table(
            df.sort_values("finalizacion", ascending=False).head(10),
            [
                "id_participante",
                "actividades_completadas",
                "total_actividades",
                "finalizacion",
                "pretest",
                "postest",
                "mejora_aprendizaje",
            ],
            360,
        )


def render_participacion(df):
    with st.container(border=True):
        section("Participación y finalización", "Detalle del avance individual y cumplimiento de actividades.")
        show_finalizacion(df)
        pro_table(
            df,
            [x for x in ["id_participante", "rubro_artesanal", "actividades_completadas", "total_actividades", "finalizacion"] if x in df],
            430,
        )


def render_aprendizaje(df):
    with st.container(border=True):
        section("Aprendizaje", "Impacto del curso medido con diagnóstico inicial, evaluación final y mejora individual.")
        show_prepost(df)
        show_mejora(df)


def render_innovacion(df):
    with st.container(border=True):
        section("Innovación", "Evaluación de creatividad, uso de IA, comparación del rediseño y presentación.")
        show_innovacion(df)

        prom = df[CRITERIOS].mean().reset_index()
        prom.columns = ["Criterio", "Promedio"]
        prom["Criterio"] = prom["Criterio"].astype(str).str.replace("_", " ").str.title()
        show_criterios_innovacion(prom)


def render_comentarios(df):
    with st.container(border=True):
        section("Comentarios abiertos", "Lectura rápida con clasificación automática.")
        show_pie(df)
        pro_table(df, ["id_participante", "comentario_abierto", "categoria_comentario"], 440)


def render_reporte(df):
    with st.container(border=True):
        section("Reporte ejecutivo", "Recomendaciones generadas a partir de los indicadores actuales.")
        recs = recommendations(df)

        for rec in recs:
            st.markdown(f'<div class="report-note">✨ {escape(rec)}</div>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="report-grid">
                <div class="report-card">
                    <div class="report-label">Participantes</div>
                    <div class="report-value">{len(df)}</div>
                </div>
                <div class="report-card">
                    <div class="report-label">Finalización</div>
                    <div class="report-value">{df["finalizacion"].mean():.1f}%</div>
                </div>
                <div class="report-card">
                    <div class="report-label">Mejora</div>
                    <div class="report-value">{df["mejora_aprendizaje"].mean():.1f}</div>
                </div>
                <div class="report-card">
                    <div class="report-label">Satisfacción</div>
                    <div class="report-value">{df["satisfaccion"].mean():.1f}/5</div>
                </div>
            </div>
            <div class="report-panel">
                <div class="report-panel-title">Resumen del reporte</div>
                <div class="report-line"><span>Promedio pretest</span><b>{df["pretest"].mean():.2f}</b></div>
                <div class="report-line"><span>Promedio postest</span><b>{df["postest"].mean():.2f}</b></div>
                <div class="report-line"><span>Innovación promedio</span><b>{df["indice_innovacion"].mean():.2f}/4</b></div>
                <div class="report-line"><span>Usabilidad promedio</span><b>{df["usabilidad"].mean():.2f}/5</b></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        txt = report_text(df, recs)
        st.download_button("⬇️ Descargar reporte TXT", txt, file_name="reporte_analitica_ia.txt", mime="text/plain")
