from collections import defaultdict 
from operator import itemgetter 
from itertools import groupby 

"""
    Isto já gera um dicionario mas ainda é roto.
"""

bigram =[('casa', 'Maias'), ('habitar', 'Lisboa'), ('Lisboa', 'Outono'), ('Outono', '1875'),
         ('vizinhança', 'Rua'), ('Rua', 'S'), ('S', '.'), ('.', 'Francisco'), ('Francisco', 'Paula'),
          ('Paula', 'bairro'), ('bairro', 'Janelas'), ('Janelas', 'Verdes'), 
          ('Verdes', 'Casa'), ('Casa', 'Ramalhete'), ('Ramalhete', 'Ramalhete'),('Ramalhete', 'Ramalhete')]

trigram=[('Maias', 'vieram', 'habitar'), ('1875', 'era', 'vizinhança'),('joao','era','maria')]


"""
    Este acho que está pas.
"""
res_bi = dict((k, [v[1] for v in itr]) for k, itr in groupby( 
                                bigram, itemgetter(0)))

#print(str(dict(res_bi)))
print(res_bi)

"""
    Agora temos de criar um dicionario

    verbos[verbo]={in:palavra1 ,out:palavra2}
"""
#res_tri = defaultdict(list) 
#for i, j, k in trigram: 
#    res_tri[j].append(i)
#    res_tri[j].append(k)

#print(str(dict(res_tri)))
#print(res_tri)
"""
res_tri={}
for i in trigram:
    res_tri[i[1]]={'in_name':i[0],'out_name':i[2]}

print(res_tri)    
"""


res_tri = defaultdict(list) 
for i in trigram:
    res_tri[i[1]].append({'in_name':i[0],'out_name':i[2]})

print(dict(res_tri))  
