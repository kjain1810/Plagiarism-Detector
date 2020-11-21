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

import os.path

STOPWORDS = None
word2vec = None
threshhold = None


def initialize_model(modeltype, custom=None):
    STOPWORDS = stopwords.words('english')
    glove_file = datapath('./glove.6B.100d.txt')
    word2vec_glove_file = get_tmpfile("glove.6B.100d.word2vec.txt")
    glove2word2vec(glove_file, word2vec_glove_file)
    word2vec = KeyedVectors.load_word2vec_format(word2vec_glove_file)
    if modeltype == "accuracy":
        threshhold = 1.9653999999998937
    elif modeltype == "f_score":
        threshhold = 5.977099999999503
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
    ret_removed_punc = re.sub(r'[^\w\s]', ' ', data)
    ans = word_tokenize(ret_removed_punc)
    valid_token = []
    for i in range(len(ans)):
        ans[i] = ans[i].lower()
        if ans[i] in word2vec.vocab:
            valid_token.append(ans[i])
        else:
            print("Throwing " + ans[i] + " from the file")
    return valid_token


def getmeanvector(tokens):
    vec = np.mean([word2vec[word] for word in tokens], axis=0)
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
