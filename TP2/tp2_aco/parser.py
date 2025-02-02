import nltk
import sys 
from pickle import load
from collections import defaultdict 
from operator import itemgetter 
from itertools import groupby 
import json
from collections import Counter
import csv

"""
Este codigo todo abre um ou multiplos ficheiros,
filtra o conteudo de modo a calcular relaçoes existentes entre nome-nome e nome-verbo-nome.
Armazena no resultado em ficheiros json.
"""

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
    Tuplos para representar relacao de nome com nome.
"""
def filter_name_bigrams(line):
    nomes=[]
    for i in range (len(line)-1):
        if((line[i][1]=='N' or line[i][1]=='NPROP') and (line[i+1][1]=='N' or line[i+1][1]=='NPROP')):
            nomes.append((line[i][0],line[i+1][0])) 
    return nomes        

def filter_trigram_relations(line):
    tri=[]
    for i in range (len(line)-2):
        if((line[i][1]=='N' or line[i][1]=='NPROP') and (line[i+1][1]=='V') and (line[i+2][1]=='N' or line[i+2][1]=='NPROP')):
            tri.append((line[i][0],line[i+1][0],line[i+2][0]))
    return tri 

#povoar o bi e tri-grama.
def povoate_grams(filtered_gm):
    bigram=[]
    trigram=[]
    for sentence in filtered_gm:
        bigram = bigram + filter_name_bigrams(sentence)
        trigram = trigram + filter_trigram_relations(sentence)
    return bigram , trigram

def dic_names(bigram):
    res_bi = dict((k, [v[1] for v in itr]) for k, itr in groupby( 
                                bigram, itemgetter(0)))
    return res_bi 

def dic_verbs(trigram):
    res_tri = defaultdict(list) 
    for i in trigram:
        res_tri[i[1]].append({'in_name':i[0],'out_name':i[2]})
    return dict(res_tri)

def save_Relation(dic,fn):
    with open(fn, 'w', encoding='utf8') as json_file:
        json.dump(dic, json_file, indent=4, ensure_ascii=False)


#list of triples to tuples.
def tritotow(tri):
    tri_res=[]
    for t in tri:
        tri_res.append((t[0],t[1]))
        tri_res.append((t[1],t[2]))
    return tri_res


#graph weight counter.
def weigthCounter(list):
    contado = Counter(list)
    list_graph = [(k[0],k[1],v) for k, v in contado.items()]
    return list_graph


def save_csv(file,list):
    with open(file, 'w') as f:
        fieldnames = ['Source', 'Target', 'Weight']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer = csv.writer(f, delimiter=',')
        writer.writerows(list)


def filter_trigram_relations_by_word(line,word):
    tri=[]
    for i in range (len(line)-2):
        if((line[i][0]==word) and (line[i+1][1]=='V') and (line[i+2][1]=='N' or line[i+2][1]=='NPROP')):
            tri.append((line[i][0],line[i+1][0],line[i+2][0]))
    return tri 

def wordRelation(word,filtered_gm):
    trigram=[]
    for sentence in filtered_gm:
        trigram = trigram + filter_trigram_relations_by_word(sentence,word)
    return trigram


def main():

    #get file and grammar
    tagger = getTagger()
    corpus=getFromOneFile(".","input.txt")
    #corpus=getALLFile()    #para dar parse de multiplos files.

    sent_Matrix=getSentenses(corpus) #matrix, cada linha é uma frase.

    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matix tuplos:(word,grammar)
    filtered_gm=filterMatrix(grammar_Matrix)    #filtered: names and verbs only.
    


    
    #bi e tri-gramas.
    bigram=[]
    trigram=[]
    bigram , trigram = povoate_grams(filtered_gm)

    #print(bigram)
    print(trigram)

    #separar os trigramas.
    tri_two=tritotow(trigram)
    print(tri_two)

    nomes_weight=weigthCounter(bigram)
    verbs_weight=weigthCounter(tri_two)
    
    save_csv('nomes.csv',nomes_weight)
    save_csv('verbs.csv',verbs_weight)
    
    #dicionario
    #res_dic=dic_names(bigram)
    #res_verb=dic_verbs(trigram)

    #json
    #save_Relation(res_dic,"nomes.json")
    #save_Relation(res_verb,"verbos.json")
 

    """
        Gerar csv com info do Carlos, Maria e Ramalhete
    """
    #tri_carlos = wordRelation('Carlos',filtered_gm)
    #tri_two_carlos=tritotow(tri_carlos)
    #verbs_weight_carlos=weigthCounter(tri_two_carlos)
    #save_csv('carlos.csv',verbs_weight_carlos)

    #tri_maria = wordRelation('Maria',filtered_gm)
    #tri_two_maria=tritotow(tri_maria)
    #verbs_weight_maria=weigthCounter(tri_two_maria)
    #save_csv('maria.csv',verbs_weight_maria)

    #tri_ramalhete = wordRelation('Ramalhete',filtered_gm)
    #tri_two_ramalhete=tritotow(tri_ramalhete)
    #verbs_weight_ramalhete=weigthCounter(tri_two_ramalhete)
    #save_csv('ramalhete.csv',verbs_weight_ramalhete)


if __name__ == "__main__":
    main()    