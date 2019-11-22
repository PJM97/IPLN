import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = 'newcorpus/' # Directory of corpus.


newcorpus = PlaintextCorpusReader(corpusdir, '.*')

print(type(newcorpus))


#print(newcorpus)
#print(type(newcorpus))
