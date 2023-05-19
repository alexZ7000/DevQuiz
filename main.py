from tkinter import *
from tkinter.messagebox import *
import smtplib
import email.message
import pygame.mixer_music
from time import sleep

root = Tk()  # Janela
root.title("DevQuiz")  # Título da janela
x, y = (root.winfo_screenwidth()), (root.winfo_screenheight())  # Pega a resolução do monitor sem considerar a escala
root.geometry(f'{x}x{y}')  # Dimensão da tela
root.minsize(1910, 1070)  # Resolução mínima para redimencionalizar
root.maxsize(1920, 1080)  # Forçar resolução Full HD (1920x1080) do DevQuiz
root.attributes("-fullscreen", 1)  # Colocar o DevQuiz em tela cheia

# IMAGENS
dev_quiz_logo = PhotoImage(file=r"Imagens\DevQuiz.png")
dev_quiz_logo_pequena = PhotoImage(file=r"Imagens\DevQuizPequeno.png")
jogar_img = PhotoImage(file=r"Imagens\JogarTemaClaro.png")
instrucoes = PhotoImage(file=r"Imagens\InstrucoesTemaClaro.png")
configuracoes = PhotoImage(file=r"Imagens\ConfiguraçõesTemaClaro.png")
sair = PhotoImage(file=r"Imagens\SairTemaClaro.png")
bg_test = PhotoImage(file=r"Imagens\BGTest.png")
senha = PhotoImage(file=r"Imagens\SenhaTemaEscuro.png")
user = PhotoImage(file=r"Imagens\UsernameTemaEscuro.png")


# FIM DAS IMAGENS

# Classe que irá definir todos os itens que todos os "Menu" vão usar
class Menu():
    # Criação da minha tela
    def __init__(self):
        self.frame = Frame(root, bg="#ccccff")
        self.build_screen()

    # Função para mudar de tema "Claro" para tema "Escuro"
    c = 0

    def change_theme(self):
        self.c = self.c + 1
        if self.c % 2 == 0:
            self.theme_txt.set("Tema Claro")
            self.frame.config(bg="#ccccff")
        else:
            self.theme_txt.set("Tema Escuro")
            self.frame.config(bg="#1D1D66")

    # Função para colocar os objetos referenciados no "DevSystem" em todas as Classes que herdarem de "Menu"
    def Set_DevSystem(self, DevSystem):
        self.DevSystem = DevSystem

    # Função para mostrar todos os widgets que forem "self.frame"
    def show(self):
        self.frame.pack(fill=BOTH, expand=True)

    # Função para esconder widgets que não serão mais usados em uma tela nova e para excluir caracteres inseridos nos "Entry"
    def hide(self):
        self.frame.forget()
        self.reset_entry()


