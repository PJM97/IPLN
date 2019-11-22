import nltk
import sys 
from pickle import load


def getFile():
    try:
        corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(".", "input.txt")
    except:
        sys.exit("Can't open input file")  
    return corpus


def getParagraph(corpus):
    paragraphs=corpus.paras()
    return paragraphs

def getWords(corpus):
    words=corpus.words()
    return words


def getSentenses(corpus):
    sentences=corpus.sents()
    return sentences

def getTagger():
    input = open('mac_morpho.pkl', 'rb')
    tagger = load(input)
    input.close()
    return tagger

stopwords = nltk.corpus.stopwords.words('portuguese')


def filterLine(line):
    return list(filter(lambda y: (y[1]=='V' or y[1]=='N' or y[1]=='NPROP') and (y[0] not in stopwords or y[1]=='V'), line))

def filterMatrix(matrix):
    return list(map(filterLine,matrix))


def main():

    tagger = getTagger()
    corpus=getFile()
    sent_Matrix=getSentenses(corpus) #matrix, cada linha é uma frase.

    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matix tuplos:(word,grammar)
    filtered_gm=filterMatrix(grammar_Matrix)    #filtered: names and verbs only.
    print(filtered_gm)

if __name__ == "__main__":
    main()    