from tkinter import messagebox, Text
from playwright.sync_api import sync_playwright

def generate_pdf(html_content: str, pdf_name: str, file_size: str = "A4") -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(path=pdf_name, format=file_size)
        browser.close()
        print("PDF generado: {pdf_name}") 
