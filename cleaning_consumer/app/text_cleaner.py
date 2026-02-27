import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def download_nltk_data():
    nltk.download('stopwords')
    nltk.download('punkt_tab')

download_nltk_data()

class TextCleaner:
    @staticmethod
    def clearing_the_data(data):
        text = data['text']
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        data['text'] = clean_text.lower()
        return data
    
    @staticmethod
    def remove_stop_words(data):
        text = data['text']
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        filtered = []
        for word in tokens:
            if word not in stop_words:
                filtered.append(word)
        cleaned_text = " ".join(filtered)
        data['text'] = cleaned_text
        return data