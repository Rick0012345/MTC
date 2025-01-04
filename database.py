import sqlite3
import tkinter as tk

# Função para conectar ao banco de dados
def conectardb():
    try:
        return sqlite3.connect('controle_medicamentos.db')
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para adicionar um paciente
def adicionar_paciente_db(nome, idade, endereco, CPF):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO pacientes (nome, idade, endereco, CPF) VALUES (?, ?, ?, ?)', (nome, idade, endereco, CPF))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao adicionar paciente: {e}")

# Função para adicionar um medicamento
def adicionar_medicamento_db(nome, estoque, vencimento):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO medicamentos (nome, estoque, vencimento) VALUES (?, ?, ?)', (nome, estoque, vencimento))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao adicionar medicamento: {e}")

# Função para carregar pacientes no TreeView
def carregar_pacientes_db(tree):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, idade, endereco, CPF FROM pacientes')
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)
    except sqlite3.Error as e:
        print(f"Erro ao carregar pacientes: {e}")

# Função para carregar medicamentos no TreeView
def carregar_medicamentos_db(tree):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, estoque, vencimento FROM medicamentos')
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)
    except sqlite3.Error as e:
        print(f"Erro ao carregar medicamentos: {e}")

# Função para gerar a base de dados (criar tabelas)
def gerardb():
    try:
        with sqlite3.connect('controle_medicamentos.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                idade INTEGER NOT NULL,
                                endereco TEXT NOT NULL,
                                CPF INTEGER NOT NULL
                            )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS medicamentos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                estoque INTEGER NOT NULL,
                                vencimento TEXT NOT NULL
                            )''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao gerar o banco de dados: {e}")


# Função para editar um paciente no banco de dados
def editar_paciente_db(nome, idade, endereco, CPF):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE pacientes
                SET nome = ?, idade = ?, endereco = ?
                WHERE CPF = ?
            ''', (nome, idade, endereco, CPF))
            conn.commit()
            print(f"Paciente com CPF {CPF} atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao editar paciente: {e}")

# Função para deletar um paciente no banco de dados
def deletar_paciente_db(CPF):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pacientes WHERE CPF = ?', (CPF,))
            conn.commit()
            print(f"Paciente com CPF {CPF} removido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao deletar paciente: {e}")

def deletar_medicamento_db(nome):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM medicamentos WHERE nome = ?', (nome,))
            conn.commit()
            print(f"Medicamento {nome} removido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao deletar medicamento: {e}")

# Gerar a base de dados ao inicializar
gerardb()
