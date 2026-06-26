# Panel de Analítica IA

Dashboard en Streamlit para el Módulo 6 del curso Moodle **Diseño y creatividad con Inteligencia Artificial para productos artesanales**.

## Funcionalidades

- Carga de archivo CSV.
- Indicadores de participación, aprendizaje, innovación, usabilidad y satisfacción.
- Gráficos interactivos con Plotly.
- Clasificación de comentarios abiertos.
- Reporte ejecutivo descargable.

## Ejecutar localmente

```powershell
pip install -r requirements.txt
python -m streamlit run app.py
```

Si no se sube un CSV, el panel usa `datos_ejemplo.csv`.

## Estructura esperada del CSV

El archivo debe incluir columnas como:

- `id_participante`
- `rubro_artesanal`
- `actividades_completadas`
- `total_actividades`
- `pretest`
- `postest`
- `analisis_producto`
- `uso_ia`
- `comparacion_rediseno`
- `presentacion_formato`
- `usabilidad`
- `satisfaccion`
- `comentario_abierto`

