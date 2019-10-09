from itertools import groupby
data = {('age', 'Low', 'Pos')  :    3 ,
        ('age', 'High', 'Pos')  :    11 ,
        ('age', 'Low', 'Neg')  :     8 ,
        ('age', 'High', 'Neg')  :    8 ,
        ('sex', 'male', 'Pos')  :    13 ,
        ('sex', 'female', 'Pos')  :  1 ,
        ('sex', 'male', 'Neg')  :    10 ,
        ('sex', 'female', 'Neg')  :  6}



def main():
    #print("ola")
    #
    #i


    #Este premite imprimir todo o dicionário.
    #print(data)

    sorted_keys = sorted(data.keys())

    #assim podemos imprimir todas as chaves.
    #print(sorted_keys)

    #index_groups = {k: list(m) for k, m in groupby(sorted_keys, lambda x: x[:2]}
    #print(index_groups)


if __name__ == "__main__":
    main()  
