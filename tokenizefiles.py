import os
import sys
import subprocess
import logging
import pandas as pd
import filetotxt as ft
import tokenizer as ts
from nltk import FreqDist


extensions = ('.txt', '.pdf', '.docx', '.pptx')


def tokenize_file(filename: str):
	""" Tokenize words in a file """
	line = ft.read_file(filename)
	words = ts.tokenizer(line)
	df = pd.DataFrame(FreqDist(words).items(), columns =['token', 'freq'])
	df = df.dropna()
	df['doc'] = filename
	df['n_words'] = len(words)
	df['tf'] = df['freq'] / df['n_words']
	print(f"Tokenized - {filename}")
	return df


def tokenize_filesindir(path):
    """ Tokenize each file with given extenion in given directory into normalized words"""
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(extensions)]
    list_dfs = [tokenize_file(file) for file in files]
    df = pd.concat(list_dfs, ignore_index=True)
    return df

# tokenizefiles("H:\\Python\\SearchEngine\\docs")

def main():
	df = tokenize_filesindir(sys.argv[1])
	print(f"Token shape - {df.shape}")
	df.to_csv("tokens.csv", index=False)


if __name__ == '__main__':
    main()