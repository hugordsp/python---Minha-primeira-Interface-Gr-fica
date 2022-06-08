import os
os.system('cls')
from tkinter import *


class Aplication():
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_de_tela()
        self.Widgets_frame_1()
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= 'darkgrey')
        self.root.geometry('700x500')  
        self.root.resizable(True, True)  
        self.root.maxsize(width= 900, height=500)
        self.root.minsize(width= 700, height=500)

    def frames_de_tela (self):   
        #Frame superior 
        self.frame_1 = Frame(self.root, bd = 4, bg = 'lightgrey', 
                                        highlightbackground= 'black', highlightthickness=1)
        self.frame_1.place(relx= 0.02, rely=0.025, relwidth=0.96, relheight=0.46)
        #Frame inferior 
        self.frame_2 = Frame(self.root, bd = 4, bg = 'lightgrey', 
                                        highlightbackground= 'black', highlightthickness=1)
        self.frame_2.place(relx= 0.02, rely=0.515, relwidth=0.96, relheight=0.46)

    def Widgets_frame_1 (self):
        #Botões:
        self.bt_limpar = Button(self.frame_1, text= "Limpar")
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=.1, relheight= 0.15)   

        self.bt_buscar = Button(self.frame_1, text= "Buscar")
        self.bt_buscar.place(relx= 0.3, rely=0.1, relwidth=.1, relheight= 0.15)  

        self.bt_novo = Button(self.frame_1, text= "Novo")
        self.bt_novo.place(relx= 0.65, rely=0.1, relwidth=.1, relheight= 0.15) 

        self.bt_alterar = Button(self.frame_1, text= "Alterar")
        self.bt_alterar.place(relx= 0.75, rely=0.1, relwidth=.1, relheight= 0.15)

        self.bt_apagar = Button(self.frame_1, text= "Apagar")
        self.bt_apagar.place(relx= 0.85, rely=0.1, relwidth=.1, relheight= 0.15)

        #Labels do frame_1:
        #1-Código;
        self.lb_codigo = Label(self.frame_1, text= 'Código:')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth= 0.078)
        #2-Nome;
        self.lb_nome = Label(self.frame_1, text= 'Nome:')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth= 0.9)
        #2-Telefone;
        self.lb_telefone = Label(self.frame_1, text= 'Telefone:')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth= 0.4)
        #2-Cidade;
        self.lb_cidade = Label(self.frame_1, text= 'Cidade:')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth= 0.45)
      
        


Aplication()
