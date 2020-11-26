# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:45:02 2020

@author: Anubhav Sharma
"""

import sys 
import os
import tkinter as tk

def send():
    os.system('python3 gui.py')
    

def rece():
    os.system('python3 client.py')
window=tk.Tk()
window.config(bg="black")
window.title("Pair Share")
Heading=tk.Label(text="Pair Share",font=("Courier",30),foreground="white", background="black",width=20, height= 1)
Heading.pack()
img=tk.PhotoImage("icon.png")

#msg0=tk.Label(text="ghgh",font=("Courier",10),image=img,foreground="yellow", background="black", height= 1)
msg=tk.Label(text="Please choose the action you want to perform",font=("Courier",10),foreground="yellow", background="black", height= 1)
button1 = tk.Button(
    text="Send Files",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=send
)

button2 = tk.Button(
    text="Receieve Files",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=rece
)
#msg0.pack()
msg.pack()
#msg1=tk.Label(text="server done binding to host and port successfully",font=("Courier",10),foreground="red", background="black", height= 1)
#msg2=tk.Label(text="server is waiting for incoming connections",font=("Courier",10),foreground="red", background="black", height= 1)
#msg1.pack()
#msg2.pack()
button1.pack()
button2.pack()
#button2.pack()
window.mainloop()
    