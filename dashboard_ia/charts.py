import plotly.express as px
import streamlit as st

from .constants import COLORS


CHART_CONFIG = {
    "displayModeBar": False,
    "displaylogo": False,
    "responsive": True,
    "modeBarButtonsToRemove": ["lasso2d", "select2d"],
}


def apply_chart_layout(fig, height=520):
    fig.update_layout(
        height=height,
        margin=dict(l=36, r=26, t=70, b=72),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#0F172A", family="Inter, Arial, sans-serif", size=13),
        title_font=dict(size=20, color="#0F172A"),
        hoverlabel=dict(bgcolor="#0F172A", font_size=13, font_color="white"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="#0F172A", size=12),
        ),
    )
    fig.update_xaxes(
        showgrid=False,
        linecolor="#CBD5E1",
        tickfont=dict(color="#0F172A", size=12),
        title_font=dict(color="#0F172A", size=13),
    )
    fig.update_yaxes(
        gridcolor="#E2E8F0",
        linecolor="#CBD5E1",
        tickfont=dict(color="#0F172A", size=12),
        title_font=dict(color="#0F172A", size=13),
    )
    return fig


def render_plotly(fig):
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)


def top_participants(data, sort_col):
    return data.sort_values(sort_col, ascending=False).head(20).copy()


def show_finalizacion(data):
    top = top_participants(data, "finalizacion")
    top["finalizacion_label"] = top["finalizacion"].map(lambda x: f"{x:.1f}%")

    fig = px.bar(
        top,
        x="id_participante",
        y="finalizacion",
        color="id_participante",
        color_discrete_sequence=COLORS,
        text="finalizacion_label",
        title="Top 20 participantes por finalización",
        labels={"id_participante": "Participante", "finalizacion": "Finalización (%)"},
        hover_data={
            "id_participante": True,
            "actividades_completadas": True,
            "total_actividades": True,
            "finalizacion": ":.1f",
        },
    )
    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        customdata=top[["actividades_completadas", "total_actividades", "pretest", "postest"]].to_numpy(),
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Finalización: %{y:.1f}%<br>"
            "Actividades: %{customdata[0]}/%{customdata[1]}<br>"
            "Pretest: %{customdata[2]}<br>"
            "Postest: %{customdata[3]}"
            "<extra></extra>"
        ),
    )
    fig.update_layout(showlegend=False)
    fig.update_yaxes(range=[0, 110], title="Finalización (%)")
    fig.update_xaxes(title="Participante")
    render_plotly(apply_chart_layout(fig))


def show_prepost(data):
    top = top_participants(data, "finalizacion")
    long_df = top.melt(
        id_vars=["id_participante", "finalizacion", "mejora_aprendizaje"],
        value_vars=["pretest", "postest"],
        var_name="Evaluación",
        value_name="Puntaje",
    )
    long_df["Evaluación"] = long_df["Evaluación"].map({"pretest": "Pretest", "postest": "Postest"})

    fig = px.bar(
        long_df,
        x="id_participante",
        y="Puntaje",
        color="Evaluación",
        barmode="group",
        color_discrete_map={"Pretest": "#93C5FD", "Postest": "#2563EB"},
        title="Pretest vs postest",
        labels={"id_participante": "Participante"},
        hover_data={"finalizacion": ":.1f", "mejora_aprendizaje": ":.1f"},
    )
    fig.update_traces(hovertemplate="<b>%{x}</b><br>Puntaje: %{y:.1f}<extra></extra>")
    fig.update_yaxes(range=[0, 10.8], title="Puntaje")
    render_plotly(apply_chart_layout(fig))


