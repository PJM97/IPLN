import nltk
#nltk.download()
#nltk.download('punkt')
#nltk.download('mac_morpho')

tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
t0 = nltk.DefaultTagger('N')
t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
#t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
#t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)



#t3_alt = nltk.TrigramTagger(tagged_sents)
"""
from pickle import dump
output = open('mac_morpho.pkl', 'wb')
dump(t3, output, -1)
output.close()

from pickle import load
input = open('mac_morpho.pkl', 'rb')
tagger = load(input)
input.close()
"""


l='Ontem, o João Antunes comeu peixe ao almoço'
print(l)
#separa o texto em pedaços.
l1=nltk.word_tokenize('Ontem, o João Antunes comeu peixe ao almoço')
print(l1)
tagged = t1.tag(nltk.word_tokenize('Ontem, o João Antunes comeu peixe ao almoço'))
print(tagged)





"""
gramatica = r
#NE: {<NPROP>+}
#PP: {<PREP><N>}


analiseGramatical = nltk.RegexpParser(gramatica)
analiseGramatical.parse(tagged)

tree = analiseGramatical.parse(tagged)
tree.draw()
print("ola")
"""
