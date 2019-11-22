""""
Em portugues:

"""

from nltk.examples.pt import *


ptext2

ptext1.concordance('olhos')

ptext1.similar('chegar')

text1.collocations()

ptext3.generate()

psent1

len(psent1)

sorted(set(psent1))

for w in psent2:
    print(w, len(w), w[-1])


[w.upper() for w in psent2]

[w for w in psent1 if w.endswith('a')]

[w for w in ptext4 if len(w) > 15]

fd1 = FreqDist(ptext1)


fd1['olhos']

fd1.max()

fd1.samples()[:100]





""""
#
#
#
#
#
#

    A partir daqui parece estar a dar:

#
# 
# 
# 
# 
# 
# 
#     
"""



from nltk.corpus import machado #biblioteca com textos Machado de Assis

#dowload do ficheiro.
#nltk.download('machado')

#lista com os nomes dos ficheiros encontrados.
machado.fileids()

#agora aqui em raw temos todo o ficheiro, literalmente todo o corpo.
raw_text = machado.raw('romance/marm05.txt')

raw_text[10000:10200]


#lista que em cada posicao poem uma palavra do texto.
text1 = machado.words('romance/marm05.txt')

text1

len(text1)


len(set(text1))

from nltk import ngrams, FreqDist

target_word = 'olhos'

fd = FreqDist(ng
    for ng in ngrams(text1, 5)
    if target_word in ng)

for hit in fd.samples():
    print(' '.join(hit))



#importar a cena dos corpus.
import nltk.corpus

#importar as palavras -> lista com as palavras.
nltk.corpus.mac_morpho.words()

#faz uma matriz, cada linha é uma frase.
nltk.corpus.mac_morpho.sents()


#lista de tuplos, segunda componente é o tipo do texto -> verbo, nome etc ...  
nltk.corpus.mac_morpho.tagged_words()


"""
    Este é importante -> gera a lista com os pares palavra, tipo gramtical
"""
nltk.corpus.mac_morpho.tagged_sents()

from nltk.corpus import floresta

#lista com todas as palavras
floresta.words()


#pares com o tipo grmatical
floresta.tagged_words()

def simplify_tag(t):
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t


#palavras gramaticais daqui
twords = floresta.tagged_words()    


"""
    Muito importante: aqui temos as cenas gramaticais

"""    

#gerar os tipos
twords = [(w.lower(), simplify_tag(t)) for (w,t) in twords]

print(' '.join(word + '/' + tag for (word, tag) in twords[:10]))

#listas de palavras da florestas
words = floresta.words()

#numero de palavras do texto.
len(words)

#cria um set que diz quantas vezes aparece uma dada palavra.
fd = nltk.FreqDist(words)
fd.max() #dizer a palavra que aparece mais vezes.

#basicamente diz todas as palavras e cenas assim 
tags = [simplify_tag(tag) for (word,tag) in floresta.tagged_words()]

#agora diz quantos há de cada tipo.
fd = nltk.FreqDist(tags)


fd.keys()[:20] # doctest: +NORMALIZE_WHITESPACE

#percorrer as frases
floresta.sents() # doctest: +NORMALIZE_WHITESPACE

#para cada frase dizer o tipo de cena gramatical dela
floresta.tagged_sents()

#faz a historia da gramatica, mas guarda em arvore.
# # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS

psents = floresta.parsed_sents()

#agora desenha a arvore com as palavras.
psents[5].draw() # doctest: +SKIP


import os, nltk.test

testdir = os.path.split(nltk.test.__file__)[0]

text = open(os.path.join(testdir, 'floresta.txt'), 'rb').read().decode('ISO 8859-1')

def concordance(word, context=30):
    for sent in floresta.sents():
        if word in sent:
            pos = sent.index(word)
            left = ' '.join(sent[:pos])
            right = ' '.join(sent[pos+1:])
            print('%*s %s %-*s' %
                (context, left[-context:], word, context, right[:context]))


concordance("dar")


from nltk.corpus import floresta

tsents = floresta.tagged_sents()
tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
train = tsents[100:]
test = tsents[:100]

tagger0 = nltk.DefaultTagger('n')

nltk.tag.accuracy(tagger0, test)

tagger1 = nltk.UnigramTagger(train, backoff=tagger0)

nltk.tag.accuracy(tagger1, test)

tagger2 = nltk.BigramTagger(train, backoff=tagger1)

nltk.tag.accuracy(tagger2, test)

sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')

raw_text = machado.raw('romance/marm05.txt')

sentences = sent_tokenizer.tokenize(raw_text)

for sent in sentences[1000:1005]:
    print("<<", sent, ">>")

import os, nltk.test

testdir = os.path.split(nltk.test.__file__)[0]

text = open(os.path.join(testdir, 'floresta.txt'), 'rb').read().decode('ISO-8859-1')

lines = text.split('\n')

train = ' '.join(lines[10:])

test = ' '.join(lines[:10])


stok = nltk.PunktSentenceTokenizer(train)

print(stok.tokenize(test))


stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')

nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()

stemmer.stem("copiar")

stemmer.stem("paisagem")

stopwords = nltk.corpus.stopwords.words('portuguese')

stopwords[:10]

fd = nltk.FreqDist(w.lower() for w in floresta.words() if w not in stopwords)

for word in list(fd.keys())[:20]:
    print(word, fd[word])




