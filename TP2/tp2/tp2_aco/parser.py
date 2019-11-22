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

def getTagger():
    input = open('mac_morpho.pkl', 'rb')
    tagger = load(input)
    input.close()
    return tagger

stopwords = nltk.corpus.stopwords.words('portuguese')



def main():
    print("Hello world")
    tagger = getTagger()
    #tagged = tagger.tag(nltk.word_tokenize('Ontem, o João Antunes comeu peixe ao almoço'))

    """

        #Isto está a funcionar o problema é que o processamento é lento, por isso tenho a matrix poupa tempo.

    corpus=getFile()
    sent_Matrix=getSentenses(corpus)
    print(sent_Matrix)

  
    #gramas para obter componente gramatical
    tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
    t0 = nltk.DefaultTagger('N')
    t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)

    gramer_Matrix = list(map(t1.tag,sent_Matrix))

    print(gramer_Matrix)
    """
    #print(poupar_Tempo)
    #print(stopwords)

    """
    my_string=[('A', 'ART'), ('casa', 'N'), ('que', 'PRO-KS-REL'), ('os', 'ART'),
             ('Maias', 'NPROP'), ('vieram', 'V'), ('habitar', 'N'), ('em', 'PREP|+'),
             ('Lisboa', 'NPROP'), (',', ','), ('no', 'KC'), ('Outono', 'NPROP'), ('de', 'PREP'),
             ('1875', 'N'), (',', ','), ('era', 'V'), ('conhecida', 'PCP'), ('na', 'NPROP'),
             ('vizinhança', 'N'), ('da', 'NPROP'), ('Rua', 'NPROP'), ('de', 'PREP'), ('S', 'NPROP'),
             ('.', '.'), ('Francisco', 'NPROP'), ('de', 'PREP'), ('Paula', 'NPROP'), (',', ','),
             ('e', 'KC'), ('em', 'PREP|+'), ('todo', 'PROADJ'), ('o', 'ART'), ('bairro', 'N'),
             ('das', 'NPROP'), ('Janelas', 'NPROP'), ('Verdes', 'NPROP'), (',', ','), ('pela', 'NPROP'),
             ('Casa', 'NPROP'), ('do', 'NPROP'), ('Ramalhete', 'N'), (',', ','), ('ou', 'KC'),
             ('simplesmente', 'ADV'), ('o', 'ART'), ('Ramalhete', 'N'), ('.', '.')]
    """         
    #result = [x.strip() for x in my_string.split(',')]
    #line = [x for (x,y) in my_string]
    #filtrado1 = list(filter(lambda y: (y[1]=='V' or y[1]=='N' or y[1]=='NPROP'), my_string))
    #print(filtrado1)
    #filtrado = list(filter(lambda y: (y[1]=='V' or y[1]=='N' or y[1]=='NPROP') and (y[0] not in stopwords or y[1]=='V'), my_string))
    #print(filtrado)
    #print(stopwords)

    #print(line)


if __name__ == "__main__":
    main()    