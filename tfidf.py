from nltk import FreqDist
import math
import sys
import pandas as pd
from importlib import reload
from nltk import FreqDist
sys.path.append("/Users/ajit/projects/dit_coder_bout_2020")
import tokenizer as tk
import tokenizefiles as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import filetotxt as ft
import tokenizer as ts

df = pd.read_csv("/Users/ajit/projects/dit_coder_bout_2020/tokens.csv")

n_docs = len(df.doc.unique())

def computeidf(row):
	word = row['token']
	n_docs_word = len(df[df['token']==word])
	if n_docs_word == 0: return 0
	return n_docs/n_docs_word

df['idf'] = df.apply(computeidf, axis = 1)
df['tf_idf'] = df['tf'] * df['idf']

df[pd.isnull(df).any(axis=1)]
x = df.pivot(index='doc', columns='token', values='tf_idf')
x.fillna(0, inplace=True)
x.shape
x

query = ["datastage"]

q = pd.DataFrame(data=0, columns=x.columns, index=["query"])
# q.at['query', "watch"] = 1
q.at['query', "movie"] = 1
q

cosine_similarity(x, q)

#---------------------------------------------
# *** Using TfidfVectorizer from sklearn ***
#---------------------------------------------

tfidf_vectorizer = TfidfVectorizer(use_idf=True)

keys = 'house'
tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
query_matrix = tfidf_vectorizer.transform([keys])
cs = cosine_similarity(query_matrix, tfidf_matrix)
cs

type(tfidf_matrix)

x = pd.DataFrame(tfidf_matrix.toarray(), columns = tfidf_vectorizer.get_feature_names(), index = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5'])
y = pd.DataFrame(query_matrix.toarray(), columns = tfidf_vectorizer.get_feature_names(), index = ['query'])

y
cs1 = cosine_similarity(x, y)
type(cs1)

def sum(a,b):
	yield a+b

x=sum(1,2)
x

from nltk.corpus import wordnet
from itertools import chain

word = 'house'

def getsynonyms(word):
	synonyms1 = [name for synonym in wordnet.synsets(word) for syn in synonym.hypernyms() for name in syn.lemma_names()]
	synonyms2 = [name for synonym in wordnet.synsets(word) for name in synonym.lemma_names()]
	return set(synonyms1 + synonyms2)

getsynonyms(word)
