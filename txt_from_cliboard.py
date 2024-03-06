import tkinter as tk
from tkinter import filedialog
import pyperclip
import os

# Þetta forrit vistar það sem er á clipboardinu í textaskrá. 

def vista():
    slod = os.path.join(path.get(), f'{titill.get()}.txt')
    with open(slod, "w") as file:
        file.write(pyperclip.paste())
    titill.set("")
    pyperclip.copy("")
    print("Vistað")

root = tk.Tk()
root.title("Seiva clipboard sem txt fæl")
root.geometry("400x200")

titill = tk.StringVar()
nafn_label = tk.Label(root, text="Nafn fæls: ").pack()
entry = tk.Entry(root, textvariable=titill).pack(padx=15, pady=15)
takki = tk.Button(root, text="Vista", command=vista, padx=15, pady=15).pack()

path = tk.StringVar()
path.set(os.getcwd())

frame_nedri = tk.Frame(root, padx=15, pady=15)
path_label = tk.Label(frame_nedri, textvariable=path).grid(row=0, column=0, padx=10, pady=10)
button = tk.Button(frame_nedri, text="Velja path", command=lambda: path.set(filedialog.askdirectory()), padx=5, pady=5).grid(row=0, column=1)   

frame_nedri.pack()



root.mainloop()