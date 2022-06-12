import os
os.system('cls')
from tkinter import * #módulo para interface gráfica
from tkinter import ttk # o ttk amplia as funções do tkinter
import sqlite3

class Funcs():
    def limpa_tela(self):
        self.ed_codigo.delete(0, END)
        self.ed_nome.delete(0, END)
        self.ed_telefone.delete(0, END)
        self.ed_cidade.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print('Conectando ao Banco de Dados...')
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do Banco de Dados.")
    def montaTabelas(self): # cria tabelas dentro do banco de dados
        self.conecta_bd()
        # Criar Tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente CHARVAR(40) NOT NULL, 
                telefone INTEGER(20),
                cidade CHARVAR(40)
            );        
        """)
        self.conn.commit(); print("Banco de Dados criado!")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.ed_codigo.get()
        self.nome = self.ed_nome.get()
        self.telefone = self.ed_telefone.get()
        self.cidade = self.ed_cidade.get()
    def add_cliente(self): # adiciona os valores ao banco de dados digitados na tela
        self.variaveis()
        self.conecta_bd() # conecta ao banco de dados
        self.cursor.execute(""" INSERT INTO clientes(nome_cliente, telefone, cidade)
         VALUES(?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit() # validar os dados
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
        ORDER BY cod; """) # cod, nome_cliente, telefone, cidade
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def clique_duplo(self, event):    
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.ed_codigo.insert(END, col1)
            self.ed_nome.insert(END, col2)
            self.ed_telefone.insert(END, col3)
            self.ed_cidade.insert(END, col4)
    def deletar_cliente(self):
        self.variaveis() 
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,) )
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def update_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? 
                                WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()                        
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def buscar_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.ed_nome.insert(END, '%')
        nome= self.ed_nome.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE nome_cliente LIKE "%s" ORDER BY nome_cliente ASC """ % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("",END, values=i)
        self.limpa_tela()    
        self.desconecta_bd()

class Aplication(Funcs):
    def __init__(self):
        self.root = Tk()
        self.style = ttk.Style()
        self.tela()
        self.frames_de_tela()
        self.Widgets_frame_1()
        self.Widgets_frame_2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        self.root.mainloop()
    

    def tela(self):
        self.root.title("Cadastro de Alunos")
        self.root.configure(background= '#155569')
        self.root.geometry('700x800')  
        self.root.resizable(True, True)  
        self.root.maxsize(width= 840, height=960)
        self.root.minsize(width= 600, height=800)
      
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
        self.bt_limpar = Button(self.frame_1, text= "Limpar", font=('verdana', '9'), command= self.limpa_tela )
        self.bt_limpar.place(relx= 0.05,rely=0.0,  relwidth=0.1, relheight= 0.07)   

        self.bt_buscar = Button(self.frame_1, text= "Buscar", font=('verdana', '9'), command=self.buscar_cliente)
        self.bt_buscar.place(relx= 0.15, rely=0.0, relwidth=.1, relheight= 0.07)  

        self.bt_novo = Button(self.frame_1, text= "Cadastrar", font=('verdana', '9'), command= self.add_cliente)
        self.bt_novo.place(relx= 0.425, rely=0.9, relwidth=.15, relheight= 0.07) 

        self.bt_alterar = Button(self.frame_1, text= "Alterar", font=('verdana', '9'), command=self.update_cliente)
        self.bt_alterar.place(relx= 0.75, rely=0.0, relwidth=.1, relheight= 0.07)

        self.bt_apagar = Button(self.frame_1, text= "Apagar", font=('verdana', '9'), command=self.deletar_cliente)
        self.bt_apagar.place(relx= 0.85, rely=0.0, relwidth=.1, relheight= 0.07)

        #Labels do frame_1:
        #1-Código;
        self.lb_codigo = Label(self.frame_1, text= 'Código:', bg='lightgrey')
        self.lb_codigo.place(relx=0.05, rely=0.10)

        self.ed_codigo = Entry(self.frame_1, bd=2)
        self.ed_codigo.place(relx=0.05, rely=0.2, relwidth= 0.078)
        #2-Nome;
        self.lb_nome = Label(self.frame_1, text= 'Nome:', bg='lightgrey')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.ed_nome = Entry(self.frame_1, bd=2)
        self.ed_nome.place(relx=0.05, rely=0.45, relwidth= 0.9)
        #2-Telefone;
        self.lb_telefone = Label(self.frame_1, text= 'Telefone:', bg='lightgrey')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.ed_telefone= Entry(self.frame_1, bd=2)
        self.ed_telefone.place(relx=0.05, rely=0.7, relwidth= 0.4)
        #2-Cidade;
        self.lb_cidade = Label(self.frame_1, text= 'Cidade:', bg='lightgrey')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.ed_cidade = Entry(self.frame_1, bd=2)
        self.ed_cidade.place(relx=0.5, rely=0.7, relwidth= 0.45)
   
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

        self.listaCli.place(relx=0.01, rely=0.01, relwidth= 0.95, relheight=0.95)
        
        #Gerando Scroll Vertical
        self.scrollistaV = ttk.Scrollbar(self.frame_2, orient= 'vertical', command= self.listaCli.yview)
        self.listaCli['yscrollcommand'] = self.scrollistaV.set
        self.scrollistaV.place(relx=0.96, rely=0.01, relwidth= 0.04, relheight=0.95)

        ''' #Gerando Scroll Horizontal
        self.scrollistaH = ttk.Scrollbar(self.frame_2, orient= 'horizontal', command= self.listaCli.xview)
        self.listaCli['xscrollcommand'] = self.scrollistaH.set
        self.scrollistaH.place(relx=0.01, rely=0.86, relwidth= 0.99, relheight=0.12)'''
        
        #selecionar tipo de tema (alt, clam, default)
        self.style.theme_use('winnative')
        
        #Estilizar tema fo Treeview selecionado
        self.style.configure('Treeview', background='silver', foreground='black',rowheight='25', fieldbackground= 'silver', bd=1)
        self.style.map('Treeview', background=[('selected', 'green')])
        self.listaCli.bind("<Double-1>", self.clique_duplo)

    def Menus(self):
        menubar = Menu(self.frame_1)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        def Quit() : self.root.destroy()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "Ajuda", menu= filemenu2)
        menubar.add_cascade(label = "Organizar clientes por:", menu= filemenu3)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label= "Instruções de uso", command=self.janela_instrucoes)
        filemenu3.add_command(label= "Código", command=self.organizar_cod)
        filemenu3.add_command(label= "Nome", command=self.organizar_nome)
   
    def organizar_nome(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
        ORDER BY nome_cliente ASC; """) # cod, nome_cliente, telefone, cidade
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def organizar_cod(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
        ORDER BY cod; """) # cod, nome_cliente, telefone, cidade
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()    

    def janela_instrucoes(self):  
  
        self.Janela_2 = Toplevel()
        self.Janela_2.title('Nova Janela')
        self.Janela_2.configure(background= '#155569')
        self.Janela_2.geometry('800x400')
        self.Janela_2.resizable(False, True )
        self.Janela_2.transient(self.root)
        self.Janela_2.focus_force()
        self.Janela_2.grab_set()
       

        #Label com instruções:
        self.lb_instrucoes = Label(self.Janela_2, text= 
        '''Instruções de uso:

        1- Para cadastrar novo cliente informe os dados nos campos e aperte o botão 'Cadastrar';
        2- O campo 'código' não deve ser preenchido na hora do cadastro;
        3- Para limpar todos os campos de preenchimento clique em 'Limpar';
        4- Para alterar dados do cliente dê duplo em seu nome na lista de cadatro e depois selecione o botão 'Alterar';
        5- Para apagar cadastro de cliente dê duplo em seu nome na lista na lista de cadastro e depois selecione o botão 'Apagar';
        6- Para buscar um cliente digite na secção "Nome" o nome da pessoa que deseja encontrar.
        7- Para mudar ordem de organização da lista va no menu superior e escolha uma das opções sugeridas.
        ''', bg='lightgrey', justify= LEFT, anchor='n')
        self.lb_instrucoes.place(relx=0.02, rely=0.02,relwidth=0.96, relheight=0.96)
        
    ''' def change_to_greet(self):
        self.frame_1.pack(fill='both', expand=1)
        self.frame_2.pack_forget()

    def change_to_order(self):
        self.frame_2.pack(fill='both', expand=1)
        self.frame_1.pack_forget()  ''' 
        
Aplication()
