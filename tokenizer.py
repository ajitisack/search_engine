import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# nltk.data.path.append('H:\\Python\\nltk_data')

LANG = 'english'

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer(LANG)
wn_lemmatizer = WordNetLemmatizer()


stop_words = set( list({''})
                 + list(stopwords.words('english')) 
                 + list(string.ascii_lowercase) 
                 + ['1','2','3','4','5','6','7','8','9','0'])


def between(n, x, y):
    """ Checks whether a number(n) is b/w 2 numbers(x & y) """
    return 1 if n >= x and n <= y else 0


def replace_NonAlphaNum_WithSpace(str):
    """ Replaces non alphanum characters with space """
    return ''.join(i if between(ord(i), 48, 57) or between(ord(i), 97, 122) else " " for i in str)


def normalize(word, method="lemmatize"):
    """ Normalizes the string/word using either stemming or lemmitization technique """
    lemmatizer = lambda word, type : wn_lemmatizer.lemmatize(word, pos=type)
    normalizer = {
          'lemmatize' : lambda word: lemmatizer(lemmatizer(lemmatizer(word, 'n'), 'v'), 'a')
        , 'snowballstem' : lambda word : snowball.stem(word)
        , 'porterstem' : lambda word : porter.stem(word)
        , 'lancasterstem' : lambda word : lancaster.stem(word)
        }
    return normalizer[method](word)


def tokenizer(str):
    """ Tokenize a string into normalized words"""
    str = replace_NonAlphaNum_WithSpace(str.lower())
    words = [normalize(word) for word in word_tokenize(str) if word not in stop_words]
    return(words)
