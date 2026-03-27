import tkinter as tk
import random
from PIL import ImageTk, Image
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from time import time, sleep

root = tk.Tk()           
x = 1
stage = tk.Canvas(root, width=800, height=800)
stage.pack()
root.geometry("120x120+1300+450")

root.update()
def img1():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice1.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice1.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def img2():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice2.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice2.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def img3():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice3.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice3.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def img4():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice4.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice4.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def img5():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice5.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice5.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def img6():
    imgtk = ImageTk.PhotoImage(file='individual_projects/Character Manager/img/Dice6.png')
    image = tk.PhotoImage(file="individual_projects/Character Manager/img/Dice6.png")
    stage.create_image((stage.winfo_width()/2, stage.winfo_height()/2), image=imgtk, anchor='center')
    stage.image = imgtk

def call(img, x):
    img
    start = time()
    root.after(30*x, root.destroy)
    mainloop()
    end = time()

for i in range(10):
    if i == 10:
        roll = random.randint(1, 6)
        if roll == 1:
            call(img1(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
        elif roll == 2:
            call(img2(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
        elif roll == 3:
            call(img3(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
        elif roll == 4:
            call(img4(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
        elif roll == 5:
            call(img5(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
        else:
            call(img6(), 10000)
            root = tk.Tk()           
            stage = tk.Canvas(root, width=1000, height=700)
            stage.pack()
            root.geometry("120x120+1300+450")
            root.update()
    else:


call(img1(), x)
root = tk.Tk()           
stage = tk.Canvas(root, width=1000, height=700)
stage.pack()
root.geometry("120x120+1300+450")
root.update()
x *= 2
call(img2(), x)
root = tk.Tk()           
stage = tk.Canvas(root, width=1000, height=700)
stage.pack()
root.geometry("120x120+1300+450")
root.update()
x *= 2
call(img3(), x)
root = tk.Tk()           
stage = tk.Canvas(root, width=1000, height=700)
stage.pack()
root.geometry("120x120+1300+450")
root.update()
x *= 2
call(img4(), x)
root = tk.Tk()           
stage = tk.Canvas(root, width=1000, height=700)
stage.pack()
root.geometry("120x120+1300+450")
root.update()
x *= 2
call(img5(), x)
root = tk.Tk()           
stage = tk.Canvas(root, width=1000, height=700)
stage.pack()
root.geometry("120x120+1300+450")
root.update()
x *= 2
call(img6(), x)