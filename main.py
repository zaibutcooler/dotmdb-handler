import tkinter as tk
from tkinter import ttk, filedialog
from ttkbootstrap import Style

def choose_file():
    file_path = filedialog.askopenfilename()
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Error")

root = tk.Tk()
root.title("Calculator")

style = Style(theme='superhero')

frame = ttk.Frame(root, padding=10)
frame.pack()

label_choose_file = ttk.Label(frame, text="Choose a file:")
label_choose_file.grid(row=0, column=0, padx=5, pady=5)

entry_file_path = ttk.Entry(frame)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

btn_browse = ttk.Button(frame, text="Browse", command=choose_file)
btn_browse.grid(row=0, column=2, padx=5, pady=5)

label_num1 = ttk.Label(frame, text="Number 1:")
label_num1.grid(row=1, column=0, padx=5, pady=5)

entry_num1 = ttk.Entry(frame)
entry_num1.grid(row=1, column=1, padx=5, pady=5)

label_plus = ttk.Label(frame, text="+")
label_plus.grid(row=1, column=2, padx=5, pady=5)

entry_num2 = ttk.Entry(frame)
entry_num2.grid(row=1, column=3, padx=5, pady=5)

btn_calculate = ttk.Button(frame, text="Calculate", command=calculate)
btn_calculate.grid(row=1, column=4, padx=5, pady=5)

result = tk.StringVar()
label_result = ttk.Label(frame, textvariable=result)
label_result.grid(row=2, columnspan=5, padx=5, pady=5)

root.mainloop()