def show_mejora(data):
    top = top_participants(data, "finalizacion")
    fig = px.line(
        top,
        x="id_participante",
        y="mejora_aprendizaje",
        markers=True,
        title="Mejora de aprendizaje",
        labels={"id_participante": "Participante", "mejora_aprendizaje": "Puntos de mejora"},
        hover_data={"pretest": ":.1f", "postest": ":.1f", "finalizacion": ":.1f"},
    )
    fig.update_traces(
        line=dict(color="#7C3AED", width=4),
        marker=dict(size=9, color="#7C3AED"),
        fill="tozeroy",
        fillcolor="rgba(124,58,237,.14)",
        customdata=top[["pretest", "postest", "finalizacion"]].to_numpy(),
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Mejora: %{y:.1f} puntos<br>"
            "Pretest: %{customdata[0]}<br>"
            "Postest: %{customdata[1]}<br>"
            "Finalización: %{customdata[2]:.1f}%"
            "<extra></extra>"
        ),
    )
    render_plotly(apply_chart_layout(fig, height=440))


def show_pie(data):
    counts = data["categoria_comentario"].value_counts().reset_index()
    counts.columns = ["Categoría", "Cantidad"]
    total = counts["Cantidad"].sum()
    counts["Porcentaje"] = counts["Cantidad"] / total * 100
    counts["Etiqueta"] = counts["Porcentaje"].map(lambda x: f"{x:.1f}%")
    color_map = {
        "Positivo": "#10B981",
        "Neutral": "#F59E0B",
        "Dificultad detectada": "#EF4444",
    }

    fig = px.bar(
        counts,
        color="Categoría",
        color_discrete_map=color_map,
        x="Categoría",
        y="Cantidad",
        text="Etiqueta",
        title="Distribución de comentarios",
        labels={"Cantidad": "Comentarios"},
    )
    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        customdata=counts[["Porcentaje"]].to_numpy(),
        hovertemplate="<b>%{x}</b><br>Comentarios: %{y}<br>Porcentaje: %{customdata[0]:.1f}%<extra></extra>",
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title="Categoría")
    fig.update_yaxes(title="Comentarios", rangemode="tozero")
    render_plotly(apply_chart_layout(fig, height=430))


def show_innovacion(data):
    top = top_participants(data, "indice_innovacion")
    fig = px.bar(
        top,
        x="id_participante",
        y="indice_innovacion",
        color="indice_innovacion",
        color_continuous_scale=["#CFFAFE", "#06B6D4", "#0E7490"],
        text=top["indice_innovacion"].map(lambda x: f"{x:.1f}"),
        title="Índice de innovación por participante",
        labels={"id_participante": "Participante", "indice_innovacion": "Innovación"},
        hover_data={"analisis_producto": ":.1f", "uso_ia": ":.1f", "comparacion_rediseno": ":.1f", "presentacion_formato": ":.1f"},
    )
    fig.update_traces(
        textposition="outside",
        customdata=top[["analisis_producto", "uso_ia", "comparacion_rediseno", "presentacion_formato"]].to_numpy(),
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Innovación: %{y:.1f}/4<br>"
            "Análisis: %{customdata[0]:.1f}<br>"
            "Uso IA: %{customdata[1]:.1f}<br>"
            "Comparación: %{customdata[2]:.1f}<br>"
            "Presentación: %{customdata[3]:.1f}"
            "<extra></extra>"
        ),
    )
    fig.update_layout(coloraxis_showscale=False, showlegend=False)
    fig.update_yaxes(range=[0, 4.4], title="Índice de innovación")
    render_plotly(apply_chart_layout(fig))


def show_criterios_innovacion(prom):
    fig = px.bar(
        prom,
        x="Criterio",
        y="Promedio",
        color="Promedio",
        color_continuous_scale=["#E0F2FE", "#06B6D4", "#0E7490"],
        text=prom["Promedio"].map(lambda x: f"{x:.1f}"),
        title="Promedio por criterio de innovación",
    )
    fig.update_traces(textposition="outside", hovertemplate="<b>%{x}</b><br>Promedio: %{y:.1f}/4<extra></extra>")
    fig.update_layout(coloraxis_showscale=False, showlegend=False)
    fig.update_yaxes(range=[0, 4.4], title="Promedio")
    render_plotly(apply_chart_layout(fig, height=420))
