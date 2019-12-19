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
import re

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

def filterRegEx(t,ar):
    regEx1=ar[0]
    regEx2=ar[1]
    regEx3=ar[2]
    p1 = re.compile(regEx1)
    p2 = re.compile(regEx2)
    p3 = re.compile(regEx3)
    for line in t:
        if(len(line)>=3):   #se tiver pelo menos 3 elms na linha
            for i in range(len(line)-2):    #variar até penultimas posições
                m1=p1.match(line[i])
                m2=p2.match(line[i+1])
                m3=p3.match(line[i+2])
                #se obtivemos resultado e dá match com a regex
                if(m1 and m2 and m3 and (m1.span()[1] == len(line[i])) and 
                    (m2.span()[1] == len(line[i+1])) and
                    (m3.span()[1] == len(line[i+2]))):
                    print("(",line[i],",",line[i+1],",",line[i+2],")")


def filterGrammer(grammar_Matrix,gram):
    #filter
    palavras = list(map(lambda y: list(filter(lambda x: x[1]==gram, y)),grammar_Matrix))
    #list
    return [item[0] for s in palavras for item in s]
    
def main():
    args=args_Parser()  #obter as flags/respetivos argumentos
    tagger = getTagger() #obter gramatica

    if(args.input): #input file
        corpus=getFromOneFile(".",args.input)
        sent_Matrix=getSentenses(corpus)  
    else:   #stdin
        sent_Matrix = readStdIn()

    #grammar_Matrix = list(map(tagger.tag,sent_Matrix))
    #print(grammar_Matrix)



    #procurar algo gramatica, exemplo: python3 comando.py -i os_maias.txt -w N
    if(args.word):
        grammar_Matrix = list(map(tagger.tag,sent_Matrix))
        gw=filterGrammer(grammar_Matrix,args.word)
        for w in gw:
            print(w,"; ",end="")
        print("\n")
        exit(0)

 
    # >python3 comando.py -i os_maias.txt -r Carlos \\w+ \\w+
    if(args.regex):
        filterRegEx(sent_Matrix,args.regex)
        exit(0)

       


    """
        Estou aqui
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
           
  
    
if __name__ == "__main__":
    main()    