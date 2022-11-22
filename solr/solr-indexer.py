import sys
import pysolr

## configurations
SOLR_ADDRESS = 'http://localhost:8983/solr/ms-marco'

BATCH_SIZE = 100
solr = pysolr.Solr(SOLR_ADDRESS, always_commit=True)


def index_documents(documents_filename, embedding_filename):
    with open(documents_filename, "r") as documents_file:
        with open(embedding_filename, "r") as vectors_file:
            documents = []
            for index, (document, vector_string) in enumerate(zip(documents_file, vectors_file)):

                vector = [float(w) for w in vector_string.split(",")]
                doc = {
                    "id": str(index),
                    "text": document,
                    "vector": vector
                }

                documents.append(doc)

                if index % BATCH_SIZE == 0:
                    solr.add(documents)
                    documents = []
                    print("==== indexed {} documents ======".format(index))

            print("finished")


def main():
    document_filename = sys.argv[1]
    embedding_filename = sys.argv[2]
    index_documents(document_filename, embedding_filename)


if __name__ == "__main__":
    main()