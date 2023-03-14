import sys
import pysolr
import time

## Solr configuration
SOLR_ADDRESS = 'http://localhost:8983/solr/ms-marco'

BATCH_SIZE = 100
# Create a client instance
solr = pysolr.Solr(SOLR_ADDRESS, always_commit=True)


def index_documents(documents_filename, embedding_filename):
    # open the file containing text
    with open(documents_filename, "r") as documents_file:
        # open the file containing vectors
        with open(embedding_filename, "r") as vectors_file:
            documents = []
            # for each document (text and related vector) creates a JSON document
            for index, (document, vector_string) in enumerate(zip(documents_file, vectors_file)):

                vector = [float(w) for w in vector_string.split(",")]
                doc = {
                    "id": str(index),
                    "text": document,
                    "vector": vector
                }
                # append JSON document to a list
                documents.append(doc)

                # to index batches of documents at a time
                if index % BATCH_SIZE == 0 and index != 0:
                    # how you'd index data to Solr
                    solr.add(documents)
                    documents = []
                    print("==== indexed {} documents ======".format(index))
            # to index the rest, when 'documents' list < BATCH_SIZE
            if documents:
                solr.add(documents)
            print("Finished")


def main():
    document_filename = sys.argv[1]
    embedding_filename = sys.argv[2]
    initial_time = time.time()
    index_documents(document_filename, embedding_filename)
    finish_time = time.time()
    print('Documents indexed in {:f} seconds\n'.format(finish_time - initial_time))

if __name__ == "__main__":
    main()