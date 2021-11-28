#Main script loads data, preprocess it, clusters, etc...
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans

import json

def tokenizer(text):
    return text.split()

data = pd.read_excel("data/preprocessed_data.xlsx")

#getting the text data
doc_data = data.abstract
docs = doc_data.to_list()

#vectorising documents based on tf-idf
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(docs) #returns CSR matrix DxV
idf = tfidf_vectorizer.idf_

#dimensionality reduction
svd = TruncatedSVD(n_components=3, random_state=42)
X_svd = svd.fit_transform(tfidf) #returns shape(n_samples, n_components), type(ndarray), Reduced version of X. This will always be a dense array

#k-means clustering 
km = KMeans(n_clusters=5, n_init = 15, random_state=42) #ToDo: hyperparameter optimisation
clusters = km.fit_predict(X_svd)
print(clusters[0])
clusters.resize(2509,1)
svd_clustered = np.append(X_svd, clusters, axis=1) #storing the correspoding cluster next to the reduced dimensions

dims_dict = [{'document': doc_i, 'title': data['title'][doc_i], 'x':x, 'y':y, 'z':z, 'cluster':clusters[doc_i].tolist()[0]} for doc_i, [x,y,z] in enumerate(X_svd)]
print(dims_dict[0])
json.dump(dims_dict, open("results/data_5_clusters.json",'w'), indent=0)