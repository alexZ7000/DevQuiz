import psycopg
import datetime

con = psycopg.connect(user='peepw', password='Jmtjh3pyqnI8',
                              host='ep-little-bird-447006.us-east-2.aws.neon.tech', dbname='devquiz')

# conexao com o postgresql
def conectar():
    try:
        return con
    except ValueError as erro:
        con.close()


# criação de cadastro
def criar_cadastro(name, username, email, senha, curso):
    cursor = con.cursor()
    cursor.execute(
        f"INSERT INTO cadastro (name, username, senha, email, curso) VALUES ('{name}', '{username}', '{senha}', '{email}', '{curso}')"
    )
    con.commit()



# criação de usuario
def criar_usuario(username, senha):
    cursor = con.cursor()
    cursor.execute("SELECT username, senha FROM cadastrar WHERE username = %s AND senha = %s", (username, senha))
    

# pegar o tempo do computador do usuario e subtrair pelo tempo que foi finalziado o jogo (ate a ultima questao),
# mandar resposta desse calculo para o banco de dados
def cronometrar(name, tempo_comeco):
    cursor = con.cursor()
    tempo_total = 10
    tempo_comeco = 0
    cursor.execute("SELECT pontos FROM usuario WHERE name = %s", name)
    tempo_no_db = cursor.fetchone()[0]
    if tempo_no_db > tempo_total:
        cursor.execute("UPDATE usuario SET pontos = %s WHERE name = %s", (tempo_total, name))
        con.commit()


def pesquisa_pergunta(question):
    cursor = con.cursor()
    question = cursor.execute(f"SELECT perguntas FROM questoes WHERE idquestao = {question}")
    con.commit()
    question = cursor.fetchone()
    
    return question


def pesquisa_alternativas(a, b):
    cursor = con.cursor()
    a = cursor.execute(f"SELECT alternativa FROM respostas WHERE idquestao = {b}")
    con.commit()
    a = cursor.fetchall()
    
    return a


def pesquisa_certa(self, a, b):
    cursor = con.cursor()
    self.correta = cursor.execute(
        "SELECT correta FROM respostas WHERE idquestao = {} AND alternativa = '{}'".format(a, b))
    con.commit()
    a = cursor.fetchone()
    
    return a


# ranking
ranking = []


def rank():
    cursor = con.cursor()
    cursor.execute("SELECT name, tempo FROM ranking ORDER BY tempo DESC")
    con.commit()
    ranking_result = cursor.fetchall()
    
    return ranking_result


# verificação de usuario
def verificar(username):
    cursor = con.cursor
    resposta = cursor.execute(f"SELECT * FROM CADASTRO WHERE USERNAME == {username}")
    con.commit()
    


# alteração de senha
def mudar_senha(username):
    cursor = con.cursor()
    cursor.execute("SELECT username FROM cadastro WHERE username = %s", username)
    if cursor.fetchone() is not None:
        senha = input("Digite a nova senha: ")
        cursor.execute("UPDATE cadastro SET senha = %s WHERE username = %s", (senha, username))
        con.commit()
    


# login
def login(name, senha):
    cursor = con.cursor()
    cursor.execute("SELECT name, senha FROM usuario WHERE name = %s AND senha = %s", (name, senha))
    


# atribuição de valor de dados de usuario
class Usuario:
    def __init__(self, username, senha, email, name, curso):
        self.__username = username
        self.__senha = senha
        self.__email = email
        self.__name = name
        self.__curso = curso
