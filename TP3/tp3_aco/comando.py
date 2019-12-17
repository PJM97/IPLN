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
import os
from treino import treino_gram
import fileinput
from graphics import generateHTML

#Parse do ficheiro de entrada
def getFromOneFile(path,fname):
    try:
        corpus=nltk.corpus.reader.plaintext.PlaintextCorpusReader(path,fname)
    except:
        sys.exit("Can't open input file")   
    return corpus 

#separa cada uma das frases
def getSentenses(corpus):
    sentences=corpus.sents()
    return sentences

#Obter ficheiro com treino gramatical
def getTagger():
    #caso não exista o ficheiro é criado
    if(not os.path.isfile('./mac_morpho.pkl')):
        treino_gram()
    #abrir o ficheiro.
    try:
        input = open('mac_morpho.pkl', 'rb')
        tagger = load(input)
        input.close()
    except:
        sys.exit("Can't open input file")

    return tagger        

#Matrix com as linhas do texto caso seja lido pelo stdin.
def readStdIn():
    lista=[]
    for line in fileinput.input():
        lista.append(line)
    matrix=list(map(lambda x: x.rstrip().split(),lista)) #retirar \n e separar as palavras
    return matrix 

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

def povoate_Bigrams(filtered_gm):
    bigram=[]
    for sentence in filtered_gm:
        bigram = bigram + filter_name_bigrams(sentence)
    return bigram

def povoate_Trigrams(filtered_gm):
    trigram=[]
    for sentence in filtered_gm:
        trigram = trigram + filter_trigram_relations(sentence)
    return trigram


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
    args=args_Parser() #obter as flags

    tagger = getTagger() #obter o tagger gramatical

    #caso seja passado um file como argumento
    if(args.input):
        corpus=getFromOneFile(".",args.input)
        sent_Matrix=getSentenses(corpus)   
    #Caso de ler do stdin 
    else:
        sent_Matrix = readStdIn()
    
    #matriz: Cada linha é uma frase e cada elemento é um tuplo (palavra,elem gramatical)
    grammar_Matrix = list(map(tagger.tag,sent_Matrix))
    #print(grammar_Matrix)

    """
        Agora vamos tratar de cada um dos casos possiveis 
        que o comando pode correr.
    """
    #caso dos nomes sem pesos
    if(args.nomes):
        filtered_gm=filterMatrix(grammar_Matrix) #matriz filtrada.
        bigram = povoate_Bigrams(filtered_gm)

        #se quiser gerar os grafos
        if(args.graph):
            nomes_weight=weigthCounter(bigram)
            generateHTML(nomes_weight,args.graph)
            #print(nomes_weight)
            
            
        """   
        #Caso haja um file output escreve os bigrams nele
        if(args.output):
            file = open(args.output,'w') 
            for l in bigram:
                file.write(str(l))
            file.close()        
        else:    
            print(bigram)   #simplesmente redireciona para o stdout.
        """

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