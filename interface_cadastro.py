import os
os.system('cls')
from tkinter import *


class Aplication():
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_de_tela()
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= 'darkgrey')
        self.root.geometry('700x500')  
        self.root.resizable(True, True)  
        self.root.maxsize(width= 900, height=500)
        self.root.minsize(width= 400, height=300)

    def frames_de_tela (self):   
        #Frame superior 
        self.frame_1 = Frame(self.root, bd = 4, bg = 'lightgrey', 
                                        highlightbackground= 'black', highlightthickness=1)
        self.frame_1.place(relx= 0.02, rely=0.025, relwidth=0.96, relheight=0.46)
        #Frame inferior 
        self.frame_2 = Frame(self.root, bd = 4, bg = 'lightgrey', 
                                        highlightbackground= 'black', highlightthickness=1)
        self.frame_2.place(relx= 0.02, rely=0.515, relwidth=0.96, relheight=0.46)

Aplication()
