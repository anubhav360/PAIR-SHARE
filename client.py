import socket
import sys
import time
import tkinter as tk
from tkinter import filedialog
from malsc import *
import os
from cryptography.fernet import Fernet
x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def call_key():
   return open("passc.key", "rb").read()

def cnt():
    port = 7878
    h_name=entry.get()
    x.connect((h_name,port))
    key_data = x.recv(1024)
    with open("passc.key", "wb") as kk:
       kk.write(key_data)
    msg["text"]="Connected to sender"
    return
   #  while 1: 
       # incoming_message=x.recv(1024)
       # incoming_messagge=incoming_message.decode()
    
       # with open("sample_rec.jpg","wb") as f:
       #    chunk = x.recv(1024)
          
       #    f.write(chunk)
       #    x.send(b"true")
       
    
      #  file_rec = x.recv(1024)
      #  if file_rec==b'0':
      #     break
      #  file_rec = file_rec.decode()
      #  print(file_rec)
      #  x.send(b'1')
      #  f = open(file_rec,"wb")
      #  while 1:
      #     chunk = x.recv(1024)
      #     if chunk!=b'0':
      #        f.write(chunk)
      #        x.send(b'1')
      #     else:
      #        break
      #  f.close()
      #  msg["text"]=(file_rec + " Recieved")
       # message= input(str(">>"))
       # message =message.encode()
       # x.send(message)
       # print(" message has been sent...")
   #  msg["text"]=("Connection Closed")   
    
    
    # x.shutdown(socket.SHUT_RDWR)
    # x.shutdown()
    # x.send(b'1')
   #  x.close()
    
def rec_file():

   directory = filedialog.askdirectory()

   file_rec = x.recv(1024)
   if file_rec==b'0':
      return
   file_rec = file_rec.decode()
   print(file_rec)
   x.send(b'1')
   f = open(directory + '/' + file_rec,"wb")
   while 1:
      chunk = x.recv(1024)
      if chunk!=b'0':
         f.write(chunk)
         x.send(b'1')
      else:
         break
   f.close()

   key = call_key()
   fer = Fernet(key)
   f = open(directory + '/' + file_rec, "rb")
   data_enc = f.read()
   f.close()
   data_org = fer.decrypt(data_enc)
   f = open(directory + '/' + file_rec, "wb")
   f.write(data_org)
   f.close()

   # msg["text"]=(file_rec + " Recieved")
   res = mals(directory + '/' + file_rec)
   if(res==2):
      msg["text"] = ("Server Overloaded : Cannot check " + file_rec)
   elif(res==1):
      if os.path.exists(directory + '/' + file_rec):
         os.remove(directory + '/' + file_rec)
      msg["text"] = (file_rec + " was found Malicious and deleted")
   elif(res==0):
      msg["text"] = (file_rec + " is recieved and Safe to use")
   return

def close_cnt():
   global x
   msg["text"]=("Connection Closed")
   x.close()
   x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   if os.path.exists("passc.key"):
      os.remove("passc.key")
   return

window=tk.Tk()
window.config(bg="black")
window.title("Receieve Files")
Heading=tk.Label(text="Receieve Files",font=("Courier",30),foreground="white", background="black",width=20, height= 1)
Heading.pack()
msg=tk.Label(text="Please enter the hostname to connect",font=("Courier",10),foreground="yellow", background="black", height= 1)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
button = tk.Button(
    text="Connect",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=cnt
)
button2 = tk.Button(
    text="Recieve File",
    width=15,
    height=1,
    bg="blue",
    fg="yellow",
    command=rec_file
)
button3 = tk.Button(
    text="Close Connection",
    width=15,
    height=1,
    bg="blue",
    fg="yellow",
    command=close_cnt
)

msg.pack()
#msg1=tk.Label(text="server done binding to host and port successfully",font=("Courier",10),foreground="red", background="black", height= 1)
#msg2=tk.Label(text="server is waiting for incoming connections",font=("Courier",10),foreground="red", background="black", height= 1)
#msg1.pack()
#msg2.pack()
entry.pack()
button.pack()
button2.pack()
button3.pack()
def on_closing():
    if os.path.exists("passc.key"):
        os.remove("passc.key")
    x.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
    