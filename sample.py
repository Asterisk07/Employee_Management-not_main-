# ayushmaan added this line

# import tkinter as tk



from tkinter import *
from functools import partial
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
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
e2=Entry(frame,textvariable=password).grid(row=1,column=1)
b=Button(root,text="Login",command=root.destroy)
b.pack()
root.mainloop()

