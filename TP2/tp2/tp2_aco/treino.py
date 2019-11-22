import nltk
import sys 
from pickle import dump


"""
    Este codigo vai ser só preciso correr uma vez, o objetivo 
    é treinar a rede para depois podermos identificar gramatica em portugues, nomes, verbos etc...
"""

tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
t0 = nltk.DefaultTagger('N')
t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)


t3_alt = nltk.TrigramTagger(tagged_sents)


output = open('mac_morpho.pkl', 'wb')
dump(t3, output, -1)
output.close()