# Tela "Esqueci minha senha"
class MenuPasswordForget(Menu):

    # Construtor
    def __init__(self, menu_login):
        super().__init__()
        self.menu_login = menu_login

    # Função para enviar e-mail para o usuário
    def send_email(self):
        self.corpo_email = """
        <p>     Olá, vimos que você esqueceu sua senha,<br>
        Mas não se preocupe, estamos aqui para te ajudar<br>
        Acesse o link abaixo para alterar sua senha:<br><br>
        youtube.com<br><br>Mas caso não tenha sido você que<br>
        tenha pedido para alterar sua senha DevQuiz<br>
        Não se preocupe, apenas ignore este e-mail.<br><br>
        Obrigado e Tenha um ótimo dia!</p>
        """
        self.msg = email.message.Message()
        self.msg['Subject'] = "Pedido para alterar senha DevQuiz"
        self.msg['From'] = "botdevquiz@gmail.com"
        self.msg['To'] = f"{self.user_email}"
        self.password = 'imqcmyfdcrrzhumt'
        self.msg.add_header('Content-Type', 'text/html')
        self.msg.set_payload(self.corpo_email)

        self.s = smtplib.SMTP('smtp.gmail.com: 587')
        self.s.starttls()
        self.s.login(self.msg['From'], self.password)
        self.s.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string().encode('utf-8'))
        print("E-mail enviado")

    # Função para limpar os caracteres inseridos no "Entry"
    def reset_entry(self):
        self.password_forget_entry.delete(0, END)

    # Função para o usuário voltar para a tela "Login"
    def back_password_forget(self):
        self.DevSystem.menu_login.show()
        self.hide()

    # Função para captar os dados que o usuário digitou no "Esqueci minha senha" e chamar a função "send_email"
    def get_user_info_password_forget(self):
        self.user_email = self.password_forget_entry.get()
        self.send_email()

    # Construir a tela "Esqueci Minha Senha"
    def build_screen(self):
        self.frame.config(bg="black")
        Label(self.frame,
              fg="white",
              bg="black",
              text="""
    Por favor, nos informe seu e-mail
Para que possamos mandar o e-mail de troca de senha 
em sua box do e-mail
Cheque sua caixa de SPAM""",
              font=("Kristen ITC", 14),
              width=50).place(x=x / 2 - 350, y=y / 2 - 250)
        Label(self.frame,
              fg="white",
              bg="black",
              text="E-mail:",
              font=("Kristen ITC", 14)).place(x=x / 2 - 275, y=y / 2 - 100)

        self.password_forget_entry = Entry(self.frame, font=("Kristen ITC", 14), bd=4, width=30)
        self.password_forget_entry.place(x=x / 2 - 200, y=y / 2 - 100)

        self.confirm_button = Button(self.frame,
                                     text="Confirmar",
                                     font=("Kristen ITC", 14),
                                     fg="white",
                                     bg="black",
                                     width=16,
                                     borderwidth=2,
                                     cursor="hand2",
                                     command=self.get_user_info_password_forget).place(x=x / 2 - 200, y=y / 2)
        Button(self.frame,
               fg="white",
               bg="black",
               cursor="hand2",
               text="Voltar",
               font=("Kristen ITC", 14),
               command=self.back_password_forget).place(x=x / 2 + 50, y=y / 2)


