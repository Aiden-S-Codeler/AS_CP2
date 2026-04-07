import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.configure(background="#f3cc1d")
eek = tk.Label(root, text="The GUI is so Gooey!", font=("Times New Roman", 30, "bold"))
eek.config(fg="#ff0000", background="#f3cc1d")
eek.grid(row=0, column=0)

dog = tk.Label(root, text="Labelmakers are so usefull!")
dog.grid(row=10, column=0)

root.minsize(250,250)
root.maxsize(1500,1500)
root.geometry("600x600+100+100")

root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

btn1 = tk.Button(root, text='ADD', command=add)
btn1.grid(row=4, column=0)

btn2 = tk.Button(root, text='SUB', command=sub)
btn2.grid(row=4, column=1)

lbl = tk.Label(root, text="0")
lbl.grid(row=5, column=0, columnspan=2)

close = tk.Button(root, text="LEAVE", command=root.destroy)
close.grid(row=7, column=3)

root.mainloop()

