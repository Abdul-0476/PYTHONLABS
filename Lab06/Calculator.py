import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg="lightblue")

        self.entry = tk.Entry(master, width=20, font=("Arial", 18), borderwidth=2, relief="sunken", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.entry.insert(0, "0")

        self.create_buttons()

        self.entry.bind("<KeyRelease>", self.key_input_handler)

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.button_click(x)
            tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, padx=2, pady=2)

        # Equal button
        tk.Button(self.master, text='=', width=5, height=2, font=("Arial", 14), command=self.calculate).grid(row=0, column=4, padx=2, pady=2)

    def button_click(self, char):
        current = self.entry.get()
        if current == "0" or current == "Error":
            current = ""

        if char == 'C':
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "0")
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + char)

    def key_input_handler(self, event):
        if event.keysym == 'Return':
            self.calculate()

    def calculate(self):
        expression = self.entry.get().replace('x', '*').replace('÷', '/')
        try:
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
