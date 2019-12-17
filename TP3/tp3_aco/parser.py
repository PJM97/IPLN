import nltk
import sys 
from pickle import load
from collections import defaultdict 
from operator import itemgetter 
from itertools import groupby 
import json
from collections import Counter
import csv
from args import args_Parser

r"""
     __________________
    |                  |
    |Enunciado : Tema 1|
    |__________________|    
 Usar o nltk 
Dado o texto anotado e umas regras (Padrão, Ação) criar triplos de informação extraída.
 “quero procurar o padrão "Nome, ..."".
Exemplo de padrão:
    grep -Po ’verde e \w+’ JornalAngolano.txt (ficheiro no natura jj)
    Output: verde e branco; verde e amarelo

Os triplos de informação extraída deverão estar relacionados com o texto e com padrão dado como input
Exemplos de padrões: Adj NP ; Adj Adj N ; ...
Mais avançado: Pode ser um adjetivo concreto ou um adjetivo qualquer (lemma)

Exemplos:
    De coisas a fazer:
        Encontrar triplos relacionados por um dado verbo.
        Encontrar todas as relações com um dado verbo especifico


Podemos para uma palavra buscar a sua anterior e a sua seguinte.    

podemos fazer com varias versões:
    Filtrado sobre o texto -> 

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

#separa cada um dos paragrafos
def getParagraph(corpus):
    paragraphs=corpus.paras()
    return paragraphs

#separa cada uma das palavras
def getWords(corpus):
    words=corpus.words()
    return words
#separa cada uma das frases
def getSentenses(corpus):
    sentences=corpus.sents()
    return sentences

#get do tagger: Permite a identificação gramatical de cada uma das palavras.
def getTagger():
    input = open('mac_morpho.pkl', 'rb')
    tagger = load(input)
    input.close()
    return tagger

#get all portuguese stopwords.
stopwords = nltk.corpus.stopwords.words('portuguese')

#filtrar nomes e verbos de cada linha.
def filterLine(line):
    return  list(filter(lambda y: (y[1]=='V' or y[1]=='N' or y[1]=='NPROP')
             and (y[0] not in stopwords or y[1]=='V'), line)) #stopword inclui verbos em alguns casos.

#Filtra sobre o texto apenas nomes e verbos
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
    args_Parser()
    """
    tagger = getTagger()     #obter o tagger gramatical
    corpus=getFromOneFile(".","input.txt")  #ler input file
    #corpus=getALLFile()    #para dar parse de multiplos files.
    sent_Matrix=getSentenses(corpus) #matrix, cada linha é uma frase.
    """
    """
    Importante pro trabalho:
        Temos aqui a matrix com as palavras e a sua correspondente valor gramatical
    """
    #grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matix tuplos:(word,grammar)
    #print(grammar_Matrix)




    #filtered_gm=filterMatrix(grammar_Matrix)    #filtered: names and verbs only.

    #print(filtered_gm) #matriz filtrada pela segunda componente de cada elemento.
    
    #bi e tri-gramas.
    #bigram=[]
    #trigram=[]
    #bigram , trigram = povoate_grams(filtered_gm)
    
    """
        Em Bigrams -> temos os pares de nomes consecutivos
        Em Trigrams -> temos os triplos, onde o elem do meio é um verbo.
    """
    """
    #print(trigram)
    
    #print(bigram)
    #print(trigram)

    #separar os trigramas.
    #Exemplo:('Maias', 'vieram','habitar') -> ('Maias', 'vieram'), ('vieram', 'habitar')
    tri_two=tritotow(trigram)
    #print(tri_two)
    
    nomes_weight=weigthCounter(bigram)  #gera trigram com o weight na ultima componete
    #print(nomes_weight)
    
    verbs_weight=weigthCounter(tri_two)
    print(verbs_weight)
    #dicionario
    #res_dic=dic_names(bigram)
    #res_verb=dic_verbs(trigram)
    """
 

  


if __name__ == "__main__":
    main()    