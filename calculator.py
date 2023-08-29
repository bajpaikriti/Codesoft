#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
root=Tk()
root.title("Calculator")
def add():
    num_value1=entry1.get()
    num_value2=entry2.get()
    
    entry3.insert(0,int(num_value1)+int(num_value2))
def subtract():
    num_value1=entry1.get()
    num_value2=entry2.get()
    entry3.insert(0,int(num_value1)-int(num_value2))
    
    
label1= Label(root,text="Enter the first number:")
label1.grid(row=0,column=0)
label2= Label(root,text="Enter the second number:")
label2.grid(row=1,column=0)
entry1=Entry(root,text="")
entry1.grid(row=0,column=1)
entry2=Entry(root,text="")
entry2.grid(row=1,column=1)
button1=Button(root,text="Add",command=add)
button1.grid(row=2,column=0)
button2=Button(root,text="Subtract",command=subtract)
button2.grid(row=2,column=1)
label3= Label(root,text="Result:")
label3.grid(row=3,column=0)
entry3=Entry(root,text="")
entry3.grid(row=3,column=1)
root.mainloop()

