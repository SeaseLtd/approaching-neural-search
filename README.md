# approaching-neural-search
Approaching Neural Search with Apache Solr and Open-source technologies 

Tutor(s): Alessandro Benedetti

# Introduction:
Please join us as to explore this exciting new Apache Solr feature and learn how you can leverage it to improve your search experience!

# Schedule:
9:00 - 9:20 - Introduction to Semantic Search Problems (vocabulary mismatch problem, semantic similarity)

9:20 - 9:40 - From Text to Vectors (Sparse vs Dense vector representation)

9:40 - 10:10 - How to generate vectors from text and integrate large language models with Apache Solr

10:10 - 10:40 - How Approximate Nearest Neighbor (ANN) approaches work, with a focus on Hierarchical Navigable Small World Graph (HNSW)

10:40 - 11:10 - How the Apache Lucene implementation works

11:10 - 11:30 - Break

11:30 - 12:00 - How the Apache Solr implementation works, with the new field type and query parser introduced

12:00 - 12:35 - How to run KNN queries and how to use it to rerank a first-stage pass

12:35 - 13:05 - Limitations and how to mitigate them

13:05 - 13:20 - Future Works

# Rquirements:

To replicate this work just install the requirements.txt in your python environment.

e.g.

using pip
```
pip install -r requirements.txt
pip install sentence-transformers
pip install pysolr
```

using Conda
```
conda create --name approaching-neural-search-tutorial-22 --file requirements.txt
conda activate approaching-neural-search-tutorial-22
conda install -c conda-forge sentence-transformers | pip install sentence-transformers
```