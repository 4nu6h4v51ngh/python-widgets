from tkinter import *
import time
import sys 

root=Tk()

def getTime():
    time_str = time.strftime("%I:%M:%S:%p")
    clock.config(text=time_str)
    clock.after(200,getTime)

clock = Label(root,font=("time",90,"bold"),bg="sky blue")
clock.pack()
getTime()

root.title('Clock by Arsenic')
root.mainloop()
