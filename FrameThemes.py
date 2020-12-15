from tkinter import *

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.fm = Frame(root, width=300, height=200, bg="blue")
        self.fm.pack(side=TOP, expand=NO, fill=NONE)    
        #self.bgcolor()
    def createWidgets(self):
        self.MyButton = Button(self)
        self.MyButton["text"] = "Change Color"
        self.MyButton["fg"]   = "red"
        self.MyButton["command"] =  self.bgcolor
        self.MyButton.pack({"side": "left"})

    def bgcolor(self):    
        #self.fm.bg="red"
        self.fm = Frame(root, width=300, height=200, bg="red")
        self.fm.pack(side=TOP, expand=NO, fill=NONE)
    
    

root = Tk()
display = App(root)
display.mainloop()
