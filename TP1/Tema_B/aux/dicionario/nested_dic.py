

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

matriz = {'um': {'um' : 2, 'a':0,'muito':0,'lindo':1,'chegar':0,'cansada':0,'doente':0,'pandemonio':1},
            'a': {'um' : 0, 'a':2,'muito':0,'lindo':0,'chegar':2,'cansada':0,'doente':0,'pandemonio':0},
            'muito': {'um' : 0, 'a':0,'muito':2,'lindo':0,'chegar':0,'cansada':1,'doente':1,'pandemonio':1},
            }


def main():
    print(matriz['um']['um'])
    print(matriz['a']['a'])
    print(matriz['muito']['muito'])
    print(matriz['um'])
    print(len(matriz))
    print(len(matriz['um']))
    print("Testar coisas para imprimir")


if __name__ == "__main__":
    main()  