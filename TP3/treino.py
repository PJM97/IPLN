import nltk
import sys 
from pickle import dump

#Função que gera o ficheiro com o treino da Gramatica
def treino_gram():
    #Treino
    tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
    t0 = nltk.DefaultTagger('N')
    t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
    t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
    t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)

    #Escrita do resultado do treino em Ficheiro.
    output = open('mac_morpho.pkl', 'wb')
    dump(t3, output, -1)
    output.close()




