import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt_tab')

class TextCleaner:
    @staticmethod
    def clearing_the_data(data):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = data.translate(translator)
        data = clean_text.lower()
        return data
    
    @staticmethod
    def remove_stop_words(data):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(data)
        filtered = []
        for word in tokens:
            if word not in stop_words:
                filtered.append(word)
        cleaned_data = " ".join(filtered)
        return cleaned_data