"""
Exemplos das cenas de pl.
"""
from nltk.examples.pt import *
import nltk
nltk.download()
from nltk.book import *

#pra ver o moby dick
text1

#ver a ocorrencia de uma palavra com contexto -> aparece ela no meio de uma frase
text1.concordance("monstrous")

#ver palavras que aparecem no mesmo contexto que a palavra referida
text1.similar("monstrous")



#basicamente desenhar um grafico com a disperção de ocorrencias destas palavras.
#Tipo em que zonas de toda a obra elas aparecem mais.
from nltk.book import *
import matplotlib
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])


#contar o # de palavras de um texto.
len(text3)

#definir uma lista.
sent1 = ['Call', 'me', 'Ishmael', '.']
sent1
len(sent1)
 	
#percentagem de palavras nao repetidas sobre o total 
def lexical_diversity(text):
	return len(set(text)) / len(text)

lexical_diversity(sent1)
sent2
sent3
['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']

#concatenar listas
sent4 + sent1

#concatenar no fim da lista
sent1.append("Some")

#ver o conteudo numa dada posicao
text4[173]

#indice de um dado elemento.
text4.index('awaken')

#elementos entre dois indices.
ext5[16715:16735]
text5[16715:16735]

#definir uma sentence
sent = ['word1', 'word2', 'word3', 'word4', 'word5',
...         'word6', 'word7', 'word8', 'word9', 'word10']
sent = ['word1', 'word2', 'word3', 'word4', 'word5','word6', 'word7', 'word8', 'word9', 'word10']
sent
sent[0]
sent[9]
sent[5:8]
sent[:3]
text2[141525:]
sent
sent[0]= 'First'
sent
sent1 = ['Call', 'me', 'Ishmael', '.']
sent1
#nova lista
my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode',
'forth', 'from', 'Camelot', '.']
noun_phrase = my_sent[1:4]
noun_phrase
saying = ['After', 'all', 'is', 'said', 'and', 'done',
'more', 'is', 'said', 'than', 'done']

#converter uma lista num set.
tokens = set(saying)

#ordenar.
tokens = sorted(tokens)
#devolve um objeto todo manhoso com as # de ocorrencias.
fdist1 = FreqDist(text1)
fdist1
fdist1.most_common(50)
fdist1
type(fdist1)
text1
type(text1)

#set do texto 1
V = set(text1)

# buscar as palavras de comprimento superior a 15
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)


#gera lista de tuplos com as palavras daqui.
list(bigrams(['more', 'is', 'said', 'than', 'done']))
text4.collocations()
sent7
[w for w in sent7 if len(w) < 4]
sorted(w for w in set(text1) if w.endswith('ableness'))


import sys
export('history', 'interactions.py')
quit()

#####################################
"""

			Capitulo 2


"""
#####################################
import nltk
#para buscar o corpo de um ficheiro.

#lista com o nome de todos os ficheiros.
nltk.corpus.gutenberg.fileids()

#buscar o conteudo do primeiro ficheiro.
"""
	Aqui abre o ficheiro e coloca e coloca numa lista
	de palavras.
"""
emma = nltk.corpus.gutenberg.words('austen-emma.txt')

# numero de palavras do ficheiro.
len(emma)


from nltk.corpus import gutenberg


#buscar os nomes do ficheiros(lista).
"""
	Lista com os nomes dos ficheiros input.
"""
gutenberg.fileids()

#buscar o conteudo deste ficheiro.
emma = gutenberg.words('austen-emma.txt')


import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)

#penso que assim primeiro passa para texto e só depois é que executa.
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

emma.concordance("surprize")


from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')


#atravessa cada nome dos ficheiros e vai buscar a info de cada um destes.
for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid))
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
	print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)




"""
	Buscar as frases de um ficheiro
"""
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]

#vai buscar o comprimento da frase mais comprida.
longest_len = max(len(s) for s in macbeth_sentences)
#obter a frase com maior comprimento de todas
[s for s in macbeth_sentences if len(s) == longest_len]



"""
	Da cena de web qualquer coisa.
"""
from nltk.corpus import webtext
for fileid in webtext.fileids():
	print(fileid, webtext.raw(fileid)[:65], '...')
from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]


"""
	Isto brown é uma cambada de texto da universidade brown, 
	caracterizado e assim. News sources etc ....
"""
from nltk.corpus import brown

#listar as categorias
brown.categories()

#coisas da categoria news.
brown.words(categories='news')


brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])



from nltk.corpus import brown

#ficheiros de news.
news_text = brown.words(categories='news')

#frequencia distributiva destas palavras.
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
	print(m + ':', fdist[m], end=' ')


#gerar pares de frequencias.	
cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
#para agora desenhar a tabela com esses pares.
cfd.tabulate(conditions=genres, samples=modals)

#routers é um file com mihloes de palavras.

from nltk.corpus import reuters
reuters.categories(['training/9865', 'training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley', 'corn'])
 reuters.words('training/9865')[:14]
reuters.words('training/9865')[:14]
reuters.words(['training/9865', 'training/9880'])
reuters.words(categories='barley')
reuters.words(categories=['barley', 'corn'])



"""
	1.5
"""
from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]
cfd = nltk.ConditionalFreqDist(
	(target, fileid[:4])
	for fileid in inaugural.fileids()
	for w in inaugural.words(fileid)
	for target in ['america', 'citizen']
	if w.lower().startswith(target))
cfd.plot()

"""
1.6
"""
nltk.corpus.cess_esp.words()



