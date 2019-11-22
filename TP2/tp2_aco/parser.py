import nltk
import sys 
from pickle import load



#Parse all .txt file from one directory
def getALLFile():
    try:
        corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(".", r".*\.txt")
    except:
        sys.exit("Can't open input file")  
    return corpus

#Parse a specific file.
def getFromOneFile(path,fname):
    try:
        corpus=nltk.corpus.reader.plaintext.PlaintextCorpusReader(path,fname)
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

#get all portuguese stopwords.
stopwords = nltk.corpus.stopwords.words('portuguese')


#filtrar nomes e verbos.
def filterLine(line):
    return  list(filter(lambda y: (y[1]=='V' or y[1]=='N' or y[1]=='NPROP')
             and (y[0] not in stopwords or y[1]=='V'), line)) #stopword que tb é verbo fica.

def filterMatrix(matrix):
    return list(map(filterLine,matrix))


def main():

    tagger = getTagger()
    corpus=getFromOneFile(".","input.txt")
    #corpus=getALLFile()

    sent_Matrix=getSentenses(corpus) #matrix, cada linha é uma frase.

    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matix tuplos:(word,grammar)
    filtered_gm=filterMatrix(grammar_Matrix)    #filtered: names and verbs only.
    print(filtered_gm)

if __name__ == "__main__":
    main()    