# Tela "Registrar-se"
class MenuSignUp(Menu):

    # Construtor
    def __init__(self, menu_login):
        super().__init__()
        self.menu_login = menu_login

    # Função para o usuário voltar para a tela "Login"
    def back_menu_sign_up(self):
        self.DevSystem.menu_login.show()
        self.hide()

    # Função para captar os dados que o usuário digitou no "Sign up"
    def get_user_info_sign_up(self):
        print(self.click.get())
        print(self.sign_up_name.get())
        print(self.sign_up_username.get())
        print(self.sign_up_email.get())
        print(self.sign_up_password.get())
        print(self.sign_up_confirm_password.get())

    # Função para limpar os caracteres inseridos no "Entry"
    def reset_entry(self):
        self.sign_up_name.delete(0, END)
        self.sign_up_username.delete(0, END)
        self.sign_up_email.delete(0, END)
        self.sign_up_password.delete(0, END)
        self.sign_up_confirm_password.delete(0, END)
        self.click.set("Selecione seu Curso")

    # Função para construir a tela "Registrar-se"
    def build_screen(self):
        Label(self.frame,
              font=("Kristen ITC", 40),
              text="REGISTRAR-SE",
              bg="#E3F2F8").place(x=x / 2 - 200, y=25)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              text="    Nome:    ").place(x=x / 2 - 200, y=150)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              text="  Username:  ").place(x=x / 2 - 200, y=200)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              text="    E-mail:    ").place(x=x / 2 - 200, y=250)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              text="    Senha:    ").place(x=x / 2 - 200, y=300)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              text="Confirme sua Senha:").place(x=x / 2 - 200, y=350)

        self.click = StringVar(self.frame)
        self.select_course = OptionMenu(self.frame,
                                        self.click,
                                        "Administração",
                                        "Ciências da Computação",
                                        "Design",
                                        "Engenharia da Computação",
                                        "Outras Engenharias",
                                        "Sistemas de Informação")
        self.click.set("Selecione seu Curso")
        self.select_course.place(x=x / 2 - 200, y=400)

        self.sign_up_name = Entry(self.frame,
                                  font=("Kristen ITC", 12),
                                  bd=4,
                                  width=30)

        self.sign_up_name.place(x=x / 2, y=150)

        self.sign_up_username = Entry(self.frame,
                                      font=("Kristen ITC", 12),
                                      bd=4,
                                      width=30)
        self.sign_up_username.place(x=x / 2, y=200)

        self.sign_up_email = Entry(self.frame,
                                   font=("Kristen ITC", 12),
                                   bd=4,
                                   width=30)
        self.sign_up_email.place(x=x / 2, y=250)

        self.sign_up_password = Entry(self.frame,
                                      font=("Kristen ITC", 12),
                                      bd=4,
                                      width=30,
                                      show="*")

        self.sign_up_password.place(x=x / 2, y=300)

        self.sign_up_confirm_password = Entry(self.frame,
                                              font=("Kristen ITC", 12),
                                              bd=4,
                                              width=30,
                                              show="*")

        self.sign_up_confirm_password.place(x=x / 2, y=350)

        self.confirm_sign_up_button = Button(self.frame,
                                             text="Confirmar",
                                             height="2",
                                             cursor="hand2",
                                             font=("Kristen ITC", 14),
                                             width="30",
                                             command=self.get_user_info_sign_up)

        self.confirm_sign_up_button.place(x=x / 2, y=400)

        self.back_sign_up_button = Button(self.frame,
                                          text="Voltar",
                                          height="2",
                                          cursor="hand2",
                                          font=("Kristen ITC", 14),
                                          width="30",
                                          command=self.back_menu_sign_up)

        self.back_sign_up_button.place(x=x / 2, y=500)


