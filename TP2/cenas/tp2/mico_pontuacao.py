from nltk.tokenize import RegexpTokenizer
import nltk

tokenizer = RegexpTokenizer(r'\w+')
pas = tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')
#tokens = list(map(nltk.word_tokenize,pas))
dab=nltk.pos_tag(pas)

print(dab)

