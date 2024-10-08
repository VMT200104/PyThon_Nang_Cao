from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator By VoMinhTan")
        self.root.geometry("570x590+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#17161b")

        self.equation = ""

        self.create_widgets()

    def create_widgets(self):
        # Result screen
        self.screen = Label(self.root, width=25, height=3, text="", font=("arial", 30), bg="#17161b", fg="#fff")
        self.screen.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='nsew')

        # Buttons
        buttons = [
            ('C', 1, 0, self.clear), ('/', 1, 1, lambda: self.show("/")),
            ('%', 1, 2, lambda: self.show("%")), ('*', 1, 3, lambda: self.show("*")),
            ('7', 2, 0, lambda: self.show("7")), ('8', 2, 1, lambda: self.show("8")),
            ('9', 2, 2, lambda: self.show("9")), ('-', 2, 3, lambda: self.show("-")),
            ('4', 3, 0, lambda: self.show("4")), ('5', 3, 1, lambda: self.show("5")),
            ('6', 3, 2, lambda: self.show("6")), ('+', 3, 3, lambda: self.show("+")),
            ('1', 4, 0, lambda: self.show("1")), ('2', 4, 1, lambda: self.show("2")),
            ('3', 4, 2, lambda: self.show("3")),
            ('0', 5, 0, lambda: self.show("0")), ('.', 5, 2, lambda: self.show("."))
        ]

        # Create buttons using grid
        for (text, row, column, command) in buttons:
            width = 5
            height = 2

            if text == '0':
                Button(self.root, text=text, width=5, height=height, font=("arial", 30, "bold"),
                       bd=1, fg="#fff", bg="#2a2d36", command=command).grid(row=row, column=column, columnspan=2, padx=5, pady=5, sticky='nsew')
            else:
                Button(self.root, text=text, width=5, height=height, font=("arial", 30, "bold"),
                       bd=1, fg="#fff", bg="#2a2d36", command=command).grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

        # Create "=" button with colspan
        Button(self.root, text='=', width=5, height=2, font=("arial", 30, "bold"),
               bd=1, fg="#fff", bg="#fe9037", command=self.calculate).grid(row=4, column=3, rowspan=2, padx=3, pady=3, sticky='nsew')

        # Configure row and column weights for resizing
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def show(self, value):
        self.equation += value
        self.screen.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.screen.config(text=self.equation)

    def calculate(self):
        if self.equation:
            try:
                result = str(eval(self.equation))
                self.equation = result
            except Exception:
                self.equation = "error"
        self.screen.config(text=self.equation)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
