#Main script loads data, preprocess it, clusters, etc...
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans

import json

def tokenizer(text):
    return text.split()

#normalizing lengths to use for visualisation
def normalize_length(length:int):
    if length == 0:
        return 0
    return np.log(length) #ln()

def get_wordclouds(tfidf_array_clustered, index_values, n_clusters=5, top_n=15):
    #generates word cloud for the documents in a cluster based on the tf-idf score of its constituent words
    for cluster in range(n_clusters):
        fully_indexed_per_cluster = {}
        cluster_indices = np.where(tfidf_array_clustered[:,-1]==cluster)
        for row in tfidf[cluster_indices[0]]:
            for (column,value) in zip(row.indices,row.data):
                fully_indexed_per_cluster[index_values[column]] = value     

        wc = WordCloud(width=1200, height=800, background_color="white")
        wordcloud = wc.generate_from_frequencies(fully_indexed_per_cluster)
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        fig.suptitle(f"Cluster {cluster}")
        plt.show()
        #plt.savefig(f"results/word_cloud_cluster_{cluster}")

data = pd.read_excel("data/preprocessed_data.xlsx") # read in the data

#getting the text data
doc_data = data.abstract
docs = doc_data.to_list()

data["doc_length"] = [len(doc.split()) for doc in data["abstract"].tolist()]
data["doc_length_normalized"] = data["doc_length"].apply(normalize_length)

#vectorising documents based on tf-idf
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(docs) #returns CSR matrix of size DxV
tfidf_array = tfidf.toarray() #converting to numpy array

#dimensionality reduction
svd = TruncatedSVD(n_components=3, random_state=42)
X_svd = svd.fit_transform(tfidf) #returns shape(n_samples, n_components), type(ndarray), Reduced version of X. This will always be a dense array

#k-means clustering 
km = KMeans(n_clusters=5, n_init = 15, random_state=42) #ToDo: hyperparameter optimisation
clusters = km.fit_predict(X_svd)

clusters.resize(2509,1)
svd_clustered = np.append(X_svd, clusters, axis=1) #storing the correspoding cluster next to the reduced dimensions
tfidf_array_clustered = np.append(tfidf_array, clusters, axis=1)

#from https://stackoverflow.com/questions/45232671/obtain-tf-idf-weights-of-words-with-sklearn
index_value = {v: k for k, v in tfidf_vectorizer.vocabulary_.items()} #dictionary --> A mapping of words to their tf-idf values.

get_wordclouds(tfidf_array_clustered, index_value)
all_data = [{'document': doc_i, 'title': data['title'][doc_i], 'x':x, 'y':y, 'z':z, 'cluster':clusters[doc_i].tolist()[0]} for doc_i, [x,y,z] in enumerate(X_svd)]
dims_dict = [{'document': doc_i, 'title': data['title'][doc_i], 'x':x, 'y':y, 'z':z, 'cluster': svd_clustered[doc_i][3], 'norm_text_length': data['doc_length_normalized'][doc_i]} for doc_i, [x,y,z] in enumerate(X_svd)]
#json.dump(dims_dict, open("results/all_data.json",'w'), indent=0)






    