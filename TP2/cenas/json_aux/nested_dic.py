# Creating an empty Dictionary 
"""
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
  
# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 
"""

dab={}

trigram=[('Maias', 'vieram', 'habitar'), ('1875', 'era', 'vizinhança')]

for i in trigram:
    dab[i[1]]={'in_name':i[0],'out_name':i[2]}

print(dab)

