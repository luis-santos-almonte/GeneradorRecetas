from tkinter import Button, Label, Entry, Text
from lib.classes.patient import Patient
from lib.classes.prescription import Prescription
from lib.functions.generate_pdf import generate_pdf
from lib.reports.base_prescription import get_base_prescription
from lib.views.prescription_add_view import PrescriptionAddView
from datetime import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello, World!")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        self.pres = Prescription()
        
        Label(self.root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = Entry(self.root, width=50)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        Label(self.root, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_lastname = Entry(self.root, width=50)
        self.entry_lastname.grid(row=1, column=1, padx=10, pady=10)
        
        Label(self.root, text="Edad:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_age = Entry(self.root, width=50)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)
        
        self.boton_agregar = Button(self.root, text="Agregar", command=self.open_prescription_add)
        self.boton_agregar.grid(row=4, column=1, columnspan=2, pady=10)
        
        self.boton_agregar = Button(self.root, text="Imprimir", command=self.print_prescription)
        self.boton_agregar.grid(row=4, column=2, columnspan=2, pady=10)
        
        self.text_prescription = Text(self.root, height=15, width=50, state="disabled")
        self.text_prescription.grid(row=6, column=1, pady=10)
        
    def open_prescription_add(self):
        view = PrescriptionAddView(self.root, self.add_prescription)
        
    def add_prescription(self, prescription):
        self.pres.add_treatment(prescription)
        
        self.update_prescription_list()
    
    def update_prescription_list(self):
        self.text_prescription.config(state="normal")
        self.text_prescription.delete("1.0", "end")
        self.text_prescription.insert("end", str(self.pres))
        self.text_prescription.config(state="disabled")
        
    def print_prescription(self):
        pat = Patient(self.entry_name.get(), self.entry_lastname.get(), int(self.entry_age.get()))
        report = get_base_prescription(pat, self.pres)
        set_date = f"{datetime.date(datetime.now())}"
        report_name = f"{pat.name} {pat.lastname}-{set_date}.pdf"
        
        generate_pdf(report, report_name)
