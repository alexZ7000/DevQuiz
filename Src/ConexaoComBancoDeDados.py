import psycopg
import datetime


# conexao com o postgresql
def conectar():
    try:
        con = psycopg.connect(user='peepw', password='Jmtjh3pyqnI8',
                              host='ep-little-bird-447006.us-east-2.aws.neon.tech', dbname='devquiz')
        print("Conectado ao banco de dados")
        return con
    except ValueError as erro:
        print("Erro de Conexão")
    con.close()


# criação de cadastro
def criar_cadastro(name, username, email, senha, curso):
    con = psycopg.connect(user='peepw', password='Jmtjh3pyqnI8', host='ep-little-bird-447006.us-east-2.aws.neon.tech',
                          dbname='devquiz')
    cursor = con.cursor()
    cursor.execute(
        f"INSERT INTO cadastro (name, username, senha, email, curso) VALUES ('{name}', '{username}', '{senha}', '{email}', '{curso}')"
    )
    print("Usuário cadastrado com sucesso")
    con.commit()
    con.close()


# criação de usuario
def criar_usuario(username, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT username, senha FROM cadastrar WHERE username = %s AND senha = %s", (username, senha))
    if cursor.fetchone() is not None:
        print("Login realizado com sucesso")
    else:
        print("Login não realizado")
    con.close()


# pegar o tempo do computador do usuario e subtrair pelo tempo que foi finalziado o jogo (ate a ultima questao),
# mandar resposta desse calculo para o banco de dados
def cronometrar(name, tempo_comeco):
    con = conectar()
    cursor = con.cursor()
    tempo_total = 10
    tempo_comeco = 0
    cursor.execute("SELECT pontos FROM usuario WHERE name = %s", name)
    tempo_no_db = cursor.fetchone()[0]
    if tempo_no_db > tempo_total:
        cursor.execute("UPDATE usuario SET pontos = %s WHERE name = %s", (tempo_total, name))
        con.commit()
        print("Pontuação atualizada")
    else:
        print("Pontuação não atualizada")


def pesquisa_pergunta(question):
    jon = conectar()
    jursor = jon.cursor()
    question = jursor.execute(f"SELECT perguntas FROM questoes WHERE idquestao = {question}")
    jon.commit()
    question = jursor.fetchone()
    jon.close()
    return question


def pesquisa_alternativas(a, b):
    von = conectar()
    vursor = von.cursor()
    a = vursor.execute(f"SELECT alternativa FROM respostas WHERE idquestao = {b}")
    von.commit()
    a = vursor.fetchall()
    von.close()
    return a


def pesquisa_certa(self, a, b):
    bon = conectar()
    bursor = bon.cursor()
    self.correta = bursor.execute(
        "SELECT correta FROM respostas WHERE idquestao = {} AND alternativa = '{}'".format(a, b))
    bon.commit()
    a = bursor.fetchone()
    bon.close()
    return a


# ranking
ranking = []


def rank():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT name, tempo FROM ranking ORDER BY tempo DESC")
    con.commit()
    ranking_result = cursor.fetchall()
    con.close()
    print(ranking_result)
    return ranking_result


# verificação de usuario
def verificar(username):
    con = conectar()
    cursor = con.cursor
    resposta = cursor.execute(f"SELECT * FROM CADASTRO WHERE USERNAME == {username}")
    con.commit()
    if resposta is not None:
        print("Existe")
    con.close()


# alteração de senha
def mudar_senha(username):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT username FROM cadastro WHERE username = %s", username)
    if cursor.fetchone() is not None:
        senha = input("Digite a nova senha: ")
        cursor.execute("UPDATE cadastro SET senha = %s WHERE username = %s", (senha, username))
        con.commit()
        print("Senha alterada com sucesso")
    else:
        print("Usuário não encontrado")
    con.close()


# login
def login(name, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT name, senha FROM usuario WHERE name = %s AND senha = %s", (name, senha))
    if cursor.fetchone() is not None:
        print("Login realizado com sucesso")
    else:
        print("Login não realizado")
    con.close()


# atribuição de valor de dados de usuario
class Usuario:
    def __init__(self, username, senha, email, name, curso):
        self.__username = username
        self.__senha = senha
        self.__email = email
        self.__name = name
        self.__curso = curso
