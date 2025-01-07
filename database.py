import tkinter as tk
import mysql.connector
from mysql.connector import Error

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

def carregar_pacientes_db(tree):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT pk, nome, idade, endereco, CPF FROM pacientes')
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



def gerardb():
    try:
        # Conexão com o servidor MySQL
        conn = mysql.connector.connect(
            host='localhost',  # Substitua pelo endereço do servidor MySQL
            user='seu_usuario',  # Substitua pelo seu usuário do MySQL
            password='sua_senha'  # Substitua pela sua senha do MySQL
        )
        
        if conn.is_connected():
            cursor = conn.cursor()

            # Criação do banco de dados, se não existir
            cursor.execute("CREATE DATABASE IF NOT EXISTS controle_medicamentos")
            cursor.execute("USE controle_medicamentos")  # Seleciona o banco

            # Criação da tabela "pacientes"
            cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                                pk INT AUTO_INCREMENT PRIMARY KEY,
                                nome VARCHAR(255) NOT NULL,
                                idade INT NOT NULL,
                                sexo ENUM('M', 'F') NOT NULL,
                                contato VARCHAR(15) NOT NULL,
                                endereco TEXT NOT NULL,
                                CPF BIGINT NOT NULL UNIQUE
                            )''')

            # Criação da tabela "medicamentos"
            cursor.execute('''CREATE TABLE IF NOT EXISTS medicamentos (
                                pk INT AUTO_INCREMENT PRIMARY KEY,
                                nome VARCHAR(255) NOT NULL,
                                estoque INT NOT NULL,
                                vencimento DATE NOT NULL
                            )''')

            conn.commit()
            print("Banco de dados e tabelas criados com sucesso.")
    
    except Error as e:
        print(f"Erro ao gerar o banco de dados: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

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
def deletar_paciente_db(pk):
    try:
        with conectardb() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pacientes WHERE pk = ?', (pk,))
            conn.commit()
            print(f"Paciente com a primary key {pk} removido com sucesso!")
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
