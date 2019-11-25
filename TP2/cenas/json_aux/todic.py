from collections import defaultdict


bigram =[('casa', 'Maias'), ('habitar', 'Lisboa'), ('Lisboa', 'Outono'), ('Outono', '1875'),
         ('vizinhança', 'Rua'), ('Rua', 'S'), ('S', '.'), ('.', 'Francisco'), ('Francisco', 'Paula'),
          ('Paula', 'bairro'), ('bairro', 'Janelas'), ('Janelas', 'Verdes'), 
          ('Verdes', 'Casa'), ('Casa', 'Ramalhete'), ('Ramalhete', 'Ramalhete')]

trigram=[('Maias', 'vieram', 'habitar'), ('1875', 'era', 'vizinhança')]





test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')] 

print("The original list is : " + str(test_list)) 

res = defaultdict(list) 
"""
    ou seja, para a primeira componente da lista é como fosse key
    e como value metemos a segunda componente,
"""
for i, j in test_list: 
    res[i].append(j) 
print("The merged dictionary is : " + str(dict(res))) 