# Tela "login" (primeira tela do jogo)
class MenuLogin(Menu):

    # Construtor
    def __init__(self, menu_sign_up,
                 menu_password_forget, menu_play, menu_settings, menu_instructions, jogar):
        super().__init__()
        self.menu_sign_up = menu_sign_up
        self.menu_password_forget = menu_password_forget
        self.menu_play = menu_play
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.jogar = jogar

    # Função para captar os dados que o usuário digitou no "login"
    def get_user_info_login(self):
        print(self.login_username_entry.get())
        print(self.login_password_entry.get())

    # Função para o usuário ir para a tela "Registrar-se"
    def go_to_sign_up(self):
        self.DevSystem.menu_sign_up.show()
        self.hide()

    # Função para o usuário ir para a tela "Esqueci minha senha"
    def go_to_password_forget(self):
        self.DevSystem.menu_password_forget.show()
        self.hide()

    # Função para limpar os caracteres inseridos no "Entry"
    def reset_entry(self):
        self.login_username_entry.delete(0, END)
        self.login_password_entry.delete(0, END)

    # Caixa de aviso para continuar sem login
    def continue_without_login(self):
        self.resposta = askyesno("Aviso Sobre Continuar Sem Cadastro",
                                 message="Ao jogar nosso jogo sem cadastro seu progresso não aparecerá no ranking")
        if self.resposta:
            self.DevSystem.menu_play.show()
            pygame.mixer.init()  # Iniciar a música do DevQuiz na tela "Menu Principal"
            pygame.mixer.music.load('Sons/musica.wav')
            pygame.mixer.music.play(-1)  # Para deixar a música tocando infinitamente
            self.hide()

    # Função para exibir uma caixinha de confirmação ao usuário, para ele decidir se realmente quer sair do DevQuiz
    def confirm(self):
        self.resposta = askyesno(message='Você tem certeza que deseja sair do DevQuiz?')
        if self.resposta:
            root.destroy()

    # Função para construir a tela "Login"
    def build_screen(self):

        Label(self.frame,
              image=bg_test,
              bg="black",
              width=1920,
              height=1080).place(x=0, y=0)

        Label(self.frame,
              image=dev_quiz_logo_pequena,
              background="white").place(x=x / 2, y=150, anchor=CENTER)

        Label(self.frame,
              image=user,
              width=280,
              height=50,
              bg="black",
              font=("Kristen ITC", 12)).place(x=x / 2, y=300, anchor=CENTER)

        self.login_username_entry = Entry(self.frame,
                                          font=("Kristen ITC", 12),
                                          bd=4,
                                          width=30)  # fleur = Arrastar janela, watch = Ampulheta

        self.login_username_entry.place(x=x / 2, y=360, anchor=CENTER)

        Button(self.frame,
               text="Logar-se",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.get_user_info_login).place(x=x / 2, y=600, anchor=CENTER)

        Button(self.frame,
               text="Registrar-se",
               command=self.go_to_sign_up,
               height="2",
               cursor="hand2",
               font=("Kristen ITC", 14),
               width="30").place(x=x / 2, y=680, anchor=CENTER)

        Label(self.frame,
              image=senha,
              width=280,
              height=50,
              bg="black",
              font=("Kristen ITC", 12)).place(x=x / 2, y=450, anchor=CENTER)

        self.login_password_entry = Entry(self.frame, show="*",
                                          font=("Kristen ITC", 12),
                                          bd=4,
                                          width=30)

        self.login_password_entry.place(x=x / 2, y=500, anchor=CENTER)

        Button(self.frame,
               text="Esqueci minha senha",
               fg="#0000EE",
               cursor="hand2",
               borderwidth=0,
               bg="white",
               command=self.go_to_password_forget,
               font=('Verdana', 9, 'italic', 'underline')).place(x=x / 2, y=530, anchor=CENTER)

        Label(self.frame,
              text="""Concordo com os Termos""",
              bg="white",
              font=("Kristen ITC", 12)).place(x=x / 2 - 42, y=800, anchor=CENTER)

        Checkbutton(self.frame,
                    fg="blue",
                    bg="white",
                    cursor="hand2", pady=3).place(x=x / 2 - 160, y=800, anchor=CENTER)

        Button(self.frame,
               text="Continuar Sem Cadastro",
               fg="#0000EE",
               cursor="hand2",
               command=self.continue_without_login,
               borderwidth=0,
               bg="white",
               font=('Verdana', 9, 'italic', 'underline')).place(x=x / 2, y=730, anchor=CENTER)

        Button(self.frame,
               font=("Kristen ITC", 14),
               text="Sair do DevQuiz",
               cursor="hand2",
               command=self.confirm).place(x=1300, y=800)


# Tela "Menu Principal" (primeira tela pós login)
class MenuPlay(Menu):

    # Construtor
    def __init__(self, menu_login, menu_settings, menu_instructions, jogar):
        super().__init__()
        self.menu_login = menu_login
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.jogar = jogar

    # Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função
    def reset_entry(self):
        pass

        # Função para exibir uma caixinha de confirmação ao usuário, para ele decidir se realmente quer sair do DevQuiz

    def confirm(self):
        self.resposta = askyesno(message='Você tem certeza que deseja sair do DevQuiz?')
        if self.resposta:
            root.destroy()

    # Função para o usuário ir para a tela "Configurações"
    def go_to_settings(self):
        self.DevSystem.menu_settings.show()
        self.hide()

    def go_to_play(self):
        self.DevSystem.jogar.show()
        self.hide()

    # Função para o usuário ir para a tela "Instruções"
    def go_to_instructions(self):
        self.DevSystem.menu_instructions.show()
        self.hide()

    # Função para construir a tela "Menu Principal"
    def build_screen(self):
        Label(self.frame, font=("Kristen ITC", 40), image=dev_quiz_logo_pequena).place(x=x / 2, y=150, anchor='center')

        Button(self.frame,
               image=jogar_img,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_play).place(x=x / 2, y=329, anchor='center')

        Button(self.frame,
               image=instrucoes,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_instructions).place(x=x / 2, y=489, anchor='center')

        Button(self.frame,
               image=configuracoes,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_settings).place(x=x / 2, y=649, anchor='center')

        Button(self.frame,
               image=sair,
               width="400",
               height="100",
               cursor="hand2",
               command=self.confirm).place(x=x / 2, y=809, anchor='center')


