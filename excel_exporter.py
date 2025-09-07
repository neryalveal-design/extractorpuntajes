def export_to_excel(df, custom_names):
    renamed_df = df.rename(columns=custom_names)
    renamed_df.to_excel("consolidado.xlsx", index=False)

