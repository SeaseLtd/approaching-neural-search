from sentence_transformers import SentenceTransformer

sentence = ["what is the gre test"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentence)
# to remove the initial "array" string and the trailing "dtype=float32"
vector = repr(list(embeddings)[0])[6:-22]
print(vector)