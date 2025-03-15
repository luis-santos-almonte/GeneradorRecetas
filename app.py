from tkinter import Button, Label, Tk
from lib.classes import patient, prescription

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("My App")
        self.geometry("300x200")
        self.resizable(False, False)
        self.label = Label(self, text="Hello, World!")
        self.label.pack()
        self.button = Button(self, text="Click Me", command=self.on_click)
        self.button.pack()

    def on_click(self):
        self.label["text"] = "Button Clicked"
