#!/usr/bin/python

from sentence_transformers import SentenceTransformer
import torch
import sys
from itertools import islice

BATCH_SIZE = 50
INFO_UPDATE_FACTOR = 1
MODEL_NAME = 'all-MiniLM-L6-v2'

model = SentenceTransformer(MODEL_NAME)
if torch.cuda.is_available():
    model = model.to(torch.device("cuda"))
print(model.device)


def main():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    batch_encode_to_vectors(input_filename, output_filename)


def batch_encode_to_vectors(input_filename, output_filename):
    with open(input_filename, 'r') as documents_file:
        with open(output_filename, 'w+') as out:
            processed = 0
            for n_lines in iter(lambda: tuple(islice(documents_file, BATCH_SIZE)), ()):
                processed += 1
                if processed % INFO_UPDATE_FACTOR == 0:
                    print("processed {} batch of documents".format(processed))
                vectors = encode(n_lines)
                for v in vectors:
                    out.write(','.join([str(i) for i in v]))
                    out.write('\n')


def encode(documents):
    embeddings = model.encode(documents, show_progress_bar=True)
    print('vector dimension: ' + str(len(embeddings[0])))
    return embeddings


if __name__ == "__main__":
        main()
