# JAMC-ASReview-Hackathon
Data visualisation track

## Rationale
The idea behind our project is to facilitate exploration of data. We have developed an interactive tool that plots the [Shell papers](https://www.ftm.nl/dossier/shell-papers#artikelen) in 3-dimensional space. The distribution of papers is not arbitrary, but rather based on meaningful dimensions resulting in a grouping of similar documents throughout space. This makes data exploration very intuitive. 
## Data & Preprocessing

The data can be found at the [FTM repository](https://github.com/ftmnl/asr).
We downloaded the data and load it from our `data/` folder.

## Visualization

## Results (demo)
## Limitations and future work

## How to run
## For the tech-savy...
You can visualize any data in our tool as long as it is exported as a JSON file with the following properties
{
"document": This is the document id,
"title": Title of the document,
"x": First dimension,
"y": Second dimension,
"z": Third dimension,
"cluster": id of the cluster (there is support for up to 6 cluster right now),
"norm_text_length": normalized text length (range 0 - 10), it's used for scaling.
}

Place the document under results/all_data.json