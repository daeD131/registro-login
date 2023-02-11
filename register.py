import pyodbc
from tkinter import *

dados_conexao = (
    "Driver={SQL Server};"
    "Server=sua_instancia;"
    "Database=Usuarios;"
    "UID=sa;"
    "PWD=senha_seu_bancoDeDados;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão realizada com sucesso!")

cursor = conexao.cursor()

def confirmar():
    login = str(campo_login.get())
    senha = str(campo_senha.get())
    print("Dados coletados com sucesso!")
    inserir_dados = f"""Insert into Dados_usuarios(login_usuario, senha_usuario)
Values
    ('{login}', '{senha}')"""

    mostrar_dados = """Select * from Dados_usuarios"""
    cursor.execute(inserir_dados)
    cursor.execute(mostrar_dados)
    cursor.commit()

window = Tk()

lb1 = Label(window, text="Registrar-se:")
lb1.grid(column=1, row=0, padx=5, pady=0)

lb2 = Label(window, text="Login:")
lb2.grid(column=0, row=1, padx=5, pady=0)

campo_login = Entry(window, width=15)
campo_login.grid(column=1, row=1, padx=5, pady=0)

lb3 = Label(window, text="Senha:")
lb3.grid(column=0, row=3, padx=5, pady=0)

campo_senha = Entry(window, width=15)
campo_senha.grid(column=1, row=3, padx=5, pady=0)

confirma = Button(window, text="Confirmar", command=confirmar)
confirma.grid(column=3, row=5, padx=5, pady=5)

window.mainloop()