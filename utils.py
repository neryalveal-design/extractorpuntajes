import pandas as pd
import streamlit as st

def analyze_data(files):
    all_data = []

    for file in files:
        # Leer desde la fila correcta donde están los encabezados
        df = pd.read_excel(file, header=8)

        # Insertar columna "curso" extrayéndolo desde fila 3 (índice 2)
        metadata = pd.read_excel(file, header=None, nrows=5, usecols="C")  # Columna 'C' contiene "CURSO"
        curso_value = metadata.iloc[2, 0] if not pd.isna(metadata.iloc[2, 0]) else "Curso desconocido"
        df["curso"] = curso_value

        # Normalizar nombre de columnas
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Renombrar columna si existe 'nombre_estudiante' u otra similar
        if "nombre_estudiante" not in df.columns:
            posible_col = [col for col in df.columns if "estudiante" in col]
            if posible_col:
                df.rename(columns={posible_col[0]: "nombre_estudiante"}, inplace=True)

        all_data.append(df)

    # Combinar todos los archivos
    full_df = pd.concat(all_data, ignore_index=True)

    cursos = full_df["curso"].unique()
    estudiantes = full_df["nomb]()_
