from Menu import *

# IMAGENS
dev_quiz_logo = PhotoImage(file=r"Images/DevQuiz.png")
dev_quiz_logo_pequena = PhotoImage(file=r"Images/DevQuizPequeno.png")
jogar_img = PhotoImage(file=r"Images/JogarTemaClaro.png")
instrucoes = PhotoImage(file=r"Images/InstrucoesTemaClaro.png")
configuracoes = PhotoImage(file=r"Images/ConfiguraçõesTemaClaro.png")
sair = PhotoImage(file=r"Images/SairTemaClaro.png")
bg_test = PhotoImage(file=r"Images/BGTest.png")
bg_white = PhotoImage(file=r"Images/BGWhite.png")
bg_pass_fgt = PhotoImage(file=r"Images/bg_pass_fgt.png")
bg_main_screen = PhotoImage(file=r"Images/BGMainScreen.png")
senha = PhotoImage(file=r"Images/SenhaTemaEscuro.png")
user = PhotoImage(file=r"Images/UsernameTemaEscuro.png")
red_gpt = PhotoImage(file=r"Images/red_gpt.png")
# FIM DAS IMAGENS
pygame.mixer.init()


class MenuPasswordForget(Menu):
    """Tela "Esqueci minha senha" """

    def __init__(self, menu_login):
        """Construtor"""
        super().__init__()
        # Canvas(x=1920, y=1080)
        self.menu_login = menu_login

    def sumir_texto(self):
        """Função para fazer o texto de confirmação de e-mail desaparecer"""
        try:
            self.l1.place_forget()
        except:
            pass

    def send_email(self):
        """Função para enviar e-mail para o usuário"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        try:
            self.sumir_texto()
            load_dotenv()
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
            self.password = os.getenv('EMAIL_KEY')
            self.msg.add_header('Content-Type', 'text/html')
            self.msg.set_payload(self.corpo_email)

            self.s = smtplib.SMTP('smtp.gmail.com: 587')
            self.s.starttls()
            self.s.login(self.msg['From'], self.password)
            self.s.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string().encode('utf-8'))
            self.l1 = Label(bg="yellow", text="E-mail Enviado!", font=("Kristen ITC", 14))
            self.l1.place(x=x / 2 - 200, y=y / 2 - 30)
        except:
            self.sumir_texto()
            self.l1 = Label(bg="yellow", text="E-mail colocado errado, ou não cadastrado", font=("Kristen ITC", 14))
            self.l1.place(x=x / 2 - 200, y=y / 2 - 30)

    def reset_entry(self):
        """Função para limpar os caracteres inseridos no "Entry" """
        self.password_forget_entry.delete(0, END)

    def back_password_forget(self):
        """Função para o usuário voltar para a tela "Login" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.sumir_texto()
        self.dev_system.menu_login.show()
        self.hide()

    def get_user_info_password_forget(self):
        """Função para captar os dados que o usuário digitou no "Esqueci minha senha" e chamar a função "send_email" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.user_email = self.password_forget_entry.get()
        self.send_email()

    def _build_screen(self):
        """Função para construir a tela "Esqueci Minha Senha" """
        Label(self.frame,
              image=bg_pass_fgt,
              width=1920,
              height=1080).place(x=0 - 2, y=0 - 2)

        self.password_forget_entry = Entry(self.frame, font=("Kristen ITC", 12), bd=4, width=30)
        self.password_forget_entry.place(x=x / 2 - 100, y=y / 2 - 75)

        self.confirm_button = Button(self.frame,
                                     text="Confirmar",
                                     font=("Kristen ITC", 14),
                                     width=16,
                                     borderwidth=2,
                                     cursor="hand2",
                                     command=self.get_user_info_password_forget)
        self.confirm_button.place(x=x / 2 - 100, y=y / 2 + 5)

        Button(self.frame,
               cursor="hand2",
               text="Voltar",
               font=("Kristen ITC", 14),
               command=self.back_password_forget).place(x=x / 2 + 165, y=y / 2 + 5)


class MenuSignUp(Menu):
    """Tela "Registrar-se" """

    def __init__(self, menu_login):
        """Construtor"""
        super().__init__()
        self.menu_login = menu_login

    def back_menu_sign_up(self):
        """Função para o usuário voltar para a tela "Login" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.sumir_texto()
        self.dev_system.menu_login.show()
        self.hide()

    def sumir_texto(self):
        """Função para fazer o texto de confirmação de cadastro desaparecer"""
        try:
            self.l1.place_forget()
        except:
            pass

    def get_user_info_sign_up(self):
        """Função para captar os dados que o usuário digitou no "Sign up" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        try:
            self.sumir_texto()
            bd.criar_cadastro(name=self.sign_up_name.get(),
                              username=self.sign_up_username.get(),
                              email=self.sign_up_email.get(),
                              senha=self.sign_up_password.get(),
                              curso=self.click.get())
            self.l1 = Label(bg="yellow", text="Cadastro realizado com sucesso", font=("Kristen ITC", 14))
            self.l1.place(x=x / 2 - 200, y=600)
        except:
            self.sumir_texto()
            self.l1 = Label(bg="yellow",
                            text="Cadastro NÃO realizado, por favor preencha todas as lacunas de forma correta",
                            font=("Kristen ITC", 14))
            self.l1.place(x=x / 2 - 200, y=600)

    def reset_entry(self):
        """Função para limpar os caracteres inseridos no "Entry" """
        self.sign_up_name.delete(0, END)
        self.sign_up_username.delete(0, END)
        self.sign_up_email.delete(0, END)
        self.sign_up_password.delete(0, END)
        self.sign_up_confirm_password.delete(0, END)
        self.click.set("Selecione seu Curso")

    def _build_screen(self):
        """Função para construir a tela "Registrar-se" """
        Label(self.frame,
              image=bg_test,
              width=1920,
              height=1080).place(x=0 - 2, y=0 - 2)

        Label(self.frame,
              font=("Kristen ITC", 60),
              text="REGISTRE-SE",
              width=13,
              bg="#E3F2F8").place(x=x / 2 - 270, y=65)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              width=15,
              text="    Nome:    ").place(x=x / 2 - 210, y=250)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              width=15,
              text="  Username:  ").place(x=x / 2 - 210, y=300)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              width=15,
              text="    E-mail:    ").place(x=x / 2 - 210, y=350)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              width=15,
              text="    Senha:    ").place(x=x / 2 - 210, y=400)

        Label(self.frame,
              font=("Kristen ITC", 14),
              bg="light blue",
              width=15,
              text="Confirme sua Senha:").place(x=x / 2 - 210, y=450)

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
        self.select_course.place(x=x / 2 - 200, y=500)

        self.sign_up_name = Entry(self.frame,
                                  font=("Kristen ITC", 12),
                                  bd=4,
                                  width=30)

        self.sign_up_name.place(x=x / 2, y=250)

        self.sign_up_username = Entry(self.frame,
                                      font=("Kristen ITC", 12),
                                      bd=4,
                                      width=30)
        self.sign_up_username.place(x=x / 2, y=300)

        self.sign_up_email = Entry(self.frame,
                                   font=("Kristen ITC", 12),
                                   bd=4,
                                   width=30)
        self.sign_up_email.place(x=x / 2, y=350)

        self.sign_up_password = Entry(self.frame,
                                      font=("Kristen ITC", 12),
                                      bd=4,
                                      width=30,
                                      show="*")

        self.sign_up_password.place(x=x / 2, y=400)

        self.sign_up_confirm_password = Entry(self.frame,
                                              font=("Kristen ITC", 12),
                                              bd=4,
                                              width=30,
                                              show="*")

        self.sign_up_confirm_password.place(x=x / 2, y=450)

        self.confirm_sign_up_button = Button(self.frame,
                                             text="Confirmar",
                                             height="2",
                                             cursor="hand2",
                                             font=("Kristen ITC", 14),
                                             width="27",
                                             command=self.get_user_info_sign_up)

        self.confirm_sign_up_button.place(x=x / 2, y=500)

        self.back_sign_up_button = Button(self.frame,
                                          text="Voltar",
                                          height="2",
                                          cursor="hand2",
                                          font=("Kristen ITC", 14),
                                          width="27",
                                          command=self.back_menu_sign_up)

        self.back_sign_up_button.place(x=x / 2, y=600)


class MenuLogin(Menu):
    """Tela "login" (primeira tela do jogo)"""

    def __init__(self,
                 menu_password_forget,
                 menu_sign_up,
                 menu_main,
                 menu_settings,
                 menu_instructions,
                 menu_play,
                 menu_nightmare,
                 menu_nightmare_choices):
        """Construtor"""
        super().__init__()
        self.menu_sign_up = menu_sign_up
        self.menu_password_forget = menu_password_forget
        self.menu_main = menu_main
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.menu_play = menu_play
        self.menu_nightmare = menu_nightmare
        self.menu_nightmare_play = menu_nightmare_choices

    def sumir_texto(self):
        """Função para fazer o texto de confirmação de cadastro desaparecer"""
        try:
            self.l1.place_forget()
        except:
            pass

    def get_user_info_login(self):
        """Função para captar os dados que o usuário digitou no "login" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        if self.login_username_entry != "" and self.login_password_entry != "":
            if bd.login(username=self.login_username_entry.get(), senha=self.login_password_entry.get()):
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/musica.wav'), loops=-1)
                self.dev_system.menu_main.show()
                self.hide()
            else:
                self.sumir_texto()
                self.l1 = Label(bg="yellow", text="Username ou senha errada", font=("Kristen ITC", 14))
                self.l1.place(x=x / 2 - 600, y=600)

    def go_to_sign_up(self):
        """Função para o usuário ir para a tela "Registrar-se" """
        self.sumir_texto()

        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_sign_up.show()
        self.hide()

    def go_to_password_forget(self):
        """Função para o usuário ir para a tela "Esqueci minha senha" """
        self.sumir_texto()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_password_forget.show()
        self.hide()

    def reset_entry(self):
        """Função para limpar os caracteres inseridos no "Entry" """
        self.login_username_entry.delete(0, END)
        self.login_password_entry.delete(0, END)

    def continue_without_login(self):
        """Caixa de aviso para continuar sem login"""
        self.sumir_texto()
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno("Aviso Sobre Continuar Sem Cadastro",
                                 message="Ao jogar nosso jogo sem cadastro seu progresso não aparecerá no ranking")
        if self.resposta:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
            self.dev_system.menu_main.show()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/musica.wav'), loops=-1)
            self.hide()
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

    def confirm(self):
        self.sumir_texto()
        """Função para exibir uma caixinha de confirmação ao usuário,
        para ele decidir se realmente quer sair do DevQuiz"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno(message='Você tem certeza que deseja sair do DevQuiz?')
        if self.resposta:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
            root.destroy()
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

    def _build_screen(self):
        """Função para construir a tela "Login" """
        self.sumir_texto()
        Label(self.frame,
              image=bg_white,
              width=1920,
              height=1080).place(x=0 - 2, y=0 - 2)

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

        self.login_password_entry = Entry(self.frame, show="*",
                                          font=("Kristen ITC", 12),
                                          bd=4,
                                          width=30)

        self.login_password_entry.place(x=x / 2, y=490, anchor=CENTER)

        Button(self.frame,
               text="Esqueci minha senha",
               fg="#0000EE",
               cursor="hand2",
               borderwidth=0,
               bg="white",
               command=self.go_to_password_forget,
               font=('Verdana', 9, 'italic', 'underline')).place(x=x / 2, y=520, anchor=CENTER)

        Button(self.frame,
               text="Continuar Sem Cadastro",
               fg="#0000EE",
               bg="white",
               cursor="hand2",
               command=self.continue_without_login,
               borderwidth=0,
               font=('Verdana', 9, 'italic', 'underline')).place(x=x / 2, y=730, anchor=CENTER)

        Button(self.frame,
               font=("Kristen ITC", 14),
               text="Sair do DevQuiz",
               cursor="hand2",
               command=self.confirm).place(x=1300, y=800)


class MenuMain(Menu):
    """Tela "Menu Principal" (primeira tela pós login)"""

    def __init__(self, menu_login, menu_settings, menu_instructions, menu_play, menu_nightmare):
        """Construtor"""
        super().__init__()
        self.menu_login = menu_login
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.menu_play = menu_play
        self.menu_nightmare = menu_nightmare

    def reset_entry(self):
        """Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função"""
        pass

    def confirm(self):
        """Função para exibir uma caixinha de confirmação ao usuário,
        para ele decidir se realmente quer sair do DevQuiz"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno(message='Você tem certeza que deseja sair do DevQuiz?')
        if self.resposta:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
            root.destroy()
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

    def go_to_settings(self):
        """Função para o usuário ir para a tela "Configurações" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_settings.show()
        self.hide()

    def go_to_play(self):
        """Função para o usuário ir para a tela "MenuPlay" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_play.show()
        self.hide()

    def go_to_instructions(self):
        """Função para o usuário ir para a tela "Instruções" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_instructions.show()
        self.hide()

    def nightmare(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno("01001101 01000101 01000100 01001111",
                                 message='01010110 01101111 01100011 01100101 00100000 01110001 01110101 01100101 01110010 00100000 01110000 01100101 01110011 01100001 01100100 01100101 01101100 01101111 00111111 ')
        if self.resposta:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
            pygame.mixer.Channel(0).stop()
            sleep(1)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sounds/creep.wav'), loops=-1)
            self.dev_system.menu_nightmare.show()
            self.hide()
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

    def _build_screen(self):
        """Função para construir a tela "Menu Principal" """
        Label(self.frame,
              image=bg_main_screen,
              width=1920,
              height=1080).place(x=0 - 2, y=0 - 2)

        Button(self.frame,
               image=jogar_img,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_play).place(x=x / 2, y=309, anchor='center')

        Button(self.frame,
               image=instrucoes,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_instructions).place(x=x / 2, y=469, anchor='center')

        Button(self.frame,
               image=configuracoes,
               width="400",
               height="100",
               cursor="hand2",
               command=self.go_to_settings).place(x=x / 2, y=629, anchor='center')

        Button(self.frame,
               image=sair,
               width="400",
               height="100",
               cursor="hand2",
               command=self.confirm).place(x=x / 2, y=789, anchor='center')

        self.gpt = Button(self.frame,
                          width="2",
                          height="1",
                          cursor="hand2",
                          text="gpt",
                          fg="#8B0000",
                          bg="black",
                          borderwidth=0,
                          activebackground="#202020",
                          activeforeground="#8B0000",
                          command=self.nightmare)
        self.gpt.place(x=1516, y=843)


class MenuSettings(Menu):
    """Tela "Configurações" """

    def __init__(self, menu_login, menu_main):
        """Construtor"""
        super().__init__()
        self.menu_login = menu_login
        self.menu_main = menu_main

    def reset_entry(self):
        """Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função"""
        pass

        # Função para realizar o logout do usuário

    def logout(self):
        """Função para o usuário realizar logout, com uma caixinha de confimação sendo exibida"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno("Logout", message="Você tem certeza que quer realizar logout?")
        if self.resposta:
            self.dev_system.menu_login.show()
            self.hide()
        else:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

    def back_menu_main(self):
        """Função para o usuário voltar para a tela "Menu Principal" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_main.show()
        self.hide()

    def theme_function(self):
        """Função para mudar o tema que por padrão é "Tema Claro", para "Tema Escuro" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.c = self.c + 1
        if self.c % 2 == 0:
            self.theme_txt.set("Tema Claro")
            self.change_theme()
            return self.c
        else:
            self.theme_txt.set("Tema Escuro")
            self.change_theme()
            return self.c

    def invoque_slider(self):
        """Função para "invocar" os dois controladores de volume"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))

        Label(self.frame, font=("Kristen ITC", 12), bg="#ccccff", text="Música").place(x=x / 2 + 220, y=310)
        self.music_volume = Scale(self.frame, bg="#ccccff", from_=100, to=0, orient=VERTICAL, length=150,
                                  cursor="hand2",
                                  command=self.update_music)
        self.music_volume.set(100)
        self.music_volume.place(x=x / 2 + 220, y=335)

        Label(self.frame, font=("Kristen ITC", 12), bg="#ccccff", text="Som").place(x=x / 2 + 320, y=310)
        self.sound_volume = Scale(self.frame, cursor="hand2", bg="#ccccff", from_=100, to=0, orient=VERTICAL,
                                  length=150,
                                  command=self.update_sound)
        self.sound_volume.set(100)
        self.sound_volume.place(x=x / 2 + 320, y=335)

    def volume_scale(self):
        """Função para definir um valor padrão para a música"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        pygame.mixer.Channel(0).set_volume(100)
        pygame.mixer.Channel(1).set_volume(100)
        pygame.mixer.Channel(2).set_volume(100)

    def update_music(self, volume):
        """Função para atualizar o volume da música"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.music_volume = int(volume) / 100
        pygame.mixer.Channel(0).set_volume(self.music_volume)
        pygame.mixer.Channel(2).set_volume(self.music_volume)

    def update_sound(self, volume):
        """Função para atualizar o volume do som dos botões"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.sound_volume = int(volume) / 100
        pygame.mixer.Channel(1).set_volume(self.sound_volume)

    def _build_screen(self):
        """Função para construir a tela "Configurações" """
        Label(self.frame,
              font=("Kristen ITC", 40),

              text="Configurações").place(x=x / 2, y=100, anchor='center')

        self.theme_txt = StringVar()
        self.theme_btn = Button(self.frame,
                                textvariable=self.theme_txt,
                                height="2",
                                font=("Kristen ITC", 14),
                                width="30",
                                cursor="hand2",
                                command=self.theme_function)
        self.theme_btn.place(x=x / 2, y=259, anchor='center')
        self.theme_txt.set("Tema Claro")

        Button(self.frame,
               text="Música",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.invoque_slider).place(x=x / 2, y=419, anchor='center')
        Button(self.frame,
               text="Logout",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.logout).place(x=x / 2, y=579, anchor='center')
        Button(self.frame,
               text="Voltar para o Menu Inicial",
               height="2",
               font=("Kristen ITC", 14),
               width="30",
               cursor="hand2",
               command=self.back_menu_main).place(x=x / 2, y=739, anchor='center')