# Tela "Configurações"
class MenuSettings(Menu):

    # Construtor
    def __init__(self, menu_play, menu_login):
        super().__init__()
        self.menu_play = menu_play
        self.menu_login = menu_login

    # Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função
    def reset_entry(self):
        pass

        # Função para realizar o logout do usuário

    def Logout(self):
        self.resposta = askyesno(message="Você tem certeza que quer realizar logout?")
        if self.resposta:
            self.DevSystem.menu_login.show()
            self.hide()

    # Função para o usuário voltar para a tela "Menu Principal"
    def back_menu_play(self):
        self.DevSystem.menu_play.show()
        self.hide()

    # Função para mudar o tema que por padrão é "Tema Claro", para "Tema Escuro"
    def theme(self):
        self.change_theme()

    # Função para mostrar o botão do "som"
    def volume_scale(self):
        self.volume_slider = Scale(self.frame, bg="#ccccff", from_=100, to=0, orient=VERTICAL, length=150,
                                   command=self.update_sound)
        self.volume_slider.set(100)
        self.volume_slider.place(x=x / 2 + 220, y=335)  # x=900, y=335
        pygame.mixer.music.set_volume(100)

    # Função para atualizar o volume do jogo
    def update_sound(self, volume):
        self.update_volume = int(volume) / 100
        pygame.mixer.music.set_volume(self.update_volume)

    # Função para construir a tela "Configurações"
    def build_screen(self):
        Label(self.frame,
              font=("Kristen ITC", 40),
              text="Configurações").place(x=x / 2, y=100, anchor='center')

        self.theme_txt = StringVar(self.frame)
        self.theme_btn = Button(self.frame,
                                textvariable=self.theme_txt,
                                height="2",
                                font=("Kristen ITC", 14),
                                width="30",
                                cursor="hand2",
                                command=self.theme).place(x=x / 2, y=259, anchor='center')
        self.theme_txt.set("Tema Claro")

        Button(self.frame,
               text="Música",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.volume_scale).place(x=x / 2, y=419, anchor='center')
        Button(self.frame,
               text="Logout",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.Logout).place(x=x / 2, y=579, anchor='center')
        Button(self.frame,
               text="Voltar para o Menu Inicial",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.back_menu_play).place(x=x / 2, y=739, anchor='center')

    # Tela "Instruções"


class MenuInstructions(Menu):

    # Construtor
    def __init__(self, menu_play, menu_login):
        super().__init__()
        self.menu_play = menu_play
        self.menu_login = menu_login

    # Função para o usuário voltar para a tela "Menu Principal"
    def back_menu_play(self):
        # self.DevSystem.get_reference(self.menu_play_string).show()
        self.DevSystem.menu_play.show()
        self.hide()

    # Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função
    def reset_entry(self):
        pass

        # Função para construir a tela "Instruções"

    def build_screen(self):
        Label(self.frame,
              text="INSTRUÇÕES",
              font=("Kristen ITC", 40),
              bg="#E3F2F8").place(x=x / 2, y=100, anchor="center")
        Label(self.frame,
              text="""



    O DevQuiz deve ser jogado utilizando-se o máximo do seu Q.I. transcendendo a realidade.
    Quebrando todos os padrões, conceitos, regras, leis...
    Composto de 50 perguntas do mais alto nível, faça tudo com bastante atenção
    A resposta nem sempre estará nas alternativas
    Nem tudo parece ser o que é, e nem tudo é o que parece ser

    """,
              font=("Kristen ITC", 14),
              bg="#E3F2F8").place(x=x / 2, y=285, anchor="center")

        Button(self.frame,
               font=("Kristen ITC", 14),
               text="Entendo a seriedade do jogo",
               padx=25,
               pady=12.5,
               cursor="hand2",
               command=self.back_menu_play).place(x=x / 2, y=570, anchor="center")


