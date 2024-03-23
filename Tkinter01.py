'''import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My First GUI")


label = tk.label(root, text = "Hello World!", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

root.mainloop()'''

import tkinter
import customtkinter
from pytube import YouTube

#system setting
customtkinter.set_appearance_mode("System")
customtkinter. set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("")