class MenuInstructions(Menu):
    """Tela "Instruções" """

    def __init__(self, menu_login, menu_main):
        """Construtor"""
        super().__init__()
        self.menu_login = menu_login
        self.menu_main = menu_main

    def back_menu_main(self):
        """Função para o usuário voltar para a tela "Menu Principal" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_main.show()
        self.hide()

    def reset_entry(self):
        """Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função"""
        pass

    def _build_screen(self):
        """Função para construir a tela "Instruções" """
        Label(self.frame,
              text="INSTRUÇÕES",
              font=("Kristen ITC", 40),
              bg="#ccccff").place(x=x / 2, y=100, anchor="center")
        Label(self.frame,
              text="""



    O DevQuiz deve ser jogado utilizando-se o máximo do seu Q.I. transcendendo a realidade.
    Quebrando todos os padrões, conceitos, regras, leis...
    Composto de 50 perguntas do mais alto nível, faça tudo com bastante atenção
    A resposta nem sempre estará nas alternativas
    Nem tudo parece ser o que é, e nem tudo é o que parece ser

    """,
              wraplength=1500,
              justify="center",
              font=("Kristen ITC", 14),
              bg="#ccccff").place(x=x / 2, y=285, anchor="center")

        Button(self.frame,
               font=("Kristen ITC", 14),
               text="Entendo a seriedade do jogo",
               padx=25,
               pady=12.5,
               cursor="hand2",
               command=self.back_menu_main).place(x=x / 2, y=570, anchor="center")


class MenuPlay(Menu):
    """Tela "MenuPlay" """

    def __init__(self, menu_main, menu_login):
        """Construtor"""
        super().__init__()
        self.menu_main = menu_main
        self.menu_login = menu_login

    def reset_entry(self):
        """Função reset para evitar erros no código, tendo em vista que o hide sempre chama essa função"""
        pass

    def hide2(self):
        """Função para esconder somente os widgets do "Tentar novamente" """
        super().hide()
        self.label.place_forget()
        self.button.place_forget()

    def questoes(self):
        """Função para "fabricar" minhas questões"""
        self.num_alternativas = {
            1: 2, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4, 14: 4, 15: 4, 16: 2,
            17: 4, 18: 4, 19: 4, 20: 4, 21: 4, 22: 4, 24: 4, 25: 4, 26: 4, 27: 4, 28: 2, 29: 4, 30: 4, 31: 4, 32: 4,
            33: 4, 34: 4, 35: 4, 36: 4, 37: 4, 38: 4, 39: 4, 40: 4, 41: 4, 42: 4, 43: 4, 44: 4, 45: 4, 46: 4, 47: 4,
            48: 4, 49: 4, 50: 4
        }
        return self.num_alternativas

    question = 0

    def button_creator(self):
        """Função para fabricar botões que fazem requisições ao banco de dados"""
        self.question = self.question + 1
        for self.i in range(1, self.questoes()[self.question] + 1):
            self.i = self.i
            self.alternativas = bd.pesquisa_alternativas(self.i, self.question)
            if self.i == 1:
                self.check1 = bd.pesquisa_certa(self, self.question, self.alternativas[self.i - 1][0])
                self.alternativas = str(self.alternativas[self.i - 1])
                self.b1 = Button(self.frame,
                                 font=("Kristen ITC", 14),
                                 height="2",
                                 width="30",
                                 text=self.alternativas[2:-3],
                                 padx=10,
                                 pady=5,
                                 cursor="hand2",
                                 command=lambda check=self.check1: self.change_question(check[0]))
                self.b1.place(x=x / 2 + 250, y=y / 2 - 100, anchor=CENTER)
            elif self.i == 2:
                self.check2 = bd.pesquisa_certa(self, self.question, self.alternativas[self.i - 1][0])
                self.alternativas = str(self.alternativas[self.i - 1])
                self.b2 = Button(self.frame,
                                 font=("Kristen ITC", 14),
                                 height="2",
                                 width="30",
                                 text=self.alternativas[2:-3],
                                 padx=10,
                                 pady=5,
                                 cursor="hand2",
                                 command=lambda check=self.check2: self.change_question(check[0]))
                self.b2.place(x=x / 2 - 250, y=y / 2 - 100, anchor=CENTER)
            elif self.i == 3:
                self.check3 = bd.pesquisa_certa(self, self.question, self.alternativas[self.i - 1][0])
                self.alternativas = str(self.alternativas[self.i - 1])
                self.b3 = Button(self.frame,
                                 font=("Kristen ITC", 14),
                                 height="2",
                                 width="30",
                                 text=self.alternativas[2:-3],
                                 padx=10,
                                 pady=5,
                                 cursor="hand2",
                                 command=lambda check=self.check3: self.change_question(check[0]))
                self.b3.place(x=x / 2 + 250, y=y / 2 + 100, anchor=CENTER)
            elif self.i == 4:
                self.check4 = bd.pesquisa_certa(self, self.question, self.alternativas[self.i - 1][0])
                self.alternativas = str(self.alternativas[self.i - 1])
                self.b4 = Button(self.frame,
                                 font=("Kristen ITC", 14),
                                 height="2",
                                 width="30",
                                 text=self.alternativas[2:-3],
                                 padx=10,
                                 pady=5,
                                 cursor="hand2",
                                 command=lambda check=self.check4: self.change_question(check[0]))
                self.b4.place(x=x / 2 - 250, y=y / 2 + 100, anchor=CENTER)
            elif self.i == 5:
                self.check5 = bd.pesquisa_certa(self, self.question, self.alternativas[self.i - 1][0])
                self.alternativas = str(self.alternativas[self.i - 1])
                self.b5 = Button(self.frame,
                                 font=("Kristen ITC", 14),
                                 height="2",
                                 width="30",
                                 text=self.alternativas[2:-3],
                                 padx=10,
                                 pady=5,
                                 cursor="hand2",
                                 command=lambda check=self.check5: self.change_question(check[0]))
                self.b5.place(x=x / 2, y=y / 2 + 300, anchor=CENTER)

    def rebobinar(self):
        self._build_screen()
        self.l1.place_forget()
        self.b1.place_forget()
        self.b2.place_forget()
        try:
            self.b3.place_forget()
        except:
            pass
        try:
            self.b4.place_forget()
        except:
            pass

        try:
            self.b5.place_forget()
        except:
            pass

    def alternativa_errada(self):
        """Função para mostrar que o usuário errou a questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.question = 0
        self.l1.place_forget()
        self.b1.place_forget()
        self.b2.place_forget()
        try:
            self.b3.place_forget()
        except:
            pass
        try:
            self.b4.place_forget()
        except:
            pass

        try:
            self.b5.place_forget()
        except:
            pass
        self.rebobinar()
        self.label = Label(self.frame, font=("Kristen ITC", 40), bg="#ccccff", text="Você Errou!")
        self.button = Button(self.frame, font=("Kristen ITC", 40), text="Tentar Novamente", cursor="hand2",
                             command=self.tentar_novamente)
        self.label.place(x=x / 2 - 600, y=y / 2, anchor="center")
        self.button.place(x=x / 2 + 200, y=y / 2, anchor="center")
        self.frame.pack(fill=BOTH, expand=True)

    def change_question(self, correta):
        """Função que verifica se o usuário acertou ou errou uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        if correta:
            self.hide()
            self._build_screen()
            self.dev_system.menu_play.show()
        else:
            self.alternativa_errada()

    def title_creator(self):
        """Função para gerar o enunciado da questão"""
        self.pergunta_label = str(bd.pesquisa_pergunta(self.question))
        self.l1 = Label(self.frame,
                        font=("Kristen ITC", 20),
                        text=str(f"{self.question}- {self.pergunta_label[2:-3]}")
                        )
        self.l1.place(x=x / 2, y=y / 2 - 400, anchor=CENTER)

    def show(self):
        """Função para mostrar os widgets que foram escondidos"""
        super().show()
        self.l1.place(x=x / 2, y=y / 2 - 400, anchor=CENTER)
        self.b1.place(x=x / 2 + 250, y=y / 2 - 100, anchor=CENTER)
        self.b2.place(x=x / 2 - 250, y=y / 2 - 100, anchor=CENTER)
        try:
            self.b3.place(x=x / 2 + 250, y=y / 2 + 100, anchor=CENTER)
        except:
            pass
        try:
            self.b4.place(x=x / 2 - 250, y=y / 2 + 100, anchor=CENTER)
        except:
            pass
        try:
            self.b5.place(x=x / 2, y=y / 2 + 300, anchor=CENTER)
        except:
            pass

    def tentar_novamente(self):
        """Função para levar o usuário para o "MenuMain" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.label.place_forget()
        self.button.place_forget()
        self.dev_system.menu_main.show()
        self.hide2()

    def _build_screen(self):
        """Função resposável por construir a tela"""
        Label(self.frame, image=bg_test, width=1920, height=1080).place(x=-2, y=-2)
        self.button_creator()
        self.title_creator()


