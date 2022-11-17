from sentence_transformers import SentenceTransformer
sentences = ["Welcome to the Search Solutions 2022 Tutorial by Alessandro Benedetti", "Approaching Neural Search with Apache Solr and Open-source Technologies"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
