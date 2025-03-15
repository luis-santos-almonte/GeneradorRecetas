from tkinter import Button, Label, Entry, messagebox
from lib.classes import patient, prescription

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello, World!")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        Label(self.root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        Label(self.root, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_lastname = Entry(self.root)
        self.entry_lastname.grid(row=1, column=1, padx=10, pady=10)
        
        Label(self.root, text="Edad:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_age = Entry(self.root)
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)
        
        self.boton_agregar = Button(self.root, text="Agregar")
        self.boton_agregar.grid(row=4, column=1, columnspan=2, pady=10)
        
        self.boton_agregar = Button(self.root, text="Imprimir")
        self.boton_agregar.grid(row=4, column=2, columnspan=2, pady=10)
