import sys
import json


def find(doc, find_term):
    coincidences = 0
    for word in doc:
        if word == find_term:
            coincidences = coincidences + 1
    return coincidences


def main(args):
    words = []
    file_words = open("AnalisisGenerados/wordsGen.txt", "r")
    words = json.JSONDecoder().decode(file_words.read())

    documents = []
    file_documents = open("AnalisisGenerados/documentoMatWS.txt", "r")
    documents = json.JSONDecoder().decode(file_documents.read())

    listword = {}
    for key, doc in documents.items():
        hist = []
        for word in words:
            hist.append(find(doc, word))
        listword[key] = hist

    file = open("AnalisisGenerados/vector_space.txt", "w")
    file.write(json.JSONEncoder().encode(listword))
    file.close()


# metodo main
if __name__ == '__main__':
    main(sys.argv)
