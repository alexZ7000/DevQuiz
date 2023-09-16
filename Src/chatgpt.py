import openai


def criar_pergunta(OPENAI_API_KEY,
                   assunto,
                   dificuldade):
    openai.api_key = OPENAI_API_KEY
    assunto = f'Elabore uma pergunta sobre {assunto}'
    dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}'
    prompt = f'{assunto}. ela deve ser do tipo Alternativa, com 4 alternativas. {dificuldade}.'
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
    )
    return resposta.choices[0].text.strip()


def responder_pergunta(OPENAI_API_KEY, pergunta):
    # deve responder a pergunta anterior com explicação
    resposta = f'Insira apenas a letra correspondente à alternativa correta, sem espaços ou caracteres adicionais para a pergunta: {pergunta}'
    gabarito = openai.Completion.create(
        engine='text-davinci-003',
        prompt=resposta,
        max_tokens=150
    )
    return gabarito.choices[0].text.strip()
