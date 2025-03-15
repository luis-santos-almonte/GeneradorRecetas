from tkinter import messagebox, Text
import pdfkit

options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'encoding': 'UTF-8',
    'no-outline': None
}

def generate_pdf(html_content: str, pdf_name: str):
    try:
        pdfkit.from_string(html_content, pdf_name, options=options)
        print("PDF generado: {pdf_name}") 
            
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el PDF: {e}")