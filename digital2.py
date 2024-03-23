from time import strftime, localtime
import tkinter as tk

def update_label():
    current_time = strftime("%Y-%m-%d %I:%M:%S %p", localtime())
    label.config(text=current_time)
    label.after(1000, update_label)

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=('ariel', 50, 'bold'), background='blue', foreground='black')
label.pack(anchor='se')
update_label()
root.mainloop()