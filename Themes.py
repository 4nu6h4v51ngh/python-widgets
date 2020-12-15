import tkinter as tk
import tkinter.ttk as ttk


class Win(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.mainf = tk.Frame(master, height=200, width=200, pady=50, padx=50)
        self.mainf.grid(row=0, column=0)

        self.colour_btns()
      
        self.colors = ['white', 'black']  # Can initialize more colors

    def colour_btns(self):
        self.white = ttk.Button(self.mainf, text="Normal",command=lambda: self.change_background(self.colors[0]))
        self.black = ttk.Button(self.mainf, text="Dark",command=lambda: self.change_background(self.colors[1]))
        
        #add more colors at sel.colors and call with their names with their corrosponding index 
        
        self.white.grid(row=0, column=0)
        self.black.grid(row=1, column=0)
        
        
    def change_background(self, color):
        self.mainf.configure(background='{}'.format(color))

root = tk.Tk()
root.title('Background')
root.update()
app = Win(root)

root.mainloop()
