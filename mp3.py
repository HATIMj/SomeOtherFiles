import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
m=[]
r=Tk()
r.geometry("500x500")
r.title("MP3 Player")
def play():
    for i in m:
        os.system(f"cvlc {i}")
def browse():

    c=filedialog.askopenfilename()
    for i in range(1):
        m.append(c)
        

    
x=Button(r,text="Browse",command=browse).pack(pady=20)
y=Button(r,text="Play",command=play)
y.pack(pady=20)


















r.mainloop()