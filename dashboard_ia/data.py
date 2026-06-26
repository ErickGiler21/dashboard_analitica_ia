from pathlib import Path

import pandas as pd
import streamlit as st

from .constants import CRITERIOS


def classify_comment(text):
    t = str(text).lower()
    bad_words = ["difícil", "dificil", "confuso", "problema", "no entend", "complicado", "dificultad", "fall", "costó", "costo"]
    good_words = ["excelente", "útil", "util", "aprend", "interesante", "mejor", "innov", "gust", "ayud"]

    if any(word in t for word in bad_words):
        return "Dificultad detectada"
    if any(word in t for word in good_words):
        return "Positivo"
    return "Neutral"


@st.cache_data
def load_csv(uploaded_file):
    example_path = Path(__file__).resolve().parent.parent / "datos_ejemplo.csv"
    if uploaded_file is None:
        return pd.read_csv(example_path)
    return pd.read_csv(uploaded_file)


def prepare(df):
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]

    if "correccion_rediseno" in df.columns and "comparacion_rediseno" not in df.columns:
        df["comparacion_rediseno"] = df["correccion_rediseno"]

    required = ["id_participante", "actividades_completadas", "total_actividades", "pretest", "postest"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error("El CSV no tiene estas columnas obligatorias: " + ", ".join(missing))
        st.stop()

    numeric_cols = [
        "actividades_completadas",
        "total_actividades",
        "pretest",
        "postest",
        "analisis_producto",
        "uso_ia",
        "comparacion_rediseno",
        "presentacion_formato",
        "usabilidad",
        "satisfaccion",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["finalizacion"] = (df["actividades_completadas"] / df["total_actividades"].replace(0, pd.NA)) * 100
    df["mejora_aprendizaje"] = df["postest"] - df["pretest"]
    df["indice_innovacion"] = df[CRITERIOS].mean(axis=1) if set(CRITERIOS).issubset(df.columns) else 0

    if "comentario_abierto" not in df.columns:
        df["comentario_abierto"] = "Sin comentario"

    df["categoria_comentario"] = df["comentario_abierto"].apply(classify_comment)
    return df
