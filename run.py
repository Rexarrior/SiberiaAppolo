import pandas as pd
import pymorphy2
import nltk
import re

from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import datetime
from multiprocessing import Pool
from tqdm import tqdm_notebook as tqdm
from gensim.models import *
from gensim import corpora



dir_hackathon = '.'
dir_data_in = f'{dir_hackathon}/Data/In'
dir_data_out = f'{dir_hackathon}/Data/Out'


all_data_in = pd.read_excel(f'{dir_data_in}/dateset_categorical_with_tnved.xlsx', header=0, index_col=0)
all_data_in.columns = ['Номер продукции', 'Коды ТН ВЭД ЕАЭС', 'Технические регламенты', 'Группа продукции', 'Общее наименование продукции', 
                       'ИЛ', 'Заявитель', 'Адрес Заявителя', 'Изготовитель', 'Страна', 'Адрес изготовителя', 'Коды ТН ВЭД ЕАЭС_ordinal', 'Технические регламенты_ordinal', 'Группа продукции_ordinal','Коды ТН ВЭД ЕАЭС текст' ]
target_groups = ['Коды ТН ВЭД ЕАЭС текст']
data_name_group = all_data_in[target_groups]


# prepare data:
prepared_data = data_name_group
for row in prepared_data.columns:
    prepared_data[row] = prepared_data[row].str.replace(r'\W', ' ')    
    prepared_data[row] = prepared_data[row].str.replace(r'\d', ' ')    
    prepared_data[row] = prepared_data[row].str.lower()
    prepared_data[row] = prepared_data[row].str.replace(r' +', ' ') 
    



nltk.download('stopwords')
nltk.download('punkt')

stop_words = nltk.corpus.stopwords.words("russian")


def lemmatize(text_in):
    lemma = pymorphy2.MorphAnalyzer()
    text = " ".join([lemma.parse(word)[0].normal_form for word in text_in.split(' ')])
    tokens = word_tokenize(text, language="russian")
    for token in tokens:
        if token in stop_words:
            tokens.remove(token)
    text = " ".join(tokens)
    return text
        


prepared_data['Номер'] = range(1, len(prepared_data) + 1)
prepared_data = prepared_data.reindex(columns=['Номер'] + target_groups)


data_lemm = prepared_data

data_lemm_out = pd.DataFrame()
data_lemm_out['Номер'] = data_lemm['Номер']
x_max = data_lemm.shape[1]
# x_max = 20
y_max = data_lemm.shape[0]
data_lemm_out = pd.DataFrame(columns=data_lemm.columns)

for x in range(x_max):
    for y in range(y_max):        
        cell = lemmatize(data_lemm_out.iloc[y][target_groups[x]])
        data_lemm_out.loc[y, target_groups[x]] = cell
        print(f'{x}   {y}')


data_lemm_out.to_excel(f'{dir_data_out}/data_lemm_morphy_tnved.xlsx', header=0)

