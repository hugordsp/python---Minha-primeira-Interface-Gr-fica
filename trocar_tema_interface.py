import os
from webbrowser import BackgroundBrowser
os.system('cls')
from tkinter import * #módulo para interface gráfica
from tkinter import ttk #Para importar função de lista para o tkinter


class Aplication():
    def __init__(self):
        self.root = Tk()
        self.style = ttk.Style()
        self.tela()
        self.frames_de_tela()
        self.Widgets_frame_1()
        self.Widgets_frame_2()
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#155569')
        self.root.geometry('700x500')  
        self.root.resizable(True, True)  
        self.root.maxsize(width= 900, height=640)
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
        self.bt_limpar = ttk.Button(self.frame_1, text= "Limpar")
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)   

        self.bt_buscar = Button(self.frame_1, text= "Buscar", font=('verdana', '9'))
        self.bt_buscar.place(relx= 0.3, rely=0.1, relwidth=.1, relheight= 0.15)  

        self.bt_novo = Button(self.frame_1, text= "Novo", font=('verdana', '9'))
        self.bt_novo.place(relx= 0.65, rely=0.1, relwidth=.1, relheight= 0.15) 

        self.bt_alterar = Button(self.frame_1, text= "Alterar", font=('verdana', '9'))
        self.bt_alterar.place(relx= 0.75, rely=0.1, relwidth=.1, relheight= 0.15)

        self.bt_apagar = Button(self.frame_1, text= "Apagar", font=('verdana', '9'))
        self.bt_apagar.place(relx= 0.85, rely=0.1, relwidth=.1, relheight= 0.15)

        #Labels do frame_1:
        #1-Código;
        self.lb_codigo = Label(self.frame_1, text= 'Código:', bg='lightgrey')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth= 0.078)
        #2-Nome;
        self.lb_nome = Label(self.frame_1, text= 'Nome:', bg='lightgrey')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth= 0.9)
        #2-Telefone;
        self.lb_telefone = Label(self.frame_1, text= 'Telefone:', bg='lightgrey')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth= 0.4)
        #2-Cidade;
        self.lb_cidade = Label(self.frame_1, text= 'Cidade:', bg='lightgrey')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth= 0.45)
   
    def Widgets_frame_2(self): 

        #Gerando Treeview pelo ttk:
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=('col1', 'col2','col3','col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.01, relwidth= 0.95, relheight=0.85)
        
        #Gerando Scrol Vertical
        self.scrollistaV = ttk.Scrollbar(self.frame_2, orient= 'vertical')
        self.listaCli.configure(yscroll=self.scrollistaV.set)
        self.scrollistaV.place(relx=0.96, rely=0.01, relwidth= 0.04, relheight=0.85)

        #Gerando Scrol Horizontal
        self.scrollistaH = ttk.Scrollbar(self.frame_2, orient= 'horizontal')
        self.listaCli.configure(xscroll=self.scrollistaH.set)
        self.scrollistaH.place(relx=0.01, rely=0.86, relwidth= 0.98, relheight=0.12)
        
        #selecionar tipo de tema (alt, clam, default)
        self.style.theme_use('winnative')
        
        #Estilizar tema fo Treeview selecionado
        self.style.configure('Treeview', background='silver', foreground='black',rowheight='25', fieldbackground= 'white', bd=1)
        self.style.map('Treeview', background=[('selected', 'green')])


Aplication()
