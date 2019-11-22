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

"""
    Agora temos de tratar de relações.
    Podemos indicar que os nomes podem relacionar-se com outros nomes.
    depois temos o caso geral de dois nomes relacionarem-se a partir de um verbo.
"""

"""
    Tuplos para representar relacao de nome com nome.
"""
def filter_name_bigrams(line):
    nomes=[]
    for i in range (len(line)-1):
        if((line[i][1]=='N' or line[i][1]=='NPROP') and (line[i+1][1]=='N' or line[i+1][1]=='NPROP')):
            nomes.append((line[i][0],line[i+1][0]))
    print("names bigrams:")
    print(nomes)        

def filter_trigram_relations(line):
    tri=[]
    for i in range (len(line)-2):
        if((line[i][1]=='N' or line[i][1]=='NPROP') and (line[i+1][1]=='V') and (line[i+2][1]=='N' or line[i+2][1]=='NPROP')):
            tri.append((line[i][0],line[i+1][0],line[i+2][0]))
    print("Trigrams:")
    print(tri)


def main():

    tagger = getTagger()
    corpus=getFromOneFile(".","input.txt")
    #corpus=getALLFile()

    sent_Matrix=getSentenses(corpus) #matrix, cada linha é uma frase.

    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matix tuplos:(word,grammar)
    #print(grammar_Matrix)
    filtered_gm=filterMatrix(grammar_Matrix)    #filtered: names and verbs only.
    #print(filtered_gm)
    fst_sentense=filtered_gm[0]
    print(fst_sentense)
    filter_name_bigrams(fst_sentense)
    filter_trigram_relations(fst_sentense)

if __name__ == "__main__":
    main()    