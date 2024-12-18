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

        )
        imgLabel.grid(row=0, column=0, padx=2, pady=2)

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
            command=None,
            corner_radius=15
        )
        btn_medicamentos = CTkButton(
            left_frame,
            text="Medicamentos",
            width=150,
            height=30,
            command=None,
            corner_radius=15
        )

        # Posicionamento dos botões
        btn_pacientes.grid(row=0, column=0, pady=30)
        btn_medicamentos.grid(row=5, column=0, pady=30)
        
        # Configuração da Treeview
        columns = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True,padx=10, pady=10)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=CENTER)
        
        carregar_pacientes_db(tree=tree)
        
        self.root.mainloop()

JanelaPrincipal()