class MenuNightmare(Menu):

    def __init__(self, menu_login, menu_main, menu_nightmare_choices):
        super().__init__()
        # self.menu_login = menu_login
        # self.menu_main = menu_main
        # self.menu_nightmare_play = menu_nightmare_play

    def reset_entry(self):
        """Função para limpar os caracteres inseridos no "Entry" """
        pass

    def fugir(self):
        """Função para levar o usuário para a tela "MenuMain" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.resposta = askyesno(message='Você tem certeza que deseja fugir do GPT?\n'
                                         'OBS: Caso você fuja, será perseguido ETERNAMENTE pelo GPT')
        if self.resposta:
            self.dev_system.menu_main.show()
            sleep(5)
            pygame.mixer.Channel(2).stop()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/musica.wav'), loops=-1)
            self.hide()

    def go_to_nightmare_choices(self):
        """Função que leva o usuário a tela "MenuNightmareChoices" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        showwarning(
            "01010110 01000011 00100000 01001110 00100000 01010110 01000001 01001001 00100000 01000011 01001111 01001110 01010011 01000101 01000111 01010101 01001001 01010010",
            message='O GPT só aprova aqueles que acertarem  no mínimo 7 questões')
        self.dev_system.menu_nightmare_choices.show()
        self.hide()

    def _build_screen(self):
        """Função que constrói minha tela"""
        self.frame.config(bg="black")
        Label(self.frame, image=red_gpt, bg="black", width=530, height=530).place(x=x / 2 - 580, y=y / 2 - 275,
                                                                                  anchor="center")
        Label(self.frame, image=red_gpt, bg="black", width=530, height=530).place(x=x / 2 + 680, y=y / 2 + 175,
                                                                                  anchor="center")

        Label(self.frame,
              font=("Kristen ITC", 60),
              text="NIGHTMARE",
              fg="#8B0000",
              bg="black").place(x=x / 2, y=y / 2 - 380, anchor="center")

        Button(self.frame,
               font=("Kristen ITC", 40),
               text="EU DESAFIO O GPT",
               fg="#8B0000",
               activebackground="#202020",
               activeforeground="#8B0000",
               width=23,
               cursor="hand2",
               command=self.go_to_nightmare_choices,
               borderwidth=5,
               bg="black").place(x=x / 2, y=y / 2, anchor="center")

        Button(self.frame,
               font=("Kristen ITC", 40),
               text="EU TENHO MEDO DO GPT",
               fg="#8B0000",
               bg="black",
               highlightbackground="blue",
               activebackground="#202020",
               activeforeground="#8B0000",
               borderwidth=5,
               cursor="hand2",
               command=self.fugir).place(x=x / 2, y=y / 2 + 200, anchor="center")


