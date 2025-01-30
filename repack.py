from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
from database import *
from PIL import Image

class JanelaPrincipal:

    def __init__(self):
        self.root = CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1250x750")
        self.root.minsize(1250, 750)
        
        # Frame principal que conterá os outros frames
        # Configuração do layout da janela principal para expandir
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Frame principal que conterá os outros frames
        main_frame = CTkFrame(
            self.root,
            fg_color="lightblue",
            corner_radius=15,
            height=750
        )
        main_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        imagem = Image.open("mtc_logo.png")  # Insira o caminho correto da imagem
        ctk_imagem = CTkImage(light_image=imagem, size=(140, 80))
        
        # Frame superior com a imagem
        imgLabel = CTkLabel(
            self.root,
            text="",
            image=ctk_imagem,
            anchor="n",

        ).grid(row=0, column=0, padx=2, pady=2)
        

        # Frames internos
        left_frame = CTkFrame(
            main_frame,
            fg_color="lightblue",
            corner_radius=15,
            height=500
        )
        tree_frame = CTkFrame(
            main_frame,
            fg_color="lightblue",
            corner_radius=10,
            height=800
        )
        
        # Layout dos frames internos
        left_frame.pack(padx=10, pady=40, side=LEFT, anchor="nw", fill=Y)
        tree_frame.pack(pady=40, side=RIGHT, fill=BOTH, expand=True)
        
        # Botões
        btn_pacientes = CTkButton(
            left_frame,
            text="Pacientes",
            width=150,
            height=30,
            command= self.abrir_janela_pacientes,
            corner_radius=15
        ).grid(row=0, column=0, pady=30)
        btn_medicamentos = CTkButton(
            left_frame,
            text="Medicamentos",
            width=150,
            height=30,
            command=None,
            corner_radius=15
        ).grid(row=5, column=0, pady=30)

        
        # Configuração da Treeview
        columns = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True,padx=10, pady=10)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=CENTER)

        # Isso deveria ser removido e deveria-se carregar medicamentos e não pacientes.
        # carregar_pacientes_db(tree=tree)

        menu = Menu(self.root, tearoff=0)
        menu_item_1 = Menu(menu, tearoff=0,)
        menu_item_1.add_command(label="Acessar o banco", font=("Arial", 10), command=self.gerenciar_banco)
        menu.add_cascade(label="Menu", menu=menu_item_1)
        self.root.config(menu=menu)

        self.root.mainloop()

    def gerenciar_banco(self):
            banco_janela = CTkToplevel(self.root, width=200 ,height=200)
            banco_janela.title("gerenciador de banco de dados")
            banco_janela.geometry("1000x600")
            banco_janela.transient(self.root)
            banco_janela.deiconify()
            banco_janela.mainloop()  
    def abrir_janela_pacientes(self):
            
        pacientes_janela = CTkToplevel(self.root)
        pacientes_janela.title("Pacientes")
        pacientes_janela.geometry("1000x600")
        pacientes_janela.transient(self.root)
        pacientes_janela.deiconify()
        
        # Configurando peso das colunas e linhas
        pacientes_janela.columnconfigure(0, weight=1)  # Coluna da esquerda
        pacientes_janela.columnconfigure(1, weight=1)  # Coluna da direita
        pacientes_janela.rowconfigure(0, weight=1)     # Linha superior
        pacientes_janela.rowconfigure(1, weight=0)     # Linha inferior
        
        #frames

        tv_frame_pacientes = CTkFrame(
            pacientes_janela,
            fg_color="lightblue",
            
            height=200,
            width=300
        )
        tv_frame_pacientes.grid(row=0, column=1, sticky="nsew")

        inp_frame = CTkFrame(
            pacientes_janela,
            fg_color="lightblue",
            
            height=200,
            width=200
        )
        
        inp_frame.grid(row=0, column=0, sticky="nsew")
        inp_frame.columnconfigure(0, weight=1)  # Faz a coluna 0 expandir

        btn_frame = CTkFrame(
            pacientes_janela,
            fg_color="lightblue",
            height=70,   
        )
        btn_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        btn_frame.columnconfigure(0, weight=1)  
        btn_frame.columnconfigure(1, weight=0) 
        btn_frame.columnconfigure(2, weight=0) 
        btn_frame.columnconfigure(3, weight=0)  
        btn_frame.columnconfigure(4, weight=1) 

        btn_adicionar_paciente = CTkButton(
            btn_frame,
            text="Adicionar Paciente",
            command=self.adicionar_paciente,
            ) # Há uma inconsistência aqui. btn_adicionar_paciente possui estrutura diferente dos outros botões 
                # Ele se refere à variável novamente para acessar o atributo grid.
        btn_adicionar_paciente.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        
        btn_remover_paciente = CTkButton(
            btn_frame,
            text="Remover Paciente",
            command=self.remover_paciente
            )
        btn_remover_paciente.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        btn_editar_paciente = CTkButton(
            btn_frame,
            text="Editar Paciente",
            command=None
            )
        btn_editar_paciente.grid(row=0, column=3, padx=20, pady=10, sticky="w")
        
        self.inp_nome = CTkEntry(
            inp_frame,
            placeholder_text="Nome",
            placeholder_text_color="#8c9190",
            fg_color="white",
            border_color="blue",
            text_color="black"
            )
        self.inp_nome.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.inp_idade = CTkEntry(
            inp_frame,
            placeholder_text="Idade",
            placeholder_text_color="#8c9190",
            fg_color="white",
            border_color="blue",
            text_color="black"

            )
        self.inp_idade.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        self.inp_endereco = CTkEntry(
            inp_frame,
            placeholder_text="Endereço",
            placeholder_text_color="#8c9190",
            fg_color="white",
            border_color="blue",
            text_color="black"
            )
        self.inp_endereco.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.inp_contato = CTkEntry(
            inp_frame,
            placeholder_text="contato familiar",
            placeholder_text_color="#8c9190",
            fg_color="white",
            border_color="blue",
            text_color="black"
            )
        self.inp_contato.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.inp_CPF = CTkEntry(
            inp_frame,
            placeholder_text="CPF",
            placeholder_text_color="#8c9190",
            fg_color="white",
            border_color="blue",
            text_color="black"
            )
        self.inp_CPF.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.inp_sexo = CTkOptionMenu(
            inp_frame,
            values=["F", "M"],
            fg_color="white",
            text_color="black"
            )
        self.inp_sexo.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
        
        self.columns_pacientes = ("id", "Nome", "Idade", "Contato Familiar", "CPF", "Endereço", "Sexo")
        self.tree_pacientes = ttk.Treeview(tv_frame_pacientes, columns=self.columns_pacientes, show="headings", height=15)
        
        for col in self.columns_pacientes:
            self.tree_pacientes.heading(col, text=col)
            self.tree_pacientes.column(col, width=150, anchor=CENTER)

        self.tree_pacientes.column("id", width=50, anchor=CENTER) 
        carregar_pacientes_db(self.tree_pacientes)
        self.tree_pacientes.pack(fill="both", expand=True,padx=10, pady=10)
        tv_frame_pacientes.grid_columnconfigure(0, weight=1)
        
    def limpar_tv_pacientes(self, treeview):
    # Remove todas as linhas existentes
        for item in treeview.get_children():
            treeview.delete(item)
