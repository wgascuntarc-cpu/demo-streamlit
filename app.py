import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Demo remoto", page_icon="📊", layout="wide")

st.title("Demo de Streamlit desde el celular")
st.caption("Publicado automáticamente desde la laptop de casa.")

col1, col2, col3 = st.columns(3)
col1.metric("Proyectos", "3", "+1")
col2.metric("Deploys hoy", "2", "0")
col3.metric("Uptime", "99.9%", "0.1%")

st.subheader("Serie de ejemplo")
datos = pd.DataFrame(
    np.random.default_rng(7).normal(size=(60, 3)).cumsum(axis=0),
    columns=["Ventas", "Costos", "Margen"],
)
st.line_chart(datos)

with st.sidebar:
    st.header("Filtros")
    st.write("Este panel vive en la nube y se actualiza con cada push.")
    st.success("Funcionando ✅")
