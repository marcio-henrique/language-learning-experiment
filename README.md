# Geração de flashcards para fixação de conteúdo a partir de textos de ensino de alemão

## Instalação de Dependências
`
    pip install -r requirements.txt 
    python3 -m spacy download xx_sent_ud_sm
    python3 -m spacy download de_core_news_sm
`
    <!-- pip install python-multipart -->


## Rodar o servidor
`
    uvicorn app.main:app --reload
`
