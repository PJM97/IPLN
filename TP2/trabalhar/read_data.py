import nltk

def getParagraph(corpus):
    print("ACCESSING PARAGRAPHS")
    paragraphs=corpus.paras()
    return paragraphs

def getWords(corpus):
    print("ACCESSING WORDS")
    words=corpus.words()
    return words


def getSentenses(corpus):
    print("ACCESSING SENTENCES")
    sentences=corpus.sents()
    return sentences

def getFile():
    corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(".", "input.txt")
    return corpus

def main():
    corpus=getFile()

    p=getParagraph(corpus)
    for i in p:
        print(i)

    s=getSentenses(corpus)

    for i in s:
        print(i)

    w=getWords(corpus)

    for i in w:
        print(i)

if __name__ == "__main__":
    main()    
