from datetime import datetime


def recommendations(df):
    recs = []

    if df["finalizacion"].mean() < 75:
        recs.append("Revisar la carga de actividades y fortalecer el acompañamiento para mejorar la finalización.")

    if df["mejora_aprendizaje"].mean() < 2:
        recs.append("Reforzar los ejercicios guiados antes de la evaluación final.")

    if (df["categoria_comentario"] == "Dificultad detectada").any():
        recs.append("Analizar los comentarios con dificultad detectada para ajustar instrucciones, contenidos y soporte técnico.")

    if "usabilidad" in df.columns and df["usabilidad"].mean() < 3.8:
        recs.append("Simplificar la navegación y añadir una guía visual de entrega de actividades.")

    if not recs:
        recs.append("Los indicadores generales son favorables. Mantener seguimiento periódico por participante.")

    return recs


def report_text(df, recs):
    lines = [
        "REPORTE FINAL - PANEL DE ANALÍTICA ASISTIDA POR IA",
        f"Fecha: {datetime.now():%d/%m/%Y %H:%M}",
        "",
        f"Participantes: {len(df)}",
    ]

    items = [
        ("finalizacion", "Finalización promedio", "%"),
        ("pretest", "Promedio pretest", ""),
        ("postest", "Promedio postest", ""),
        ("mejora_aprendizaje", "Mejora promedio", ""),
        ("indice_innovacion", "Innovación promedio", "/4"),
        ("usabilidad", "Usabilidad promedio", "/5"),
        ("satisfaccion", "Satisfacción promedio", "/5"),
    ]

    for col, label, suffix in items:
        if col in df.columns:
            lines.append(f"{label}: {df[col].mean():.2f}{suffix}")

    lines += ["", "RECOMENDACIONES:"]
    lines += [f"- {rec}" for rec in recs]
    return "\n".join(lines)
