import socket
import sys
import time
import tkinter as tk
from tkinter import filedialog
from functools import partial
from cryptography.fernet import Fernet
import os

def gen_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

def call_key():
    return open("pass.key", "rb").read()

x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port= 7878
x.bind(("", port))
gen_key()

h_name= socket.gethostname()
print("server will start on host: ", h_name)
connection = ''
address = ''

def listen():
    global connection, address
    x.listen(1)
    connection,address= x.accept()
    connection.send(call_key())
    #print('accepted')
    msg1["text"]="Receiver Has connected to the server and is now online..."
    msg2["text"]="Enter File Destination to send"
    return

def send_file():
    global connection, address
    file_send = entry.get()
    # display_mess=display_mess.encode()
    # connection.send(display_mess)
    # print(file_send)
    # with open(file_send, "rb") as f:
    #    chunk = f.read(1024)
    #    connection.send(chunk)
    #    connection.recv(1)
    # connection.send(b'')
    # if file_send == 'exit':
    #     connection.send(b'0')
    #     break
    try:
        f = open(file_send , "rb")
    except:
        msg2["text"]="No such file .Enter Correct File Destination to send"
        return
    name = file_send.split('/')[-1]

    key = call_key()
    data_org = f.read()
    f.close()
    fer = Fernet(key)
    data_enc = fer.encrypt(data_org)
    with open("temp" , "wb") as f:
        f.write(data_enc)
    f = open("temp", "rb")

    connection.send(name.encode())
    connection.recv(1)
    while 1:
        chunk = f.read(1024)
        if chunk:
            connection.send(chunk)
            connection.recv(1)
        else:
            connection.send(b'0')
            break
    f.close()

    if os.path.exists("temp"):
        os.remove("temp")

    msg1["text"]=name+" is sent"
    msg2["text"]="Enter File Destination to send"
    return

def open_browse():
    path = filedialog.askopenfilename()
    entry.delete(0,tk.END)
    entry.insert(0,path)
    return

def close_cnt():
   global x
   x.close()
   x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   x.bind(("",port))
   msg1["text"]="server done binding to host and port successfully"
   msg2["text"]="server is waiting for incoming connections"
   return

# port= 7878

# x.bind((h_name, port))
# x.bind(('', port))
# print( "server done binding to host and port successfully")
# print("server is waiting for incoming connections")

# x.listen(9)

# connection,address= x.accept()
# print(address, " Has connected to the server and is now online...")


# connection.shutdown(socket.SHUT_RDWR)
# x.shutdown(socket.SHUT_RDWR)
# connection.shutdown()
# x.shutdown()
# connection.recv(1)
# connection.close()
# x.close()



window=tk.Tk()
window.config(bg="black")
window.title("Send Files")
Heading=tk.Label(text="Send Files",font=("Courier",30),foreground="white", background="black",width=20, height= 1)
Heading.pack()
msg=tk.Label(text="Please connect using receiving application to hostname "+h_name,font=("Courier",10),foreground="yellow", background="black", height= 1)
entry = tk.Entry(fg="yellow", bg="blue", width=50)

browse = tk.Button(
    text="Browse",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=open_browse
)
button = tk.Button(
    text="Start Listening",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=listen
)
button2 = tk.Button(
    text="Send File",
    width=10,
    height=1,
    bg="blue",
    fg="yellow",
    command=send_file
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

msg1=tk.Label(text="server done binding to host and port successfully",font=("Courier",10),foreground="red", background="black", height= 1)
msg2=tk.Label(text="server is waiting for incoming connections",font=("Courier",10),foreground="red", background="black", height= 1)
msg1.pack()
msg2.pack()
entry.pack()
browse.pack()
button.pack()
button2.pack()
# button3.pack()
def on_closing():
    if os.path.exists("pass.key"):
        os.remove("pass.key")
    x.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
