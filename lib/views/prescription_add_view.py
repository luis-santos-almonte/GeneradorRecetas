from tkinter import Tk, Label, Button, Entry, messagebox, Toplevel
from lib.classes.prescription import prescription

class prescription_add_view: 
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        
        self.view = Toplevel(self.root)
        self.view("Agregar a receta")
        self.view("400x200")
        self.view.resizable(False, False)
        
        Label(self.view, text="Descripcion:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_description = Entry(self.view)
        self.entry_description.grid(row=0, column=1, padx=10, pady=10)

        Label(self.view, text="Uso:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_usage = Entry(self.view)
        self.entry_usage.grid(row=1, column=1, padx=10, pady=10)

        Label(self.view, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_quantity = Entry(self.view)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=10)

        # Botón para guardar el producto
        self.boton_guardar = Button(self.view, text="Guardar", command=self.validate_entries)
        self.boton_guardar.grid(row=3, column=0, columnspan=2, pady=10)
        
    def validate_entries(self):
        if not self.entry_description.get() or not self.entry_usage.get() or not self.entry_quantity.get():
            messagebox.showwarning("Error", "Todos los campos son obligatorios")