#
    def limpar_campos_pacientes(self):
        self.inp_nome.delete(0, END)
        self.inp_idade.delete(0, END)
        self.inp_endereco.delete(0, END)
        self.inp_contato.delete(0, END)
        self.inp_CPF.delete(0, END)

    def adicionar_paciente(self):
        n1 = self.inp_nome.get()
        n2 = int(self.inp_idade.get())
        n3 = self.inp_sexo.get()
        n4 = self.inp_contato.get()
        n5 = self.inp_endereco.get()
        n6 = int(self.inp_CPF.get())
        print(n1, n2, n3, n4, n5, n6)
        print(type(n1), type(n2), type(n3), type(n4), type(n5), type(n6))

        if n1 == "" or n2 == "" or n3 == "" or n4 == "" or n5 == "" or n6 == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
            return
        else:
            self.limpar_tv_pacientes(self.tree_pacientes)
            adicionar_paciente_db(n1, n2, n3, n4, n5, n6)
            for col in self.columns_pacientes:
                self.tree_pacientes.heading(col, text=col)
                self.tree_pacientes.column(col, width=150, anchor=CENTER)
            
            self.tree_pacientes.pack(fill="both", expand=True,padx=10, pady=10)
            
            carregar_pacientes_db(self.tree_pacientes)
            self.limpar_campos_pacientes()
            
    def remover_paciente(self):
        selecionado = self.tree_pacientes.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum paciente selecionado")
            return
        else:
            paciente_selecionado = self.tree_pacientes.item(selecionado[0], "values")

            pk = paciente_selecionado[0]
            
            # Remover paciente do banco de dados
            deletar_paciente_db(pk=pk)

            # Atualizar a Treeview
            self.limpar_tv_pacientes(self.tree_pacientes)
            carregar_pacientes_db(self.tree_pacientes)

            messagebox.showinfo("Sucesso", "Paciente removido com sucesso!")
            
JanelaPrincipal()