import nltk
nltk.download('cess_esp')
nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words()
nltk.download('floresta')
nltk.corpus.floresta.words()

#em indiano
nltk.corpus.indian.words('hindi.pos')
nltk.download('indian')
nltk.corpus.indian.words('hindi.pos')
nltk.corpus.udhr.fileids()
#japones roto
nltk.corpus.udhr.words('Javanese-Latin1')[11:]




#Universal Declaration of Human Rights(udhr)
from nltk.corpus import udhr

#uma cambada de linguas.
languages = ['Chickasaw', 'English', 'German_Deutsch',
'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']



cfd = nltk.ConditionalFreqDist(
	(lang, len(word))
	for lang in languages
	for word in udhr.words(lang + '-Latin1'))

#fazer o grafico.	
cfd.plot(cumulative=True)



#buscar o ficheiro
raw = gutenberg.raw("burgess-busterbrown.txt")
raw[1:20] #isto é o texto todo -> logo isto vai aparecer as primeiras 20 letras.
words = gutenberg.words("burgess-busterbrown.txt")
words[1:20]

#agora vamos buscar por frases
sents = gutenberg.sents("burgess-busterbrown.txt")
sents[1:20] #logo isto sao as primeiras 20 frases


#load do nosso
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict' #diretoria onde está o ficheiro
wordlists = PlaintextCorpusReader(corpus_root, '.*')

#agora temos o nome de todos os ficheiros.
wordlists.fileids()
wordlists.words('connectives')
from nltk.corpus import BracketParseCorpusReader
corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
file_pattern = r".*/wsj_.*\.mrg"



ptb = BracketParseCorpusReader(corpus_root, file_pattern)




"""
	2.2
"""
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))



genre_word = [(genre, word)
	for genre in ['news', 'romance']
	for word in brown.words(categories=genre)]



len(genre_word)
genre_word[:4]
genre_word[-4:]
cfd = nltk.ConditionalFreqDist(genre_word)
cfd.conditions()
print(cfd['news'])
print(cfd['romance'])
cfd['romance'].most_common(20)
cfd['romance']['could']

"""
2.3
"""
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
	(target, fileid[:4])
	for fileid in inaugural.fileids()
	for w in inaugural.words(fileid)
	for target in ['america', 'citizen']
	if w.lower().startswith(target))


from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
	(lang, len(word))
	for lang in languages
	for word in udhr.words(lang + '-Latin1'))
	#desenhar uma tabela
cfd.tabulate(conditions=['English', 'German_Deutsch'],
	samples=range(10), cumulative=True)



"""
	2.4
"""
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven',
'and', 'the', 'earth', '.']
list(nltk.bigrams(sent))
	
def generate_model(cfdist, word, num=15):
	for i in range(num):
		print(word, end=' ')
		word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
cfd['living']
generate_model(cfd, 'living')




"""
		3.2

"""
from __future__ import division
def lexical_diversity(text):
	return len(text) / len(set(text))
def lexical_diversity(my_text_data):
	word_count = len(my_text_data)
	vocab_size = len(set(my_text_data))
	diversity_score = vocab_size / word_count
	return diversity_score
from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
lexical_diversity(kjv)



def plural(word):
	if word.endswith('y'):
		return word[:-1] + 'ies'
	elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
		return word + 'es'
	elif word.endswith('an'):
		return word[:-2] + 'en'
	else:
		return word + 's'
plural('fairy')
plural('woman')

plural('wish')
plural('fan')

"""
	4.1
"""
def unusual_words(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab - english_vocab
	return sorted(unusual)

unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
unusual_words(nltk.corpus.nps_chat.words())
from nltk.corpus import stopwords
stopwords.words('english')


def content_fraction(text):
	stopwords = nltk.corpus.stopwords.words('english')
	content = [w for w in text if w.lower() not in stopwords]
	return len(content) / len(text)


content_fraction(nltk.corpus.reuters.words())


puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
[w for w in wordlist if len(w) >= 6
	and obligatory in w
	and nltk.FreqDist(w) <= puzzle_letters]

names = nltk.corpus.names


names.fileids()
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]


cfd = nltk.ConditionalFreqDist(
(fileid, name[-1])
for fileid in names.fileids()
for name in names.words(fileid))
cfd.plot()

"""
	4.2
"""
entries = nltk.corpus.cmudict.entries()
len(entries)
for entry in entries[42371:42379]:
	print(entry)


for word, pron in entries:
	if len(pron) == 3:
		ph1, ph2, ph3 = pron
	if ph1 == 'P' and ph3 == 'T':
		print(word, ph2, end=' ')


syllable = ['N', 'IH0', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]



[w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n']
sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n'))


def stress(pron):
	return [char for phone in pron for char in phone if char.isdigit()]
[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]
[w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]


p3 = [(pron[0]+'-'+pron[2], word)
for (word, pron) in entries
if pron[0] == 'P' and len(pron) == 3]
p3
cfd = nltk.ConditionalFreqDist(p3)
for template in sorted(cfd.conditions()):
	if len(cfd[template]) > 10:
		words = sorted(cfd[template])
		wordstring = ' '.join(words)
		print(template, wordstring[:70] + "...")

		
prondict = nltk.corpus.cmudict.dict()
prondict['fire']
prondict['blog']
prondict['blog'] = [['B', 'L', 'AA1', 'G']]
prondict['blog']
text = ['natural', 'language', 'processing']
[ph for w in text for ph in prondict[w][0]]
fr2en = swadesh.entries(['fr', 'en'])
quit()
