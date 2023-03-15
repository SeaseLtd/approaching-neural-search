from sentence_transformers import SentenceTransformer

# A sentence to encode
sentence = ["what is the gre test"]

# Load or create a SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Compute sentence embeddings
embeddings = model.encode(sentence)

# Create an array of floats comma separated (removing the initial "array" string and the trailing "dtype=float32")
vector_embeddings = repr(list(embeddings)[0])[6:-22]
print(vector_embeddings)