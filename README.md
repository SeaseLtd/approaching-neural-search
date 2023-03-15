# approaching-neural-search
Approaching Neural Search with Apache Solr and Open-source technologies 

Tutor(s): Alessandro Benedetti and Ilaria Petreti

# Introduction:
This is the repository for all the Solr neural search tutorial material. Here you can find everything you need to implement a simple Solr system to perform neural queries.

For a step-by-step description read our [blog post](https://sease.io/2023/01/apache-solr-neural-search-tutorial.html).

# Requirements:

To replicate this tutorial, you need:

- Solr 9.1.1 (download [here](https://solr.apache.org/downloads.html))
- python 3.8
- to install the requirements.txt in your python environment

e.g.

using pip
```
pip install -r requirements.txt
```

using Conda
```
conda create --name solr-neural-search-tutorial --file requirements.txt
conda activate solr-neural-search-tutorial
```

## Repository content ##
- **[from-text-to-vectors](from-text-to-vectors)**: contains the python script to generate vector embeddings
  - **[documents](from-text-to-vectors/documents)**: contains an example of the MS Marco passage retrieval data (10k)
  - **[vectors](from-text-to-vectors/vectors)**: contains the vector embeddings obtained from the MS Marco passage retrieval data (10k)
- **[solr](solr)**: contains the python script to index batches of documents to Solr at once from a file and a JSON file containing a Postman collection of Solr requests for neural search
  - **[ms-marco](solr/ms-marco)**: contains Solr configuration files

## Pipeline commands: ##
To run Solr and create the ms-marco collection:

````
cd solr-9.1.1
bin/solr start
bin/solr create -c ms-marco
````

To produce vectors externally:

````
cd from-text-to-vectors
python batch-sentence-transformers.py "./documents/documents_10k.tsv" "./vectors/vectors_10k.tsv"
````

To index batches of documents to Solr:

````
cd solr
python solr-indexer.py "../from-text-to-vectors/documents/documents_10k.tsv" "../from-text-to-vectors/vectors/vectors_10k.tsv"
````

To encode a query:

````
cd from-text-to-vectors
python single-sentence-transformers.py
````

To run knn queries import the following file into Postman to test and interact with Solr:

````
Solr_Neural_Search_Tutorial.postman_collection.json
````
