#Import necessary libraries
from tkinter import *
from tkinter import messagebox
#Setup Tkinter Window
root=Tk()
root.geometry("200x200")
#Function for Displaying Warning Message
#This will be called once the button is cicked
#messagebox.showwarning("Window Name","Text to be displayed")
def msg():
        messagebox.showwarning("Alert","Stop! Virus found.")
#Adding Button Widget to Window
button=Button(root,text="Scan for Virus",command=msg)
button.place(x=40,y=80)
#Enterimg main event loop
root.mainloop()