from nltk.corpus import PlaintextCorpusReader
import nltk

"""

    este codigo nao funciona mas, tá perto.

"""
corpus_root = '/'
def main():
    wordlists = nltk.corpus.reader.plaintext.PlaintextCorpusReader("./", "./input.txt")
    print(wordlists.fileids())
    print("ola")

if __name__ == "__main__":
    main()    
