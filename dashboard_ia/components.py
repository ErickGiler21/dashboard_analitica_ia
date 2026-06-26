from datetime import datetime
from html import escape
from pathlib import Path

import streamlit as st


def metric(label, value, icon, help_text):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{escape(str(label))}</div>
            <div class="metric-value">{escape(str(value))}</div>
            <div class="metric-help">{escape(str(help_text))}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_grid(items):
    cards = []
    for label, value, icon, help_text in items:
        cards.append(
            '<div class="metric-card">'
            f'<div class="metric-icon">{icon}</div>'
            f'<div class="metric-label">{escape(str(label))}</div>'
            f'<div class="metric-value">{escape(str(value))}</div>'
            f'<div class="metric-help">{escape(str(help_text))}</div>'
            "</div>"
        )
    st.markdown(f'<div class="metrics-grid">{"".join(cards)}</div>', unsafe_allow_html=True)


def section(title, subtitle):
    st.markdown(
        f'<div class="section-title">{escape(str(title))}</div><div class="section-sub">{escape(str(subtitle))}</div>',
        unsafe_allow_html=True,
    )


def section_label(text):
    st.markdown(f'<div class="summary-section-label">{escape(str(text))}</div>', unsafe_allow_html=True)


def tag(value, kind):
    if kind == "finalizacion":
        n = float(str(value))
        cls = "tag-ok" if n >= 85 else "tag-warn" if n >= 70 else "tag-bad"
        return f'<span class="tag {cls}">{n:.1f}%</span>'

    if kind == "mejora":
        n = float(str(value))
        cls = "tag-ok" if n >= 4 else "tag-warn" if n >= 2 else "tag-bad"
        return f'<span class="tag {cls}">{n:.1f}</span>'

    cls = {
        "Positivo": "tag-ok",
        "Neutral": "tag-neutral",
        "Dificultad detectada": "tag-bad",
    }.get(str(value), "tag-neutral")
    return f'<span class="tag {cls}">{escape(str(value))}</span>'


def pro_table(data, cols=None, height=430):
    if cols is None:
        cols = list(data.columns)

    labels = {
        "id_participante": "Id Participante",
        "rubro_artesanal": "Rubro Artesanal",
        "actividades_completadas": "Actividades Completadas",
        "total_actividades": "Total Actividades",
        "finalizacion": "Finalización",
        "pretest": "Pretest",
        "postest": "Postest",
        "mejora_aprendizaje": "Mejora Aprendizaje",
        "comentario_abierto": "Comentario Abierto",
        "categoria_comentario": "Categoría",
        "usabilidad": "Usabilidad",
        "satisfaccion": "Satisfacción",
    }

    table_html = [f'<div class="pro-table-wrap" style="max-height:{height}px"><table class="pro-table"><thead><tr>']

    for col in cols:
        title = labels.get(col, col.replace("_", " ").title())
        table_html.append(f"<th>{escape(str(title))}</th>")

    table_html.append("</tr></thead><tbody>")

    for _, row in data[cols].iterrows():
        table_html.append("<tr>")
        for col in cols:
            value = row[col]
            if col == "finalizacion":
                cell = tag(value, "finalizacion")
            elif col == "mejora_aprendizaje":
                cell = tag(value, "mejora")
            elif col == "categoria_comentario":
                cell = tag(value, "categoria")
            elif isinstance(value, float):
                cell = escape(f"{value:.1f}")
            else:
                cell = escape(str(value))
            table_html.append(f"<td>{cell}</td>")
        table_html.append("</tr>")

    table_html.append("</tbody></table></div>")
    st.markdown("".join(table_html), unsafe_allow_html=True)


def control_panel(source, total_participants):
    st.markdown(
        f"""
        <div class="summary-control">
            <div class="summary-control-head">
                <div class="summary-control-icon">📊</div>
                <div>
                    <div class="summary-control-title">Analítica IA</div>
                    <div class="summary-control-sub">Panel de control</div>
                </div>
            </div>
            <div class="control-grid">
                <div class="control-item">
                    <div class="control-label">Estado</div>
                    <div class="control-value">✅ Datos listos</div>
                </div>
                <div class="control-item">
                    <div class="control-label">Fuente</div>
                    <div class="control-value">{escape(source)}</div>
                </div>
                <div class="control-item">
                    <div class="control-label">Participantes</div>
                    <div class="control-value">{total_participants}</div>
                </div>
                <div class="control-item">
                    <div class="control-label">Actualizado</div>
                    <div class="control-value">{datetime.now():%d/%m/%Y %H:%M}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def upload_panel():
    st.markdown('<div class="tool-title">Herramientas</div><div class="tool-sub">Subir archivo CSV</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Subir archivo CSV", type=["csv"], key="csv_upload")

    template_path = Path(__file__).resolve().parent.parent / "plantilla_datos.csv"
    if template_path.exists():
        with open(template_path, "rb") as f:
            st.download_button(
                "⬇️ Descargar plantilla CSV",
                f,
                file_name="plantilla_datos.csv",
                mime="text/csv",
            )

    return uploaded_file


def summary_insights(df, recommendations):
    recs = recommendations(df)
    best = df.sort_values("finalizacion", ascending=False).iloc[0]
    risk_count = int((df["finalizacion"] < 70).sum())
    positive_pct = df["categoria_comentario"].eq("Positivo").mean() * 100 if len(df) else 0

    st.markdown(
        f"""
        <div class="summary-insights">
            <div class="insight-card">
                <div class="insight-title">Mayor avance</div>
                <div class="insight-value">{escape(str(best["id_participante"]))} · {float(best["finalizacion"]):.1f}%</div>
                <div class="insight-copy">Participante con mejor cumplimiento de actividades.</div>
            </div>
            <div class="insight-card">
                <div class="insight-title">Atención docente</div>
                <div class="insight-value">{risk_count}</div>
                <div class="insight-copy">Participantes por debajo del 70% de finalización.</div>
            </div>
            <div class="insight-card">
                <div class="insight-title">Clima del curso</div>
                <div class="insight-value">{positive_pct:.1f}%</div>
                <div class="insight-copy">Comentarios clasificados como positivos.</div>
            </div>
            <div class="insight-card">
                <div class="insight-title">Recomendación principal</div>
                <div class="insight-value">Acción sugerida</div>
                <div class="insight-copy">{escape(recs[0])}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
