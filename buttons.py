from tkinter import *

root=Tk()
root.geometry('500x500')


root.title("buttons")
f=Frame(root,bg='black')



buttons=[i for i in range(1,10)]

for i in range(len(buttons)):

    
        b=Button(f,text=buttons[i],width=8,height=2)
        b.pack()
    

f.pack()
root.mainloop()