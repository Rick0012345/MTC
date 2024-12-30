from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
from database import carregar_pacientes_db, carregar_medicamentos_db, adicionar_paciente_db, editar_paciente_db, deletar_paciente_db
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
        
        carregar_pacientes_db(tree=tree)
        
        self.root.mainloop()

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
            command=None
            ).grid(row=0, column=1, padx=20, pady=10, sticky="w")
        btn_remover_paciente = CTkButton(
            btn_frame,
            text="Remover Paciente",
            command=None
            ).grid(row=0, column=2, padx=20, pady=10, sticky="w")
        btn_editar_paciente = CTkButton(
            btn_frame,
            text="Editar Paciente",
            command=None
            ).grid(row=0, column=3, padx=20, pady=10, sticky="w")
        
        inp_nome = CTkEntry(
            inp_frame,
            placeholder_text="Nome",
            placeholder_text_color="black",
            fg_color="white",
            border_color="blue"

            ).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    
        inp_idade = CTkEntry(
            inp_frame,
            placeholder_text="Idade",
            placeholder_text_color="black",
            fg_color="white",
            border_color="blue"
            ).grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        inp_endereco = CTkEntry(
            inp_frame,
            placeholder_text="Endereço",
            placeholder_text_color="black",
            fg_color="white",
            border_color="blue"
            ).grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        inp_contato = CTkEntry(
            inp_frame,
            placeholder_text="contato familiar",
             placeholder_text_color="black",
            fg_color="white",
            border_color="blue"
            ).grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        

        columns_pacientes = ("Nome", "Idade", "Contato Familiar", "CPF")
        tree_pacientes = ttk.Treeview(tv_frame_pacientes, columns=columns_pacientes, show="headings", height=15)
        
        for col in columns_pacientes:
            tree_pacientes.heading(col, text=col)
            tree_pacientes.column(col, width=150, anchor=CENTER)

        tree_pacientes.pack(fill="both", expand=True,padx=10, pady=10)
        tv_frame_pacientes.grid_columnconfigure(0, weight=1)
JanelaPrincipal()
