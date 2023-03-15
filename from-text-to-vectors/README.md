# from-text-to-vector
Approaching Neural Search with Apache Solr and Open-source technologies

# Model:
`all-MiniLM-L6-v2` is the model recommended:

https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

# Dataset:
Passage Retrieval task is recommended:

https://microsoft.github.io/msmarco/
https://microsoft.github.io/msmarco/Datasets.html#passage-ranking-dataset

## Folder content:

To create vector embeddings from the ms-marco corpus:
- Example INPUT: documents_10k.tsv in documents folder
- Example OUTPUT: vectors_10k.tsv in vectors folder

````
python batch-sentence-transformers.py "./documents/documents_10k.tsv" "./vectors/vectors_10k.tsv"
````

To create vector embeddings from a single sentence:

````
python single-sentence-transformers.py
````