from services.excel_service import save_excel


def export_dataframe(df, path):
    save_excel(df, path)
