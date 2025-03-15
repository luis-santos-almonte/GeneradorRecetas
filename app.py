from tkinter import Button, Label
from lib.classes import patient, prescription

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello, World!")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.label = Label(self.root, text="Hello, World!")
        self.label.pack()
        self.button = Button(self.root, text="Click Me", command=self.on_click)
        self.button.pack()

    def on_click(self):
        self.label["text"] = "Button Clicked"
