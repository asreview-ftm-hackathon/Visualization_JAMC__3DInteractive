# JAMC-ASReview-Hackathon

Data visualisation track

## Rationale

The idea behind our project is to facilitate exploration of data. We have developed an interactive tool that plots
the [Shell papers](https://www.ftm.nl/dossier/shell-papers#artikelen) in 3-dimensional space. The distribution of papers
is not arbitrary, but rather based on meaningful dimensions resulting in a grouping of similar documents throughout
space. This makes data exploration very intuitive. The interactive element of the project also makes it easier for an
investigator to dig through the content. An investigator can select a document to get its title as well as proximal
documents.

## Data & Preprocessing

The data can be found at the [FTM repository](https://github.com/ftmnl/asr). We download the data and load it from
our `data/` folder. For this project we mostly focused on the visualisation and thus minimal data cleaning has taken
place. We take the following data processing steps: tokenisation, vectorisation of tokens (based on frequency,
specifically tf-idf), dimensionality reduction, and finally clustering (using k-means clustering). Vectorisation is
arguably the most important step as it, to put it simply, it encodes each document into a vector. It is important that
such encoding is based on semantically meaningful features of the text. The encoding yields a high dimensionality vector
per document. Thus, a dimensionality reduction technique (specifically singular value decomposition) is used to obtain a
3-dimensional vector per document and thus plot it in a human readable manner. K-means is applied on the documents to
identify meaningful clusters, groupings of documents that are in some way similar.

## Visualization

The documents represented as 3d vectors are plotted in space, giving the document space. We have made the space
interactive allowing the user to explore the document space and select documents to view more information about them. We
further colour code documents based on their clustering (i.e., documents belonging to the same cluster will have the
same colour). However, so far the idea of clusters (and thus similarity) remains abstract. Thus, we have implemented a
method that shows a word cloud for each cluster. This would help an investigator by giving an idea of the main keywords
present in groupings of documents, hopefully assisting with the identification of topics.

## Results (demo)

## Limitations and future work

- quality of vectorization
- quality of dimensionality reduction
- kmeans clustering hyperparameter optimisation i.e., exploring different clustering setting

## How to run

To install all dependencies run `pip install -r requirements.txt`
To process the data run `python3 visualization.py`. A excel dataset is required and can be placed in the `data/`
subfolder. The only further requirement of the dataset is that it contains the following two attributes: `title`
and `abstract` both holding data of type string (i.e., text data).

To run the interactive visualisation tool run `python3 run.py` which will launch a local server
at [localhost:1337/main.html](localhost:1337/main.html)

## For the tech-savy...

You can visualize any data in our tool as long as it is exported as a JSON file with the following properties

```json
[
  {
    "document": "This is the document id",
    "title": "Title of the document",
    "x": "First dimension",
    "y": "Second dimension",
    "z": "Third dimensionO",
    "cluster": "id of the cluster (there is support for up to 6 cluster right now)",
    "norm_text_length": "normalized text length (range 0 - 10), it's used for scaling."
  },
  {
    "document": 0,
    "title": "Verzoek_regulier__facultatief_advies_uitgebr_proc.doc_dd. ",
    "x": 0.4581327643567375,
    "y": -0.10269132303493203,
    "z": 0.00710544383780284,
    "cluster": 0.0,
    "norm_text_length": 6.725033642166843
  }
]
```

Place the document under results/all_data.json