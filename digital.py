from tkinter import*

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)
    
label = Label(root, font = ("DS-Digital", 80),bg = 'black',foreground = 'white')
label.pack(anchor="center")

time()
mainloop() 
