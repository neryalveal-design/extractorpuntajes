from fpdf import FPDF

def export_to_pdf(df, courses, custom_names):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Análisis de Cursos", ln=True, align="C")
    
    for course in courses:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, f"Curso: {course}", ln=True)
        pdf.set_font("Arial", size=10)
        sub_df = df[df['curso'] == course]
        avg = sub_df.filter(like="ensayo").mean(axis=1).mean()
        pdf.cell(200, 10, f"Promedio general: {avg:.2f}", ln=True)
        pdf.ln()

    pdf.output("analisis.pdf")

