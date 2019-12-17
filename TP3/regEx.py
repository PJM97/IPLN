import re

"""
    Ou seja isto dá match a tudo que quisermos, podemos apanhar uma regex
"""
#p = re.compile('[A-Z][a-z]+')
#p = re.compile(r'\w+')
#p = re.compile('Carlos')
#p = re.compile('Maria')

#print(p.match("")) #pra este caso imprime none

palavra = 'Carlos'
regEx= '[A-Z][a-z]+'
p = re.compile(regEx)
m = p.match(palavra)
if(m):
    print(len(palavra) == m.span()[1]) #na segunda componete é o length da palavra
else :
    print("vazio")

