import pandas as pd

def analyze_data(files):
    all_data = []
    for file in files:
        df = pd.read_excel(file) if file.name.endswith("xlsx") else pd.read_csv(file)
        all_data.append(df)

    full_df = pd.concat(all_data, ignore_index=True)
    cursos = full_df['curso'].unique()
    estudiantes = full_df['nombreEstudiante'].nunique()
    return full_df, cursos, estudiantes

def get_course_stats(df, course):
    data = df[df['curso'] == course]
    puntajes = data.filter(like="ensayo").values.flatten()
    puntajes = [p for p in puntajes if pd.notnull(p)]

    if len(puntajes) == 0:
        return {"average": 0, "min": 0, "max": 0, "count": 0}

    return {
        "average": sum(puntajes)/len(puntajes),
        "min": min(puntajes),
        "max": max(puntajes),
        "count": len(data)
    }

