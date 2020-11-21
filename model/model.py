import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas as pd
import re

from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import os

STOPWORDS = None
word2vec = None
threshhold = None


def initialize_model(modeltype, custom=None):
    STOPWORDS = stopwords.words('english')
    glovepath = os.path.abspath(os.getcwd())
    glovepath += "/model/glove.6B.100d.txt"
    glove_file = datapath(glovepath)
    word2vec_glove_file = get_tmpfile("glove.6B.100d.word2vec.txt")
    glove2word2vec(glove_file, word2vec_glove_file)
    word2vec = KeyedVectors.load_word2vec_format(word2vec_glove_file)
    if modeltype == "accuracy":
        threshhold = 2.4572000000008547
    elif modeltype == "f_score":
        threshhold = 5.920599999999634
    else:
        threshhold = custom


def getdata(filepath):
    if os.path.isfile(filepath) == False:
        print("File does not exist!")
        return None
    reader = open(filepath, "r")
    data = reader.read()
    return data


def gettokens(data):
    trimmedwords = word_tokenize(data)
    words = [re.sub(r'[^\w\s]', ' ', word) for word in trimmedwords]
    ans = [y for x in words for y in word_tokenize(x)]
    valid_token = []
    for i in range(len(ans)):
        ans[i] = ans[i].lower()
        if ans[i] in word2vec.vocab:
            valid_token.append(ans[i])
        else:
            print("Throwing " + ans[i] + " from the file")
    return valid_token


def getmeanvector(tokens):
    freq = {}
    for token in tokens:
        if token in freq.keys():
            freq[token] += 1
        else:
            freq[token] = 1
    a = 0.001
    vec = np.mean([word2vec[word] * (a / (a + freq[word]))
                   for word in tokens], axis=0)
    return vec


def getdistance(vec1, vec2):
    cosine = scipy.spatial.distance.cosine(vec1, vec2)
    return cosine * 100


def getresult(distance):
    if distance >= threshhold:
        return True
    return False


def usercall(filepath):
    data = getdata(filepath)
    if data == None:
        return None
    tokens = gettokens(data)
    meanvector = getmeanvector(tokens)
    return meanvector


def userresult(vec1, vec2):
    distance = getdistance(vec1, vec2)
    return getresult(distance)
