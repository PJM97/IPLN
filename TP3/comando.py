#!/usr/bin/env python3
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
    lst = []
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
                    lst.append((line[i],line[i+1],line[i+2]))

    return lst                


def filterGrammer(grammar_Matrix,gram):
    #filter
    palavras = list(map(lambda y: list(filter(lambda x: x[1]==gram, y)),grammar_Matrix))
    #list
    return [item[0] for s in palavras for item in s]







def main():
    
    args=args_Parser()  #obter as flags/respetivos argumentos

    #Terminar execuções mutuamente exclusivas: não é possivel gerar grafos nos casos sem relações
    #Restantes exclusões mutuas tratadas por args_Parser
    if((args.word  or (args.nomes == False and
        args.palavra == None and args.regex == None and
        args.verbs == False and args.word == None))
        and args.graph):
       sys.exit("Mutuamente exclusivo, não possui relações para gerar grafos")
    if(args.graph and args.output):
           sys.exit("Mutuamente exclusivo, geração de multiplos outputs")


    tagger = getTagger() #obter gramatica

    #input file
    if(args.input): 
        corpus=getFromOneFile(".",args.input)
        sent_Matrix=getSentenses(corpus)
    #stdin      
    else:   
        sent_Matrix = readStdIn()

    
    #matrix de pares (Palavra,Classe_de_Palavra)
    grammar_Matrix = list(map(tagger.tag,sent_Matrix))

    #Execução Simples: Se nenhuma flag associada a processamento de texto,
    #simplesmente imprime os pares (Palavra,Classe_de_Palavra)
    if( args.nomes == False and args.palavra == None and args.regex == None and
        args.verbs == False and args.word == None): 
        gram = [item for s in grammar_Matrix for item in s]    

    #Procura por componente gramatical(Nomes -N, nomes próprios -NPROP ...)
    # exemplo:
    #  python3 comando.py -i os_maias.txt -w N
    # python3 comando.py -i os_maias.txt -w N -o out.txt
    if(args.word):
        grammar_Matrix = list(map(tagger.tag,sent_Matrix))
        gram=filterGrammer(grammar_Matrix,args.word)

   

    """
    Opções que possuem relações de palavras, logo é possivel geração de grafos.
    """
    if(args.nomes or args.verbs or args.palavra or args.regex):

        # Sequencia de Triplos no texto de acordo com RegEx: classicas [a-z]+ ou à python \\w+
        # Ex: python3 comando.py -i os_maias.txt -r Carlos \\w+ \\w+
        # Ex: python3 comando.py -i os_maias.txt -r Carlos \\w+ \\w+ -g grafo.html
        if(args.regex):
            gram=filterRegEx(sent_Matrix,args.regex)
            if(args.graph):
                gram=tritotow(gram)
        else:
            #processar dados 
            filtered_gm=filterMatrix(grammar_Matrix)

            #Relações de nomes que se encontram na mesma frase de um texto
            # python3 comando.py -i os_maias.txt -n
            # python3 comando.py -i os_maias.txt -n -g mones.html
            if(args.nomes):
                gram = povoate_Bigrams(filtered_gm)
            #Todas as relações centradas por um verbo
            #python3 comando.py -i os_maias.txt -v
            #python3 comando.py -i os_maias.txt -v -g ver.html
            #python3 comando.py -i os_maias.txt -v -o ver.txt
            if(args.verbs):  
                gram = povoate_Trigrams(filtered_gm)
                if(args.graph): #caso de gerar grafo
                    gram=tritotow(gram)
            #Relações centradas numa dada palavra: (Maria, verbo, palavra)
            #Ex:
            #python3 comando.py -i os_maias.txt -p Maria
            #python3 comando.py -i os_maias.txt -p Maria -o mar.txt
            #python3 comando.py -i os_maias.txt -p Maria -g mar.html
            if(args.palavra):
                gram = wordRelation(args.palavra,filtered_gm)
                if(args.graph):
                    gram=tritotow(gram)
        #caso gerar grafo output   
        if(args.graph): 
            gram_weight=weigthCounter(gram)
            generateHTML(gram_weight,args.graph)
            exit(0) #termina a execução, senão o comando teria 2 outputs: gerar file + imprimir para o terminal

    #Processamento do output: ou para ficheiro ou para stdout
    if(args.output):    
        file = open(args.output,'w') 
        for l in gram:
            file.write(str(l))
            file.write(" ")
        file.close()        
    else:    #stdout
        for l in gram:
            print(l)
        
    
if __name__ == "__main__":
    main()    