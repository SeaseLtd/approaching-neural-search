from sentence_transformers import SentenceTransformer
sentences = ["what is the name of the famous painting at louvre"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
vector = list(embeddings)
print(vector)