# Tela "Jogar"
class Jogar(Menu):

    def __init__(self, menu_play, menu_login):
        super().__init__()
        self.menu_play = menu_play
        self.menu_login = menu_login

    def reset_entry(self):
        pass

    def questoes(self):
        self.perguntas = {1: "True or False", }
        self.alternativas = {1: ("1", '"1"', '"0"')}
        self.certa = {1: "1"}
        self.n = 1
        # self.questao = self.perguntas.fromkeys(self.n), self.alternativas.fromkeys(self.n), self.certa.fromkeys(self.n)
        # if self.certa.fromkeys(self.n):
        #     ...
        # else:
        #     ...

    def build_screen(self):
        self.questoes()
        Label(self.frame, text=self.perguntas[1]).place(x=x / 2, y=y / 2, anchor="center")
        Button(self.frame, text=self.alternativas[1]).place(x=x / 2, y=y / 2 + 200, anchor="center")
        # Button(self.frame, text=self.alternativas[2]).place(x=x/2+100,y=y/2+200, anchor="center")


# Classe para referenciar objetos
class DevSystem():
    # Construtor
    def __init__(self,
                 menu_login,
                 menu_password_forget,
                 menu_sign_up,
                 menu_play,
                 menu_settings,
                 menu_instructions,
                 jogar):
        self.menu_login = menu_login
        self.menu_password_forget = menu_password_forget
        self.menu_sign_up = menu_sign_up
        self.menu_play = menu_play
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.jogar = jogar

    # def __init__(self,menus):
    #     self.dictionary = {nameof(var):menu for menu in menus}
    #     print(self.dictionary)

    # Função para pegar a referência dos objetos
    def get_reference(self, reference_name):
        if reference_name == "menu_login":
            return self.menu_login
        elif reference_name == "menu_password_forget":
            return self.menu_password_forget
        elif reference_name == "menu_sign_up":
            return self.menu_sign_up
        elif reference_name == "menu_play":
            return self.menu_play
        elif reference_name == "menu_settings":
            return self.menu_settings
        elif reference_name == "menu_instructions":
            return self.menu_instructions
        elif reference_name == "jogar":
            return self.jogar
        else:
            raise Exception(f"reference_name not found, string name is wrong: {reference_name}")


# Referência Fraca dos meus objetos
menu_sign_up = MenuSignUp("menu_login")
menu_play = MenuPlay("menu_login", "menu_settings", "menu_instructions", "jogar")
menu_password_forget = MenuPasswordForget("menu_login")
menu_settings = MenuSettings("menu_play", "menu_login")
menu_instructions = MenuInstructions("menu_play", "menu_login")
jogar = Jogar("menu_login", "menu_play")
menu_login = MenuLogin("menu_sign_up",
                       "menu_password_forget",
                       "menu_play",
                       "menu_settings",
                       "menu_instructions",
                       "jogar")
menu_login.show()  # Chamo a função "show" para mostrar minha primeira tela "Login"

# Referência Forte dos meus objetos
DevSystem = DevSystem(menu_login,
                      menu_password_forget,
                      menu_sign_up,
                      menu_play,
                      menu_settings,
                      menu_instructions,
                      jogar)

menu_sign_up.Set_DevSystem(DevSystem)
menu_password_forget.Set_DevSystem(DevSystem)
menu_login.Set_DevSystem(DevSystem)
menu_play.Set_DevSystem(DevSystem)
menu_settings.Set_DevSystem(DevSystem)
menu_instructions.Set_DevSystem(DevSystem)
jogar.Set_DevSystem(DevSystem)

root.mainloop()
# mudar os nomes das variaveis e métodos