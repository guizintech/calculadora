import customtkinter as ctk
from math import sqrt, sin, cos, tan, log10
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("420x760")
app.title("Calculadora V2")
app.resizable(False, False)

BG = "#070707"
CARD = "#111111"
BTN = "#1C1C1C"
HOVER = "#2B2B2B"

BLUE = "#00E5FF"
PURPLE = "#8B5CF6"
PINK = "#FF007A"
GREEN = "#00FFB3"
WHITE = "#FFFFFF"
GRAY = "#8E8E93"

app.configure(fg_color=BG)

expression = ""

header = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

header.pack(fill="x", pady=(15, 0), padx=20)

title = ctk.CTkLabel(
    header,
    text="CALC V2",
    font=("Segoe UI", 30, "bold"),
    text_color=BLUE
)

title.pack(side="left")

clock = ctk.CTkLabel(
    header,
    text="",
    font=("Segoe UI", 15),
    text_color=GRAY
)

clock.pack(side="right")

def update_clock():
    clock.configure(text=datetime.now().strftime("%H:%M:%S"))
    app.after(1000, update_clock)

update_clock()

container = ctk.CTkFrame(
    app,
    width=380,
    height=660,
    corner_radius=35,
    fg_color=CARD,
    border_width=1,
    border_color="#222222"
)

container.pack(pady=15)
container.pack_propagate(False)

history = ctk.CTkLabel(
    container,
    text="",
    anchor="e",
    justify="right",
    font=("Segoe UI", 14),
    text_color=GRAY
)

history.pack(fill="x", padx=25, pady=(25, 0))

display = ctk.CTkEntry(
    container,
    height=90,
    corner_radius=25,
    border_width=0,
    fg_color="#0D0D0D",
    text_color=WHITE,
    font=("Segoe UI", 42, "bold"),
    justify="right"
)

display.pack(fill="x", padx=20, pady=(10, 25))

buttons_frame = ctk.CTkFrame(
    container,
    fg_color="transparent"
)

buttons_frame.pack(pady=5)

def refresh():
    display.delete(0, "end")
    display.insert(0, expression)

def add(value):
    global expression
    expression += str(value)
    refresh()

def clear():
    global expression
    expression = ""
    refresh()

def backspace():
    global expression
    expression = expression[:-1]
    refresh()

def calculate():
    global expression

    try:
        result = str(eval(expression))
        history.configure(text=f"{expression} =")
        expression = result
        refresh()

    except:
        display.delete(0, "end")
        display.insert(0, "Erro")
        expression = ""

def apply_function(func):
    global expression

    try:
        value = float(expression)

        if func == "sqrt":
            result = sqrt(value)

        elif func == "sin":
            result = sin(value)

        elif func == "cos":
            result = cos(value)

        elif func == "tan":
            result = tan(value)

        elif func == "log":
            result = log10(value)

        expression = str(round(result, 8))
        refresh()

    except:
        display.delete(0, "end")
        display.insert(0, "Erro")
        expression = ""

def create_button(text, row, col, command,
                  color=BTN,
                  hover=HOVER,
                  width=78,
                  height=68,
                  text_color=WHITE):

    button = ctk.CTkButton(
        buttons_frame,
        text=text,
        command=command,
        width=width,
        height=height,
        corner_radius=22,
        fg_color=color,
        hover_color=hover,
        text_color=text_color,
        font=("Segoe UI", 24, "bold"),
        border_width=1,
        border_color="#2A2A2A"
    )

    button.grid(
        row=row,
        column=col,
        padx=7,
        pady=7
    )

buttons = [

    ("C", 0, 0, clear, PINK),
    ("⌫", 0, 1, backspace, "#333333"),
    ("√", 0, 2, lambda: apply_function("sqrt"), PURPLE),
    ("÷", 0, 3, lambda: add("/"), BLUE),

    ("7", 1, 0, lambda: add("7")),
    ("8", 1, 1, lambda: add("8")),
    ("9", 1, 2, lambda: add("9")),
    ("×", 1, 3, lambda: add("*"), BLUE),

    ("4", 2, 0, lambda: add("4")),
    ("5", 2, 1, lambda: add("5")),
    ("6", 2, 2, lambda: add("6")),
    ("-", 2, 3, lambda: add("-"), BLUE),

    ("1", 3, 0, lambda: add("1")),
    ("2", 3, 1, lambda: add("2")),
    ("3", 3, 2, lambda: add("3")),
    ("+", 3, 3, lambda: add("+"), BLUE),

    ("sin", 4, 0, lambda: apply_function("sin"), PURPLE),
    ("cos", 4, 1, lambda: apply_function("cos"), PURPLE),
    ("tan", 4, 2, lambda: apply_function("tan"), PURPLE),
    ("log", 4, 3, lambda: apply_function("log"), PURPLE),

]

for item in buttons:

    if len(item) == 5:
        text, row, col, command, color = item
    else:
        text, row, col, command = item
        color = BTN

    create_button(
        text,
        row,
        col,
        command,
        color=color
    )

zero_button = ctk.CTkButton(
    buttons_frame,
    text="0",
    command=lambda: add("0"),
    width=170,
    height=68,
    corner_radius=22,
    fg_color=BTN,
    hover_color=HOVER,
    text_color=WHITE,
    font=("Segoe UI", 24, "bold"),
    border_width=1,
    border_color="#2A2A2A"
)

zero_button.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=7,
    pady=7,
    sticky="w"
)

dot_button = ctk.CTkButton(
    buttons_frame,
    text=".",
    command=lambda: add("."),
    width=78,
    height=68,
    corner_radius=22,
    fg_color=BTN,
    hover_color=HOVER,
    text_color=WHITE,
    font=("Segoe UI", 24, "bold"),
    border_width=1,
    border_color="#2A2A2A"
)

dot_button.grid(
    row=5,
    column=2,
    padx=7,
    pady=7
)

equal_button = ctk.CTkButton(
    buttons_frame,
    text="=",
    command=calculate,
    width=78,
    height=68,
    corner_radius=22,
    fg_color=GREEN,
    hover_color="#00CC92",
    text_color="black",
    font=("Segoe UI", 28, "bold")
)

equal_button.grid(
    row=5,
    column=3,
    padx=7,
    pady=7
)

def keyboard(event):

    key = event.keysym

    if key in "0123456789":
        add(key)

    elif key == "plus":
        add("+")

    elif key == "minus":
        add("-")

    elif key == "slash":
        add("/")

    elif key == "asterisk":
        add("*")

    elif key == "period":
        add(".")

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()

app.bind("<Key>", keyboard)

footer = ctk.CTkLabel(
    app,
    text="Modern Futuristic Calculator",
    font=("Segoe UI", 12),
    text_color=GRAY
)

footer.pack(pady=(0, 10))

app.mainloop()
