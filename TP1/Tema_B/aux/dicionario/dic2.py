from collections import defaultdict
import pprint


'''
Temos aqui o dicionario, onde a chave é um triplo
'''

data = {
    ('age', 'Low', 'Pos')  :    3 ,
    ('age', 'High', 'Pos')  :    11 ,
    ('age', 'Low', 'Neg')  :     8 ,
    ('age', 'High', 'Neg')  :    8 ,
    ('sex', 'male', 'Pos')  :    13 ,
    ('sex', 'female', 'Pos')  :  1 ,
    ('sex', 'male', 'Neg')  :    10 ,
    ('sex', 'female', 'Neg')  :  6
}



def main():
    #assim permite criar uma lista.
    prefix2 = defaultdict(list)


    for tuple_key in data:  #Em tuple_keys temos os triplos das chaves.
        #fica como key os 2 primeiros do tuplo e como value os triplos.
        prefix2[tuple_key[:2]].append(tuple_key)

    pprint.pprint(dict(prefix2))




if __name__ == "__main__":
    main()  

