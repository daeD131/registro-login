import pyodbc
from tkinter import *

dados_conexao = (
    "Driver={SQL Server};"
    "Server=sua_instancia;"
    "Database=Dados_usuarios;"
    "UID=sa;"
    "PWD=senha_seu_bancoDeDados;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão realizada com sucesso!")

cursor = conexao.cursor()

def logar():
    consulta = """Select * from Dados_usuarios"""
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    login = str(campo_login.get())
    senha = str(campo_senha.get())
    for linha in linhas:
        if login not in linhas[0] and senha not in linhas[1]:
            print("Login ou senha incorretos!!")
        else:
            print("Login realizado com sucesso!")


window = Tk()

lb1 = Label(window, text="Bem-vindo(a) ao sistema!\nEntre com login e senha")
lb1.grid(column=1, row=0, padx=5, pady=5)

lb2 = Label(window, text="Login:")
lb2.grid(column=0, row=1, padx=0, pady=0)

campo_login = Entry(window, width=15)
campo_login.grid(column=1, row=1, padx=0, pady=0)

lb3 = Label(window, text="Senha:")
lb3.grid(column=0, row=2, padx=0, pady=0)

campo_senha = Entry(window, width=15)
campo_senha.grid(column=1, row=2, padx=0, pady=0)

entrar = Button(window, text="Entrar", command=logar)
entrar.grid(column=3, row=3, padx=5, pady=5)
cursor.commit()

window.mainloop()