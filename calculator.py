import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x395")
        self.maxsize(400, 395)
        self.resizable(False, False)
        self.dark_mode = True  # Set to False for light mode
        print("Set name and size")

        # Create a lighter color for the button press effect
        self.lighter_color = "#A0A0A0"  # Change this to your preferred lighter color

        # Set the background color of the buttons initially
        for btn in self.winfo_children():
            if isinstance(btn, tk.Button):
                btn.configure(bg="black" if self.dark_mode else "white", activebackground=self.lighter_color)


        # Bind functions for button press and release events
        self.bind_buttons()

        # Fonts
        self.button_font = ("Arial", 16, "bold")
        self.display_font = ("Arial", 24, "bold")
        print("Set font")

        # Calculator display
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_label = tk.Label(self, textvariable=self.result_var, font=self.display_font, anchor="e", padx=10, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        print("Set up display")

        # Buttons
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("π", 5, 2), ("exp", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("√", 6, 3),
            ("log", 7, 0), ("ln", 7, 1), ("x^2", 7, 2), ("x^y", 7, 3),
            ("DEL", 8, 0), ("AC", 8, 1), ("<-", 8, 2), ("e", 8, 3)
        ]

        for button_text, row, col in self.buttons:
            btn = tk.Button(self, text=button_text, font=self.button_font, command=lambda text=button_text: self.on_button_click(text))
            btn.grid(row=row, column=col, sticky="nsew")
            btn.configure(bg="black", fg="white") if self.dark_mode else btn.configure(bg="white", fg="black")
            self.grid_columnconfigure(col, weight=1)
        print("Set up buttons")

    def bind_buttons(self):
        for btn in self.winfo_children():
            if isinstance(btn, tk.Button):
                btn.bind("<ButtonPress-1>", self.on_button_press)
                btn.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        event.widget.config(relief=tk.SUNKEN)
        print("Button sunken")

    def on_button_release(self, event):
        event.widget.config(relief=tk.RAISED)
        print("Button raised")

    def on_button_click(self, text):
        current_value = self.result_var.get()
        if text == "=":
            try:
                result = self.evaluate_expression(current_value)
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif text == "AC":
            self.result_var.set("0")
        elif text == "DEL":
            if current_value == "0" or current_value == "Error":
                self.result_var.set("0")
            elif len(current_value) == 1:
                self.result_var.set("0")
            else:
                self.result_var.set(current_value[:-1])
        elif text == "<-":
            self.result_var.set(current_value[:-1])
        elif text == "π":
            self.result_var.set(str(math.pi))
        elif text == "exp":
            self.result_var.set(str(math.e))
        elif text in {"sin", "cos", "tan", "log", "ln", "x^2"}:
            result = self.calculate_scientific_function(text)
            self.result_var.set(result)
        elif text == "x^y":
            self.result_var.set(current_value + "**")
        else:
            if current_value == "0" or current_value == "Error":
                self.result_var.set(text)
            elif current_value.startswith("0"):
                self.result_var.set(current_value[1:] + text)
            else:
                self.result_var.set(current_value + text)

    def evaluate_expression(self, expression):
        try:
            return str(eval(expression))
        except Exception:
            return "Error"

    def calculate_scientific_function(self, func_name):
        try:
            value = float(self.result_var.get())
            if func_name == "sin":
                return str(math.sin(value))
            elif func_name == "cos":
                return str(math.cos(value))
            elif func_name == "tan":
                return str(math.tan(value))
            elif func_name == "log":
                return str(math.log10(value))
            elif func_name == "ln":
                return str(math.log(value))
            elif func_name == "x^2":
                return str(value**2)
        except Exception:
            return "Error"
        
calc = '''

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
     '''

print(calc)

thank = '''

████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ████████╗██╗░░██╗██╗░██████╗
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ╚══██╔══╝██║░░██║██║██╔════╝
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ░░░██║░░░███████║██║╚█████╗░
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ░░░██║░░░██╔══██║██║░╚═══██╗
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░░░██║░░░██║░░██║██║██████╔╝
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
     '''

print(thank)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
