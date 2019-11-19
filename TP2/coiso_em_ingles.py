import nltk
from nltk.corpus import treebank
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('treebank')
#nltk.download('words')
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

#print(tokens)  #basicamente vai partir isto em palavras.

tagged = nltk.pos_tag(tokens)   # agora temos as palavras separadas por tokens.
#print(tagged)

entities = nltk.chunk.ne_chunk(tagged)

#print(entities)
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()