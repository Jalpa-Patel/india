
# coding: utf-8

# In[69]:

# Assignment 8 : Similarity of Text and Graph based models

import re
import pandas as pd
import numpy as np
import math
from collections import Counter

#read .h5 file
store = pd.HDFStore('store2.h5')

#Dataframe variable
df1 = store['df1']
df2 = store['df2']

#1.1.1 Jaccard - Similarity on sets

#Build the word sets of each article for each article id. 
df1["wordset"] = df1.text.apply(lambda x: re.findall("\w+",str(x)))
df1.head()

#Calculate the jaccard coefficent
def calcJaccardSimilarity(wordset1, wordset2):
    union_of_wordset = list(set.union(wordset1,wordset2))
    intersection_of_wordset = list(set.intersection(wordset1,wordset2))
    jaccard_coefficient = float(len(intersection_of_wordset))/len(union_of_wordset)
    return jaccard_coefficient

#Compute the result for the articles Germany and Europe.

article_ge = df1[df1.name=="Germany"]
wordset_for_ge = str(article_ge['text'].values).split()
set_ge = set(wordset_for_ge)
article_eu = df1[df1.name=="Europe"]
wordset_for_eu = str(article_eu['text'].values).split()
set_eu = set(wordset_for_eu)

print("Jaccard Word Similarity :" + str(calcJaccardSimilarity(set_ge,set_eu)))

#1.1.2 TF-IDF with cosine similarity

#Count the term frequency of each term for each article and document frequencies of each term. 
tf_foreach_article['tf'] = df1.wordset.apply(lambda x: Counter(x))
print(tf_foreach_article.head())
tdf_foreach_article['tdf']=dict(tf_foreach_article)
print(tf_foreach_article)

#For each article id provide a dictionary of terms with their tf-idf scores as the corresponding values.

def idf(word, list_of_docs):
    return math.log(len(list_of_docs) /
            float(num_docs_containing(word, list_of_docs)))
def tf_idf(word, doc, list_of_docs):
    return (tf(word, doc) * idf(word, list_of_docs))

# Implement Cosine Similarity functions taking two term frequency dictionary 

def calculateCosineSimilarity(tfidf1, tfidf2):
    all_words = set(tfidf1.keys())& set(tfidf2.keys())
    v1 = [tfidf1[k] for k in all_words]
    v2 = [tfidf2[k] for k in all_words]
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    add1 = math.sqrt(sum(n ** 2 for n in v1))
    add2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (add1 * add2)

#Compute the result for the articles Germany and Europe.
text_ge = dict(Counter(wordset_for_ge)) #This is the dictionary for TF in article Germany
text_eu = dict(Counter(wordset_for_eu))

print('TF-IDF Cosine Similarity:', calculateCosineSimilarity(text_ge,text_eu))


#1.2 Similarity of Graphs

article_ge_outlink = df2[df2.name=="Germany"]
wordset_for_ge_outlink = str(article_ge_outlink['out_links'].values).split()
set_ge_outlink = set(wordset_for_ge_outlink)
article_eu_outlink = df2[df2.name=="Europe"]
wordset_for_eu_outlink = str(article_eu_outlink['out_links'].values).split()
set_eu_outlink = set(wordset_for_eu_outlink)

print("Jaccard Graph Similarity :" + str(calcJaccardSimilarity(set_ge_outlink,set_eu_outlink)))




# In[ ]:




# In[ ]:



