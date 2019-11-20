from nltk.corpus.reader.plaintext import PlaintextCorpusReader

    


def getFileNames(corpus):
    files=corpus.fileids()
    for f in files:
        print(f)

def getCorpus():
    corpus = PlaintextCorpusReader(".", r".*\.txt")
    return corpus

def getAllCorpus(corpus):
    all_text=corpus.raw()
    print(all_text)

def getFromOneFile(corpus,fname):
    ftext=corpus.raw(fname)
    print(ftext)

def main():
    corpus=getCorpus()
    getFileNames(corpus)
    getAllCorpus(corpus)
    getFromOneFile(corpus,"input.txt")
    getFromOneFile(corpus,"news1.txt")

if __name__ == "__main__":
    main()  