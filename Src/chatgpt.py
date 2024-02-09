from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def criar_pergunta(OPENAI_API_KEY,
                   assunto,
                   dificuldade):
    assunto = f'Elabore uma pergunta sobre {assunto}'
    dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}'
    prompt = f'{assunto}. ela deve ser do tipo Alternativa, com 4 alternativas. {dificuldade}.'
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def responder_pergunta(OPENAI_API_KEY, pergunta):
    # deve responder a pergunta anterior com explicação
    resposta = f'Insira apenas a letra correspondente à alternativa correta, sem espaços ou caracteres adicionais para a pergunta: {pergunta}'
    gabarito = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=resposta,
        max_tokens=150
    )
    return gabarito.choices[0].text.strip()
