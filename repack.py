#atualizacao do app com intuito de facilitar o desenvolvimento

from tkinter import *
from customtkinter import *

class JanelaPrincipal:

    def __init__(self):
        
        self.root = CTk()
        self.root.title("MTC - Controle de Medicamentos")
        self.root.geometry("1250x750")
        self.root.minsize(1250, 750)
        

        # Frames
        left_frame = CTkFrame(self.root, fg_color="lightblue", corner_radius=15,height=500)
        tree_frame=CTkFrame(self.root, fg_color="lightblue", corner_radius=10, height=800)

        left_frame.pack(padx=10, pady=40,side=LEFT,anchor="nw",fill=Y)
        tree_frame.pack(pady=40,fill=X)
        
        #Buttons
        btn_pacientes = CTkButton(left_frame, text="Pacientes", width=150, command=None)
        btn_medicamentos = CTkButton(left_frame, text="Medicamentos", width=150, command=None)


        btn_pacientes.grid(row=0, column=0)
        btn_medicamentos.grid(row=5, column=0,pady=50,)



        self.root.mainloop()



JanelaPrincipal()