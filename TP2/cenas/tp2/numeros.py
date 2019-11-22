test_list = ['A', 'casa', 'que', 'os', 'Maias', 'vieram', 'habitar', 'em', 'Lisboa', ',', 'no', 'Outono', 'de', '1875', ',', 'era', 'conhecida', 'na',
 'vizinhança', 'da', 'Rua', 'de', 'S', '.', 'Francisco', 'de', 'Paula', ',', 'e', 'em', 'todo', 'o', 'bairro', 'das', 'Janelas', 'Verdes',
 ',', 'pela', 'Casa', 'do', 'Ramalhete', ',', 'ou', 'simplesmente', 'o', 'Ramalhete', '.']

#[1, 4, 5, 6, 4, 5, 6, 5, 4] 

print("The original list : " + str(test_list)) 

size = len(test_list) 
idx_list = [idx + 1 for idx, val in
            enumerate(test_list) if val == ','] 



res = [test_list[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))] 
  
# print result 
print("The list after splitting by a value : " + str(res))


