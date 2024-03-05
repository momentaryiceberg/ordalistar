import tkinter as tk
import pyperclip

# Þetta forrit vistar það sem er á clipboardinu í textaskrá. 

def vista():
    with open(f'{titill.get()}.txt', "w") as file:
        file.write(pyperclip.paste())
    titill.set("")
    pyperclip.copy("")
    print("Vistað")

root = tk.Tk()

titill = tk.StringVar()
entry = tk.Entry(root, textvariable=titill).pack(padx=15, pady=15)
takki = tk.Button(root, text="Vista", command=vista, padx=15, pady=15).pack()

root.mainloop()