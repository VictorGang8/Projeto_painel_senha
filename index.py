from tkinter import * 
from tkinter import messagebox

cliente=Tk()
cliente.title("Solicitar Senha")
cliente.geometry("300x350")
cliente.configure(background="lightgreen")

# VARIÁVEIS COMPARTILHADAS
contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("***")

# TELA 2 (ADMINISTRADOR)
admin = Toplevel(cliente)
admin.title("Adminitrador")
admin.geometry("300x350")
admin.configure(bg="darkblue")

#Lista da fila no admin
Label(admin, text="Fila de Senhas", font=("Arial", 14)).pack(pady=10)

lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

#TELA 3 (PAINEL)
painel = Toplevel(cliente)
painel.title("Painel de Senhas")
painel.geometry("400x300")
painel.configure(bg="pink")

Label(painel, text="Senha Atual", font=("Arial,20")).pack(pady=20)

Label(
    painel,
    textvariable=senha_atual,
    font=("Arial, 40"),
    fg="red"
).pack(pady=20)

# FUNÇÕES
def solicitar_senha():
    global contador
    
    senha = f"A{contador:03}"
    fila.append(senha)
    
    lista_admin.insert(END, senha)
    
    messagebox.showinfo("Senha gerada", "Sua senha é {}".format(senha))
    
    contador +=1
    
def chamar_senha():
    if len(fila) == 0:
        messagebox.showwarning("Aviso", "Fila vazia!")
    else:
        senha = fila.pop(0)
        
        lista_admin.delete(0)
        
        senha_atual.set(senha)

Label(cliente, text="Retirar Senha", font=("Arial", 14)).pack(pady=10)   

Button(
    cliente,
    text="Gerar senha",
    width=30,
    background="gray",
    command=solicitar_senha
).pack(pady=10)

Button(
    admin,
    text="Chamar Próxima",
    width=30,
    background="gray",
    command=chamar_senha
).pack(pady=10)

#Execução
cliente.mainloop()