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


all_data_in = pd.read_excel(f'{dir_data_in}/dataset.xlsx', header=0)
all_data_in.columns = ['Номер продукции', 'Коды ТН ВЭД ЕАЭС', 'Технические регламенты', 'Группа продукции', 'Общее наименование продукции', 
                       'ИЛ', 'Заявитель', 'Адрес Заявителя', 'Изготовитель', 'Страна', 'Адрес изготовителя']
all_data_in.head(2)

data_name_group = all_data_in[['Группа продукции', 'Общее наименование продукции']]
data_name_group


# prepare data:
prepared_data = data_name_group
for row in prepared_data.columns:
    prepared_data[row] = prepared_data[row].str.replace(r'\W', ' ')    
    prepared_data[row] = prepared_data[row].str.replace(r'\d', ' ')    
    prepared_data[row] = prepared_data[row].str.lower()
    prepared_data[row] = prepared_data[row].str.replace(r' +', ' ') 
    
prepared_data.head()



nltk.download('stopwords')
nltk.download('punkt')

stop_words = nltk.corpus.stopwords.words("russian")
stop_words.extend(['https', 'который', 'это', 'также', 'новый', 'являться', 'позволять', 'возможность', 
                   'наш', 'свой', 'ru', 'ещё', 'www', 'ru', 'com', 'пока', 'год'])

def lemmatize_cell(data_lemm, x, y):
    lemma = pymorphy2.MorphAnalyzer()
    cell = data_lemm.loc[y, data_lemm.columns[x]]
    print('Coords: ', x, y, '\n') #, datetime.datetime.now()
    text = ''
    if type(cell) == str and len(cell) > 0:
        text = " ".join([lemma.parse(word)[0].normal_form for word in cell.split(' ')])
        tokens = word_tokenize(text, language="russian")
#         tokens = lemma.parse(word)[0].normal_form 
        for token in tokens:
            if token in stop_words:
                tokens.remove(token)
        text = " ".join(tokens)
        
#     print(text, '\n')
        
    return text


prepared_data['Номер'] = range(1, len(prepared_data) + 1)
prepared_data = prepared_data.reindex(columns=['Номер', 'Группа продукции', 'Общее наименование продукции'])
prepared_data.tail(2)


data_lemm = prepared_data

data_lemm_out = pd.DataFrame()
data_lemm_out['Номер'] = data_lemm['Номер']
x_max = data_lemm.shape[1]
# x_max = 20
y_max = data_lemm.shape[0]
data_lemm_out = pd.DataFrame(columns=data_lemm.columns)

for x in range(x_max):
    for y in range(y_max):        
        cell = lemmatize_cell(data_lemm, x, y)
        data_lemm_out.loc[y, data_lemm_out.columns[x]] = cell
        
data_lemm_out


data_lemm_out.head()

data_lemm_out.to_excel(f'{dir_data_out}/data_lemm_morphy.xlsx', header=0)


vectorizer = TfidfVectorizer(max_df=0.6, min_df=0.1, stop_words=stop_words)
data_vectors = vectorizer.fit_transform(data_lemm_out['Проект'])
data_vectors


inertia = []
xy_min = 10
xy_max = 50
xy_step = 10
for k in range(xy_min,xy_max,xy_step):
    mbk  = MiniBatchKMeans(n_clusters=k,init='random', random_state=1).fit(data_vectors)
    inertia.append(np.sqrt(mbk.inertia_))
plt.plot(range(xy_min,xy_max,xy_step),inertia,marker='s')
plt.xlabel('K')
plt.ylabel('(C_k)')
plt.show()


data_to_claster = data_lemm_out
data_to_claster.head()

n_clasters = 35
mbk  = MiniBatchKMeans(n_clusters=n_clasters,init='random').fit(data_vectors)
y_kmeansMBK = mbk.predict(data_vectors)
Num = [] 
Num = [pt for pt in y_kmeansMBK]
df2 = {'Кластер': Num}
dfMBK = pd.DataFrame(df2)
data_claster_out = pd.concat([data_to_claster,dfMBK], axis=1)
data_claster_out.to_excel(f'{dir_data_out}/Claster.xlsx', index=False)
