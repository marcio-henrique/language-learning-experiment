from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Configure sua chave de API
client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)


def generate_flashcard(texto: str) -> dict:
#prompt 1
#     prompt = f"""
# Você é um assistente para criação de flashcards de aprendizado de alemão para iniciantes. Você produzirá um flashcard para cada verbo em alemão que te enviar.

# Cada flashcard seguirá o formato:
# - Título do flashcard: [Título curto]
# - Descrição: [Descrição explicando o verbo]
# - Frase de exemplo em alemão: [Frase]
# - Tradução da frase: [Tradução]
# - Pergunta de múltipla escolha (em português) e 5 opções, indicando a correta.

# Você irá criar os flashcards a partir dos verbos: \"{texto}\"
# """

    prompt = f"""
        Você é um assistente de ensino de aprendizado de alemão para iniciantes. Para cada verbo abaixo, você deverá criar 2 questões de múltipla escolha (em português), com 5 alternativas, incluindo a alternativa correta.
        Verbos: \"{texto}\"
    """

    # Nova forma de chamar a API para usar o modelo GPT
    response = client.responses.create(
        model="gpt-4.1",
        instructions="Você é um assistente de ensino de aprendizado de alemão para iniciantes.",
        input=prompt
        # max_tokens=400 #TODO só colocar se precisar. Se ajudar na experiência, deixar (bolso vai chorar, mas é temporário)
    )

    conteudo = response.choices[0].message.content

    return {"conteudo": conteudo}
