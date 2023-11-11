from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk
import re
import spacy

nltk.download('stopwords')

def lemmatize(text):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc])
    return lemmatized_text

def generate_wordcloud(text):
    text = lemmatize(text)
    words = re.findall(r'\b(?![0-9])\w+\b', text.lower())
    stop_words_nltk = set(stopwords.words('spanish'))
    custom_stopwords = ["noviembre", "méxico", "ser", "hacer", "foto"
                        , "noviembre", "viernes", "ap", "tener", "tras"
                        , "quedar", "año", "millón", "entérate", "dos"
                        , "nov", "haber", "mil", "mundo", "nuevo", "hora"
                        , "ee", "encuesta", "dejar", "video", "the", "ver"
                        , "octubre", "decir", "pedir", "uu", "miercoles", "noticia"
                        , "deportes", "buscar", "afp", "noticias", "asi"
                        , "día", "ir", "play", "miercoles", "jueves"]
    all_stop_words = stop_words_nltk.union(custom_stopwords)
    
    words = [word for word in words if word not in all_stop_words]
    word_freq = Counter(words)
    wordcloud = WordCloud(width=1600, height=800, background_color='white').generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('Práctica_10/WordCloud_NoticiasMX.png')
    plt.show()

if __name__ == "__main__":
    with open('Práctica_10/noticias.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    generate_wordcloud(text)
