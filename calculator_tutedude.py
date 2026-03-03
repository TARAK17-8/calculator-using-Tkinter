import tkinter as tk

def add():
    try:
        r.set(float(a.get()) + float(b.get()))
    except:
        r.set("Error")

def sub():
    try:
        r.set(float(a.get()) - float(b.get()))
    except:
        r.set("Error")

def mul():
    try:
        r.set(float(a.get()) * float(b.get()))
    except:
        r.set("Error")

def div():
    try:
        r.set(float(a.get()) / float(b.get()))
    except:
        r.set("Error")

root = tk.Tk()
root.title("Calculator")

a = tk.StringVar()
b = tk.StringVar()
r = tk.StringVar()

tk.Label(root, text="First Number").grid(row=0, column=0)
tk.Entry(root, textvariable=a).grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
tk.Entry(root, textvariable=b).grid(row=1, column=1)

tk.Button(root, text="+", command=add).grid(row=2, column=0)
tk.Button(root, text="-", command=sub).grid(row=2, column=1)
tk.Button(root, text="*", command=mul).grid(row=3, column=0)
tk.Button(root, text="/", command=div).grid(row=3, column=1)

tk.Label(root, text="Result").grid(row=4, column=0)
tk.Entry(root, textvariable=r).grid(row=4, column=1)

root.mainloop()