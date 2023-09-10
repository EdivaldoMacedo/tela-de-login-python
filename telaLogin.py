import sys
import tkinter as tk
import tkinter.ttk as ttk

class AuthenticationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x606+647+284")
        self.root.title("Authentication")
        self.root.configure(background="#39007a")

        self.show_login_frame()  # Inicialmente, exibe a janela de login
        
    def show_login_frame(self):
        
        self.frame_login = tk.Frame(self.root)
        self.frame_login.place(relx=0.217, rely=0.182, relheight=0.668, relwidth=0.575)
        self.frame_login.configure(relief='flat')
        self.frame_login.configure(borderwidth="2")
        self.frame_login.configure(background="#0d1f42")

        self.Entry1 = tk.Entry(self.frame_login)
        self.Entry1.place(relx=0.116, rely=0.272, height=20, relwidth=0.736)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.frame_login, show='*')
        self.Entry2.place(relx=0.116, rely=0.494, height=20, relwidth=0.736)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label1_login = tk.Label(self.frame_login)
        self.Label1_login.place(relx=0.377, rely=0.049, height=31, width=76)
        self.Label1_login.configure(background="#0d1f42")
        self.Label1_login.configure(font="-family {SimSun} -size 20")
        self.Label1_login.configure(foreground="#ffffff")
        self.Label1_login.configure(text='''Login''')

        self.Label1_login_1 = tk.Label(self.frame_login)
        self.Label1_login_1.place(relx=0.116, rely=0.173, height=31, width=106)
        self.Label1_login_1.configure(background="#0d1f42")
        self.Label1_login_1.configure(font="-family {SimSun} -size 20")
        self.Label1_login_1.configure(foreground="#ffffff")
        self.Label1_login_1.configure(text='''Usuario''')

        self.Label1_login_2 = tk.Label(self.frame_login)
        self.Label1_login_2.place(relx=0.087, rely=0.395, height=31, width=106)
        self.Label1_login_2.configure(background="#0d1f42")
        self.Label1_login_2.configure(font="-family {SimSun} -size 20")
        self.Label1_login_2.configure(foreground="#ffffff")
        self.Label1_login_2.configure(text='''Senha''')

        self.Button1_login = tk.Button(self.frame_login, command=self.login_backend)
        self.Button1_login.place(relx=0.087, rely=0.593, height=54, width=117)
        self.Button1_login.configure(background="#d8a0c5")
        self.Button1_login.configure(foreground="#000000")
        self.Button1_login.configure(text='''Logar''')

        self.Button1_register = tk.Button(self.frame_login, command=self.show_registration_frame)
        self.Button1_register.place(relx=0.58, rely=0.593, height=54, width=117)
        self.Button1_register.configure(background="#d8a0c5")
        self.Button1_register.configure(foreground="#000000")
        self.Button1_register.configure(text='''Cadastrar''')

    def show_registration_frame(self):
        self.frame_login.destroy()
        self.frame_register = tk.Frame(self.root)
        self.frame_register.place(relx=0.217, rely=0.182, relheight=0.668, relwidth=0.575)
        self.frame_register.configure(relief='flat')
        self.frame_register.configure(borderwidth="2")
        self.frame_register.configure(background="#0d1f42")

        self.Entry1_register = tk.Entry(self.frame_register)
        self.Entry1_register.place(relx=0.116, rely=0.272, height=20, relwidth=0.736)
        self.Entry1_register.configure(background="white")
        self.Entry1_register.configure(font="TkFixedFont")
        self.Entry1_register.configure(foreground="#000000")
        self.Entry1_register.configure(insertbackground="black")

        self.Entry2_register = tk.Entry(self.frame_register, show='*')
        self.Entry2_register.place(relx=0.116, rely=0.494, height=20, relwidth=0.736)
        self.Entry2_register.configure(background="white")
        self.Entry2_register.configure(font="TkFixedFont")
        self.Entry2_register.configure(foreground="#000000")
        self.Entry2_register.configure(insertbackground="black")

        self.Label1_register = tk.Label(self.frame_register)
        self.Label1_register.place(relx=0.377, rely=0.049, height=31, width=76)
        self.Label1_register.configure(background="#0d1f42")
        self.Label1_register.configure(font="-family {SimSun} -size 20")
        self.Label1_register.configure(foreground="#ffffff")
        self.Label1_register.configure(text='''Cadastro''')

        self.Label1_register_1 = tk.Label(self.frame_register)
        self.Label1_register_1.place(relx=0.116, rely=0.173, height=31, width=106)
        self.Label1_register_1.configure(background="#0d1f42")
        self.Label1_register_1.configure(font="-family {SimSun} -size 20")
        self.Label1_register_1.configure(foreground="#ffffff")
        self.Label1_register_1.configure(text='''Usuario''')

        self.Label1_register_2 = tk.Label(self.frame_register)
        self.Label1_register_2.place(relx=0.087, rely=0.395, height=31, width=106)
        self.Label1_register_2.configure(background="#0d1f42")
        self.Label1_register_2.configure(font="-family {SimSun} -size 20")
        self.Label1_register_2.configure(foreground="#ffffff")
        self.Label1_register_2.configure(text='''Senha''')

        self.Button1_register_3 = tk.Button(self.frame_register, command=self.register_backend)
        self.Button1_register_3.place(relx=0.58, rely=0.593, height=54, width=117)
        self.Button1_register_3.configure(background="#d8a0c5")
        self.Button1_register_3.configure(foreground="#000000")
        self.Button1_register_3.configure(text='''Cadastrar''')

        

        self.TSeparator1 = ttk.Separator(self.frame_register)
        self.TSeparator1.place(relx=0.493, rely=0.568, relheight=0.148)

    def login_backend(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.strip(), usuarios))
        senhas = list(map(lambda x: x.strip(), senhas))

        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('Usuário logado')
                self.root.destroy()
                logado = True

        if not logado:
            print('Usuário ou senha incorretos')

    def register_backend(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1_register.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2_register.get() + '\n')
            
            print('Usuário cadastrado com sucesso!')
            self.show_login_frame()  # Chama a função para exibir a janela de login após o cadastro
 
        except Exception as e:
            print('Houve um erro:', str(e))
            
    def run(self):
        self.root.mainloop()

app = AuthenticationApp()
app.run()






