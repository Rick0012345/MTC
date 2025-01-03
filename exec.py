import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from database import carregar_pacientes_db, carregar_medicamentos_db,adicionar_paciente_db, editar_paciente_db, deletar_paciente_db, adicionar_medicamento_db, deletar_medicamento_db

class JanelaPrincipal:
    def __init__(self):
        
        self.root = ctk.CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1200x600")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Frame esquerdo para os botões Pacientes e Medicamentos
        left_frame = ctk.CTkFrame(main_frame)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
        
        btn_pacientes = ctk.CTkButton(left_frame, text="Pacientes", width=150, command=self.abrir_janela_pacientes)
        btn_pacientes.pack(pady=10)
        
        btn_medicamentos = ctk.CTkButton(left_frame, text="Medicamentos", width=150, command=self.abrir_janela_medicamentos)
        btn_medicamentos.pack(pady=10)
        # TESTANDO MUDANÇAS
        # Frame direito para o TreeView de Medicamentos
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configurar o TreeView para exibir os medicamentos
        columns = ("Nome do Medicamento", "Estoque", "Vencimento")
        tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=200, anchor=tk.CENTER)

        # Carregar medicamentos do banco de dados
        carregar_medicamentos_db(tree)

        # Configurações de redimensionamento
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

    # Função para abrir a janela de Pacientes
    def abrir_janela_pacientes(self):
        pacientes_janela = ctk.CTkToplevel(self.root)
        pacientes_janela.title("Pacientes")
        pacientes_janela.geometry("1000x600")
        pacientes_janela.transient(self.root)
        pacientes_janela.deiconify()

        # Frame para exibir e manipular os pacientes
        self.frame_pacientes = ctk.CTkFrame(pacientes_janela)
        self.frame_pacientes.pack(fill="both", expand=True)

        # Botões para Adicionar, Remover e Editar Pacientes
        btn_adicionar_paciente = ctk.CTkButton(self.frame_pacientes, text="Adicionar Paciente", command=self.adicionar_paciente)
        btn_adicionar_paciente.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        btn_remover_paciente = ctk.CTkButton(self.frame_pacientes, text="Remover Paciente", command=self.remover_paciente)
        btn_remover_paciente.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        btn_editar_paciente = ctk.CTkButton(self.frame_pacientes, text="Editar Paciente", command=None)
        btn_editar_paciente.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        #entradas_para inserção de novo paciente
        self.inp_nome = ctk.CTkEntry(self.frame_pacientes, placeholder_text="Nome")
        self.inp_nome.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.inp_idade = ctk.CTkEntry(self.frame_pacientes, placeholder_text="Idade")
        self.inp_idade.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.inp_endereco = ctk.CTkEntry(self.frame_pacientes, placeholder_text="Endereço")
        self.inp_endereco.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.inp_CPF = ctk.CTkEntry(self.frame_pacientes, placeholder_text="CPF")
        self.inp_CPF.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        # Configuração do TreeView para os pacientes
        self.columns_pacientes = ("Nome", "Idade", "Endereço", "CPF")
        self.tree_pacientes = ttk.Treeview(self.frame_pacientes, columns=self.columns_pacientes, show="headings", height=15)
        
        for col in self.columns_pacientes:
            self.tree_pacientes.heading(col, text=col)
            self.tree_pacientes.column(col, width=150, anchor=tk.CENTER)

        self.tree_pacientes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
        self.frame_pacientes.grid_columnconfigure(0, weight=1)
        
        carregar_pacientes_db(self.tree_pacientes)

    
    def abrir_janela_medicamentos(self):
        medicamentos_janela = ctk.CTkToplevel(self.root)
        medicamentos_janela.title("Medicamentos")
        medicamentos_janela.geometry("1000x600")
        medicamentos_janela.transient(self.root)
        medicamentos_janela.deiconify()

        # Frame para exibir e manipular os medicamentos
        self.frame_medicamentos = ctk.CTkFrame(medicamentos_janela)
        self.frame_medicamentos.pack(fill="both", expand=True)

        # Botões para Adicionar, Remover e Editar Medicamentos
        btn_adicionar_medicamento = ctk.CTkButton(self.frame_medicamentos, text="Adicionar Medicamento", command=self.adicionar_medicamento)
        btn_adicionar_medicamento.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        btn_remover_medicamento = ctk.CTkButton(self.frame_medicamentos, text="Remover Medicamento", command=self.remover_medicamento)
        btn_remover_medicamento.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        btn_editar_medicamento = ctk.CTkButton(self.frame_medicamentos, text="Editar Medicamento", command=None)
        btn_editar_medicamento.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        #entradas_para inserção de novo paciente
        self.inp_nome = ctk.CTkEntry(self.frame_medicamentos, placeholder_text="Nome")
        self.inp_nome.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.inp_estoque = ctk.CTkEntry(self.frame_medicamentos, placeholder_text="Estoque")
        self.inp_estoque.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.inp_validade = ctk.CTkEntry(self.frame_medicamentos, placeholder_text="Vencimento")
        self.inp_validade.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # Configuração do TreeView para os medicamentos
        self.columns_medicamentos = ("Nome do Medicamento", "Estoque", "Vencimento")
        self.tree_medicamentos = ttk.Treeview(self.frame_medicamentos, columns=self.columns_medicamentos, show="headings", height=15)
        
        #carregando os dados atualizados
        for col in self.columns_medicamentos:
            self.tree_medicamentos.heading(col, text=col)
            self.tree_medicamentos.column(col, width=150, anchor=tk.CENTER)

        self.tree_medicamentos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
        self.frame_medicamentos.grid_columnconfigure(0, weight=1)
        
        # Carregar medicamentos do banco de dados
        carregar_medicamentos_db(self.tree_medicamentos)

    def adicionar_medicamento(self):
        n1 = self.inp_nome.get()
        n2 = self.inp_estoque.get()
        n3 = self.inp_validade.get()

        if n1 == "" or n2 == "" or n3 == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
            return
        else:
            # Limpa o TreeView para evitar duplicações
            # Funciona em qualquer treeview, apesar do nome.
            self.limpar_tv_pacientes(self.tree_medicamentos)

            adicionar_medicamento_db(n1, n2, n3)
            for col in self.columns_medicamentos:
                self.tree_medicamentos.heading(col, text=col)
                self.tree_medicamentos.column(col, width=150, anchor=tk.CENTER)
            
            self.tree_medicamentos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
            self.frame_medicamentos.grid_columnconfigure(0, weight=1)
            
            
            carregar_medicamentos_db(self.tree_medicamentos)
            self.limpar_campos_medicamentos()

    def remover_medicamento(self):
        selecionado = self.tree_medicamentos.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum medicamento selecionado")
            return
        else:
        # Obter dados do medicamento selecionado
            medicamento_selecionado = self.tree_medicamentos.item(selecionado[0], "values")
            nome = medicamento_selecionado[0]
            # idade = medicamento_selecionado[1]
            # endereco = medicamento_selecionado[2]
            
            # Remover medicamento do banco de dados
            deletar_medicamento_db(nome)

            # Atualizar a Treeview
            self.limpar_tv_pacientes(self.tree_medicamentos)
            carregar_medicamentos_db(self.tree_medicamentos)

            messagebox.showinfo("Sucesso", "Medicamento removido com sucesso!")

    # Funções para manipulação (ações fictícias)
    def adicionar_paciente(self):
        n1 = self.inp_nome.get()
        n2 = self.inp_idade.get()
        n3 = self.inp_endereco.get()
        n4 = self.inp_CPF.get()

        if n1 == "" or n2 == "" or n3 == "" or n4 == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
            return
        else:
            # Limpa o TreeView para evitar duplicações
            self.limpar_tv_pacientes(self.tree_pacientes)
            adicionar_paciente_db(n1, n2, n3, n4)
            for col in self.columns_pacientes:
                self.tree_pacientes.heading(col, text=col)
                self.tree_pacientes.column(col, width=150, anchor=tk.CENTER)
            
            self.tree_pacientes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)
            self.frame_pacientes.grid_columnconfigure(0, weight=1)
            
            
            carregar_pacientes_db(self.tree_pacientes)
            self.limpar_campos_pacientes()

    def limpar_campos_medicamentos(self):
        self.inp_nome.delete(0, tk.END)
        self.inp_estoque.delete(0, tk.END)
        self.inp_validade.delete(0, tk.END)

    def limpar_campos_pacientes(self):
        self.inp_nome.delete(0, tk.END)
        self.inp_idade.delete(0, tk.END)
        self.inp_endereco.delete(0, tk.END)
        self.inp_CPF.delete(0, tk.END)

    def limpar_tv_pacientes(self, treeview):
        # Remove todas as linhas existentes
        for item in treeview.get_children():
            treeview.delete(item)

    def remover_paciente(self):
        selecionado = self.tree_pacientes.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum paciente selecionado")
            return
        else:
        # Obter dados do paciente selecionado
            paciente_selecionado = self.tree_pacientes.item(selecionado[0], "values")
            # nome = paciente_selecionado[0]
            # idade = paciente_selecionado[1]
            # endereco = paciente_selecionado[2]
            cpf = paciente_selecionado[3]  # Supondo que o CPF é o quarto campo (índice 3)
            
            # Remover paciente do banco de dados
            deletar_paciente_db(cpf)

            # Atualizar a Treeview
            self.limpar_tv_pacientes(self.tree_pacientes)
            carregar_pacientes_db(self.tree_pacientes)

            messagebox.showinfo("Sucesso", "Paciente removido com sucesso!")
            
    def atualizar_dados(self):
            n1 = self.inp_nome.get()
            n2 = self.inp_idade.get()
            n3 = self.inp_endereco.get()
            n4 = self.inp_CPF.get()

            if n1 == "" or n2 == "" or n3 == "" or n4 == "":
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
                return
            
            # Atualizar o paciente no banco de dados
            editar_paciente_db(n4, n1, n2, n3)  # CPF não muda, mas os outros dados sim
            
            # Limpar TreeView e recarregar os dados
            self.limpar_campos_pacientes(self.tree_pacientes)
            carregar_pacientes_db(self.tree_pacientes)
            
            messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
            self.limpar_campos_paciente()

            # Botão de confirmar atualização
            btn_confirmar_edicao = ctk.CTkButton(self.frame_pacientes, text="Confirmar Edição", command=self.atualizar_dados)
            btn_confirmar_edicao.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        
   
# Inicializar a aplicação
JanelaPrincipal()

