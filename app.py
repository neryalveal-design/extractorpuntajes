import streamlit as st
import pandas as pd
from pdf_exporter import export_to_pdf
from excel_exporter import export_to_excel
from utils import analyze_data, get_course_stats

st.set_page_config(page_title="Consolidador de Ensayos", layout="wide")

st.title("📊 Consolidador de Ensayos por Curso")

# 1. Subir archivos
uploaded_files = st.file_uploader("Sube archivos Excel o CSV", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    data, courses, students = analyze_data(uploaded_files)

    st.tabs(["Resumen", "Por Curso", "Exportar"])

    with st.expander("📌 Resumen"):
        st.metric("Archivos procesados", len(uploaded_files))
        st.metric("Cursos detectados", len(courses))
        st.metric("Estudiantes únicos", students)

        for course in courses:
            stats = get_course_stats(data, course)
            st.write(f"**{course}** - {stats['count']} estudiantes - Promedio: {stats['average']:.1f}")

    with st.expander("📘 Por Curso"):
        for course in courses:
            st.subheader(course)
            stats = get_course_stats(data, course)
            st.write(f"Estudiantes: {stats['count']}")
            st.write(f"Promedio: {stats['average']:.1f}")
            st.write(f"Mínimo: {stats['min']}")
            st.write(f"Máximo: {stats['max']}")

            st.dataframe(data[data['curso'] == course])

    with st.expander("📤 Exportar"):
        custom_names = {}
        ensayos = [col for col in data.columns if col.startswith("ensayo")]

        st.write("Personaliza nombres de columnas:")
        for ensayo in ensayos:
            custom_name = st.text_input(f"Nombre para {ensayo}", value=ensayo)
            custom_names[ensayo] = custom_name

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Descargar Excel"):
                export_to_excel(data, custom_names)
        with col2:
            if st.button("📄 Descargar PDF"):
                export_to_pdf(data, courses, custom_names)

