import nltk
import sys 
from pickle import load
from collections import defaultdict 
from operator import itemgetter 
from itertools import groupby 
from collections import Counter
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

#Matrix com as linhas do texto caso seja lido pelo stdin.
def readStdIn():
    lista=[]
    sys.argv=[] #resolve o bug de ler pelo stdin não funcionar com flags.
    for line in fileinput.input():
        lista.append(line)
    
    matrix=list(map(lambda x: x.rstrip().split(),lista)) #retirar \n e separar as palavras
    return matrix 

#separa cada uma das frases
def getSentenses(corpus):
    sentences=corpus.sents()
    return sentences

#Obter ficheiro com treino gramatical
def getTagger():
    #caso não exista o ficheiro é criado
    if(not os.path.isfile('./mac_morpho.pkl')):
        treino_gram()
    try:
        input = open('mac_morpho.pkl', 'rb')
        tagger = load(input)
        input.close()
    except:
        sys.exit("Can't open input file")

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
    args=args_Parser()
    print(args.regex)

    tagger = getTagger() #obter gramatica

    if(args.input): #input file
        corpus=getFromOneFile(".",args.input)
        sent_Matrix=getSentenses(corpus)   
    else:   #stdin
        sent_Matrix = readStdIn()

    print(sent_Matrix)     
    print(args.regex)   
    """    
        

       
   
    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matriz gramaticalmente notada

    if(args.nomes): #relações com todos os nomes
        filtered_gm=filterMatrix(grammar_Matrix)
        bigram = povoate_Bigrams(filtered_gm)

        if(args.graph): #caso gerar grafo output
            nomes_weight=weigthCounter(bigram)
            generateHTML(nomes_weight,args.graph)            

        if(args.output):    #guardar em ficheiro
            file = open(args.output,'w') 
            for l in bigram:
                file.write(str(l))
            file.close()        
        else:    #stdout
            print(bigram) 
        
    elif(args.verbs):   #trigramas de palavra-verb-palavra
            filtered_gm=filterMatrix(grammar_Matrix)
            trigram = povoate_Trigrams(filtered_gm)
            
            if(args.graph): #caso de gerar grafo
                tri_two=tritotow(trigram)
                verbs_weight=weigthCounter(tri_two)
                generateHTML(verbs_weight,args.graph)
            if(args.output):
                file = open(args.output,'w') 
                for l in trigram:
                    file.write(str(l))
                file.close()        
            else:
                print(trigram)

    elif(args.palavra):
            filtered_gm=filterMatrix(grammar_Matrix) 
            tri_palavra = wordRelation(args.palavra,filtered_gm)

            if(args.graph):
                tri_two_palavra=tritotow(tri_palavra)
                verbs_weight_palavra=weigthCounter(tri_two_palavra)
                generateHTML(verbs_weight_palavra,args.graph)

            if(args.output):
                file = open(args.output,'w')
                for l in tri_palavra:
                    file.write(str(l))
                file.close()        
            else:
                print(tri_palavra) 

    elif(args.regex):
        print("Caso pra regEx")            
    """
    
if __name__ == "__main__":
    main()    