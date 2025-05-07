import spacy
from langdetect import detect
from typing import List, Dict
from app.services.llm_service import generate_flashcard

# Carrega os modelos
nlp_sentencas = spacy.load("xx_sent_ud_sm")  # modelo multilíngue para dividir sentenças
nlp_alemao = spacy.load("de_core_news_sm")    # modelo focado em alemão

def process_text(text: str) -> List[Dict[str, str]]:
    # 1. Segmentar em sentenças
    doc_sentencas = nlp_sentencas(text)
    sentencas_alemao = []

    # 2. Detectar idioma e filtrar sentenças em alemão
    for sent in doc_sentencas.sents:
        texto = sent.text.strip()
        if texto and len(texto) >= 3:
            try:
                if detect(texto) == 'de':
                    sentencas_alemao.append(texto)
            except Exception:
                pass  # Ignora falhas na detecção

    if not sentencas_alemao:
        return []

    # 3. Concatenar sentenças em alemão para um novo processamento
    texto_alemao = " ".join(sentencas_alemao)
    doc_alemao = nlp_alemao(texto_alemao)

    # 4. Extrair verbos únicos
    verbos = set()
    for token in doc_alemao:
        if token.pos_ == "VERB":
            verbo_lematizado = token.lemma_.lower()
            verbos.add(verbo_lematizado)

    if not verbos:
        return []
    
    verbosStr = ', '.join(verbos)

    # 5. Gerar flashcards básicos
    flashcards = []
    # for verbo in sorted(verbos):
        # card = {
        #     "titulo": f"Verbo: {verbo}",
        #     "descricao": f"O verbo '{verbo}' é usado em frases em alemão.",
        #     "exemplo": f"Exemplo: Ich {verbo} jeden Tag.",  # exemplo básico; a LLM depois pode melhorar
        #     "pergunta": f"O que significa o verbo '{verbo}' em alemão?"
        # }
    card = generate_flashcard(verbosStr)
    flashcards.append(card)

    return flashcards
