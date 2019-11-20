import nltk

corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(".", "input.txt")

print("ACCESSING PARAGRAPHS")

paragraphs=corpus.paras()

for p in paragraphs:
    print(p)

#raw_input()

print("ACCESSING SENTENCES")

sentences=corpus.sents()

for s in sentences:
    print(s)
    
#raw_input()

print("ACCESSING WORDS")

words=corpus.words()

for w in words:
    print(w)