class MenuNightmareChoices(Menu):

    def __init__(self, menu_login, menu_main, menu_nightmare, menu_nightmare_play):
        super().__init__()

        self.menu_login = menu_login
        self.menu_main = menu_main
        self.menu_nightmare = menu_nightmare
        self.menu_nightmare_play = menu_nightmare_play

    def reset_entry(self):
        """Função para limpar os caracteres inseridos no "Entry" """
        pass

    def back_menu_nightmare_choices(self):
        """Função para sair da tela "MenuNightmareChoices" """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.dev_system.menu_nightmare.show()
        self.hide()

    def acertos_user(self):
        """Função para contar a quantidade de acertos do usuário"""
        self.acertos = self.acertos
        self.resposta_gpt = self.resposta_gpt.lower()
        self.resposta_gpt = self.resposta_gpt[0]
        self.resposta_var = self.resposta_var_ruim.get().lower()
        if self.resposta_var == self.resposta_gpt:
            self.acertos = self.acertos + 1
            showinfo("01000001 01000011 01000101 01010010 01010100 01001111 01010101",
                     message=f"Você acertou esta questão. Você está com {self.acertos} acertos de 10 questões")
            self.resposta_var_ruim.set("")
            return self.acertos
        else:
            self.acertos = self.acertos
            showerror("01000101 01010010 01010010 01001111 01010101",
                      message=f"Você errou esta questão. Você está com {self.acertos} acertos de 10 questões")
            self.resposta_var_ruim.set("")
            return self.acertos

    def final(self):
        """Função que mostra ao usuário se o GPT o aprovou"""
        self.acertos_user()
        showinfo("01000001 01010000 01010010 01001111 01010110 01000001 01000100 01001111 00001010",
                 message=f"Você está com {self.acertos} acertos de 10 questões")
        if self.acertos > 6:
            showinfo("01000001 01010000 01010010 01001111 01010110 01000001 01000100 01001111",
                     message=f"Você está com {self.acertos} acertos de 10 questões")
            self.dev_system.menu_main.show()
            pygame.mixer.Channel(2).stop()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/musica.wav'), loops=-1)
            self.hide()
        else:
            c = 0
            while c != 11:
                showerror("01010010 01000101 01010000 01010010 01001111 01010110 01000001 01000100 01001111",
                          message="Você foi REPROVADO pelo gpt", )
                c = c + 1
            sleep(2)
            root.destroy()

    def questao10(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 10
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.final,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao9(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 9
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao10,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao8(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 8
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao9,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao7(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 7
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao8,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao6(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 6
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao7,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao5(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 5

        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao6,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao4(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 4
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()

        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao5,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao3(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 3

        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()
        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao4,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao2(self):
        """Função para fazer uma questão"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.acertos_user()
        self.l8.place_forget()
        self.r8.place_forget()
        self.r9.place_forget()
        self.r10.place_forget()
        self.r11.place_forget()
        self.b3.place_forget()

        self.resposta_var_ruim.set("")
        self.questao = 2
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()
        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
        self.resposta_gpt_longa = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
        self.resposta_gpt = str(self.resposta_gpt_longa[0])

        self.l8 = Label(self.frame,
                        text=f"""{str(self.questao)}- {self.texto_gpt}""",
                        font=("Kristen ITC", 26),
                        wraplength=1500,
                        justify="center",
                        fg="#8B0000",
                        bg="black")
        self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

        # 4 radiobuttons para o jogador assinalar entre a,b,c,d
        self.resposta_var_ruim = StringVar()
        self.r8 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="A",
                              value="a",
                              variable=self.resposta_var_ruim
                              )
        self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

        self.r9 = Radiobutton(self.frame,
                              font=("Kristen ITC", 30),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="B",
                              value="b",
                              variable=self.resposta_var_ruim
                              )
        self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

        self.r10 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="C",
                               value="c",
                               variable=self.resposta_var_ruim
                               )
        self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

        self.r11 = Radiobutton(self.frame,
                               font=("Kristen ITC", 30),
                               fg="#8B0000",
                               bg="black",
                               activebackground="#202020",
                               activeforeground="#8B0000",
                               cursor="hand2",
                               text="D",
                               value="d",
                               variable=self.resposta_var_ruim
                               )
        self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

        # função para verificar se a resposta esta certa

        self.b3 = Button(self.frame,
                         text="Verificar Resposta",
                         command=self.questao3,
                         font=("Kristen ITC", 14),
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def questao1(self):
        """Função para fazer uma questão e verificar se o usuário respondeu ao radiobutton"""
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/click.wav'))
        self.assunto = self.assunto_var.get()
        self.dificuldade = self.dificuldade_var.get()
        if self.assunto != "" and self.dificuldade != "":
            self.l1.place_forget()
            self.l2.place_forget()
            self.l3.place_forget()
            self.l4.place_forget()

            self.r1.place_forget()
            self.r2.place_forget()
            self.r3.place_forget()
            self.r4.place_forget()
            self.r5.place_forget()
            self.r6.place_forget()
            self.r7.place_forget()

            self.b1.place_forget()
            self.b2.place_forget()

            self.questao = 1

            load_dotenv()
            OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
            self.texto_gpt = criar_pergunta(OPENAI_API_KEY, self.assunto, self.dificuldade)
            self.resposta_gpt = str(responder_pergunta(OPENAI_API_KEY, self.texto_gpt))
            # self.resposta_gpt = str(self.resposta_gpt_longa[0])

            self.l8 = Label(self.frame,
                            text=f"""{str(self.questao)}- {self.texto_gpt}""",
                            font=("Kristen ITC", 26),
                            wraplength=1500,
                            justify="center",
                            fg="#8B0000",
                            bg="black")
            self.l8.place(x=x / 2, y=y / 2 - 300, anchor=CENTER)

            # 4 radiobuttons para o jogador assinalar entre a,b,c,d
            self.resposta_var_ruim = StringVar()
            self.r8 = Radiobutton(self.frame,
                                  font=("Kristen ITC", 30),
                                  fg="#8B0000",
                                  bg="black",
                                  activebackground="#202020",
                                  activeforeground="#8B0000",
                                  cursor="hand2",
                                  text="A",
                                  value="a",
                                  variable=self.resposta_var_ruim
                                  )
            self.r8.place(x=x / 2 - 150, y=y / 2 + 100)

            self.r9 = Radiobutton(self.frame,
                                  font=("Kristen ITC", 30),
                                  fg="#8B0000",
                                  bg="black",
                                  activebackground="#202020",
                                  activeforeground="#8B0000",
                                  cursor="hand2",
                                  text="B",
                                  value="b",
                                  variable=self.resposta_var_ruim
                                  )
            self.r9.place(x=x / 2 - 50, y=y / 2 + 100)

            self.r10 = Radiobutton(self.frame,
                                   font=("Kristen ITC", 30),
                                   fg="#8B0000",
                                   bg="black",
                                   activebackground="#202020",
                                   activeforeground="#8B0000",
                                   cursor="hand2",
                                   text="C",
                                   value="c",
                                   variable=self.resposta_var_ruim
                                   )
            self.r10.place(x=x / 2 + 50, y=y / 2 + 100)

            self.r11 = Radiobutton(self.frame,
                                   font=("Kristen ITC", 30),
                                   fg="#8B0000",
                                   bg="black",
                                   activebackground="#202020",
                                   activeforeground="#8B0000",
                                   cursor="hand2",
                                   text="D",
                                   value="d",
                                   variable=self.resposta_var_ruim
                                   )
            self.r11.place(x=x / 2 + 150, y=y / 2 + 100)

            # função para verificar se a resposta esta certa

            self.b3 = Button(self.frame,
                             text="Verificar Resposta",
                             command=self.questao2,
                             font=("Kristen ITC", 14),
                             fg="#8B0000",
                             activebackground="#202020",
                             activeforeground="#8B0000",
                             width=23,
                             cursor="hand2",
                             padx=80,
                             borderwidth=5,
                             bg="black")
            self.b3.place(x=x / 2 - 200, y=y / 2 + 375)

    def _build_screen(self):
        """Função que constrói a tela"""
        self.frame.config(bg="black")
        self.acertos = 0
        self.l1 = Label(self.frame, image=red_gpt, bg="black", width=530, height=530)
        self.l1.place(x=x / 2 - 580, y=y / 2, anchor="center")

        self.l2 = Label(self.frame,
                        font=("Kristen ITC", 50),
                        text="01000101 01010011 01000011 01001111 01001100 01001000 01000001",
                        fg="#8B0000",
                        bg="black")
        self.l2.place(x=x / 2, y=y / 2 - 375, anchor="center")

        self.l3 = Label(self.frame,
                        font=("Kristen ITC", 50),
                        fg="#8B0000",
                        bg="black",
                        text="Assunto")
        self.l3.place(x=x / 2 - 150, y=y / 2 - 150)

        self.assunto_var = StringVar()
        self.r1 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Java",
                              value="Java",
                              variable=self.assunto_var)
        self.r1.place(x=x / 2 - 150, y=y / 2 - 50)

        self.r2 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Python",
                              value="Python",
                              variable=self.assunto_var)
        self.r2.place(x=x / 2 - 150, y=y / 2)

        self.r3 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Modelagem Orientada a Objetos",
                              value="Modelagem Orientada a Objetos",
                              variable=self.assunto_var)
        self.r3.place(x=x / 2 - 150, y=y / 2 + 50)

        self.r4 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Banco de Dados Relacionais",
                              value="Banco de Dados Relacionais",
                              variable=self.assunto_var)
        self.r4.place(x=x / 2 - 150, y=y / 2 + 100)

        self.l4 = Label(self.frame,
                        font=("Kristen ITC", 50),
                        fg="#8B0000",
                        bg="black",
                        text="Dificuldade")
        self.l4.place(x=x / 2 + 250, y=y / 2 - 150)

        self.dificuldade_var = StringVar()
        self.r5 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Fácil",
                              value="Fácil",
                              variable=self.dificuldade_var)
        self.r5.place(x=x / 2 + 250, y=y / 2 - 50)

        self.r6 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              cursor="hand2",
                              text="Médio",
                              value="Médio",
                              variable=self.dificuldade_var)
        self.r6.place(x=x / 2 + 250, y=y / 2)

        self.r7 = Radiobutton(self.frame,
                              font=("Kristen ITC", 14),
                              fg="#8B0000",
                              bg="black",
                              cursor="hand2",
                              activebackground="#202020",
                              activeforeground="#8B0000",
                              text="Difícil",
                              value="Difícil",
                              variable=self.dificuldade_var)
        self.r7.place(x=x / 2 + 250, y=y / 2 + 50)

        self.b1 = Button(self.frame,
                         font=("Kristen ITC", 14),
                         text="ESTOU PRONTO PARA VENCER O GPT",
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         command=self.questao1,
                         cursor="hand2",
                         padx=80,
                         borderwidth=5,
                         bg="black")
        self.b1.place(x=x / 2, y=y / 2 + 250, anchor="center")

        self.b2 = Button(self.frame,
                         font=("Kristen ITC", 14),
                         text="EU QUERO MINHA MAMÃE",
                         fg="#8B0000",
                         activebackground="#202020",
                         activeforeground="#8B0000",
                         width=23,
                         cursor="hand2",
                         padx=80,
                         command=self.back_menu_nightmare_choices,
                         borderwidth=5,
                         bg="black")
        self.b2.place(x=x / 2, y=y / 2 + 350)


class DevSystem:
    """Classe para referenciar objetos"""

    def __init__(self,
                 menu_login,
                 menu_password_forget,
                 menu_sign_up,
                 menu_main,
                 menu_settings,
                 menu_instructions,
                 menu_play,
                 menu_nightmare,
                 menu_nightmare_choices):
        """Construtor"""
        self.menu_login = menu_login
        self.menu_password_forget = menu_password_forget
        self.menu_sign_up = menu_sign_up
        self.menu_main = menu_main
        self.menu_settings = menu_settings
        self.menu_instructions = menu_instructions
        self.menu_play = menu_play
        self.menu_nightmare = menu_nightmare
        self.menu_nightmare_choices = menu_nightmare_choices

    # def __init__(self,menus):
    #     self.dictionary = {nameof(var):menu for menu in menus}
    #     print(self.dictionary)

    def get_reference(self, reference_name):
        """Função para pegar a referência dos objetos"""
        if reference_name == "menu_login":
            return self.menu_login
        elif reference_name == "menu_password_forget":
            return self.menu_password_forget
        elif reference_name == "menu_sign_up":
            return self.menu_sign_up
        elif reference_name == "menu_main":
            return self.menu_main
        elif reference_name == "menu_settings":
            return self.menu_settings
        elif reference_name == "menu_instructions":
            return self.menu_instructions
        elif reference_name == "menu_play":
            return self.menu_play
        elif reference_name == "menu_nightmare":
            return self.menu_nightmare
        elif reference_name == "menu_nightmare_choices":
            return self.menu_nightmare_choices
        else:
            raise Exception(f"reference_name not found, string name is wrong: {reference_name}")


# Referência Fraca dos meus objetos
menu_sign_up = MenuSignUp("menu_login")
menu_main = MenuMain("menu_login", "menu_settings", "menu_instructions", "menu_play", "menu_nightmare")
menu_password_forget = MenuPasswordForget("menu_login")
menu_settings = MenuSettings("menu_login", "menu_main")
menu_instructions = MenuInstructions("menu_login", "menu_main")
menu_play = MenuPlay("menu_login", "menu_main")
menu_nightmare = MenuNightmare("menu_login", "menu_main", "menu_nightmare_choices")
menu_nightmare_choices = MenuNightmareChoices("menu_login", "menu_main", "menu_nightmare", "menu_nightmare_play")
menu_login = MenuLogin("menu_password_forget",
                       "menu_sign_up",
                       "menu_main",
                       "menu_settings",
                       "menu_instructions",
                       "menu_play",
                       "menu_nightmare",
                       "menu_nightmare_choices")
menu_login.show()  # Chamo a função "show" para mostrar minha primeira tela "Login"

# Referência Forte dos meus objetos
DevSystem = DevSystem(menu_login,
                      menu_password_forget,
                      menu_sign_up,
                      menu_main,
                      menu_settings,
                      menu_instructions,
                      menu_play,
                      menu_nightmare,
                      menu_nightmare_choices)

menu_sign_up.set_dev_system(DevSystem)
menu_password_forget.set_dev_system(DevSystem)
menu_login.set_dev_system(DevSystem)
menu_main.set_dev_system(DevSystem)
menu_settings.set_dev_system(DevSystem)
menu_instructions.set_dev_system(DevSystem)
menu_play.set_dev_system(DevSystem)
menu_nightmare.set_dev_system(DevSystem)
menu_nightmare_choices.set_dev_system(DevSystem)

root.mainloop()
# mudar os nomes das variaveis e métodos
