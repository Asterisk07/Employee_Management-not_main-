# import tkinter as tk
from tkinter import *
#from functools import partial
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
def my_window():
    top=Toplevel()
    #top.deiconify()
    frame=Frame(top)
    frame.pack()
    add=Button(frame,text="ADD",command=self_add)
    add.grid(row=0,column=0)
    update=Button(frame,text="UPDATE")
    update.grid(row=1,column=0)
    view_all=Button(frame,text="VIEW ALL")
    view_all.grid(row=2,column=0)
    view_self=Button(frame,text="VIEW SELF")
    view_self.grid(row=3,column=0)
    
    

root=Tk()
root.geometry('400x150')  
frame=Frame(root)
frame.pack()

d=Label(frame,text="Username").grid(row=0,column=0)
#d.grid(row=0,column=0)
username = StringVar()
password=StringVar()
e=Label(frame,text="Password:")
e.grid(row=1,column=0)
e1=Entry(frame,textvariable=username).grid(row=0,column=1)
e2=Entry(frame,textvariable=password,show="*").grid(row=1,column=1)
b=Button(root,text="Login",command=my_window)

b.pack()
root.mainloop()
