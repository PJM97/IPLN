import nltk
import nltk.corpus

sentence = """Frase em portugues. Hoje comi bolinhos, estava muito bom."""

tokens = nltk.word_tokenize(sentence)

stopwords = nltk.corpus.stopwords.words('portuguese')

print(tokens)


tagged = nltk.pos_tag(tokens)

#tagged2=nltk.corpus.mac_morpho.tagged_words()

ola = nltk.corpus.mac_morpho.pos_tag()


print(tagged)

#cetem-publico
