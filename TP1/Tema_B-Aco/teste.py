

def main():
    mat = [['um', 'lindo'], ['a', 'chegar'], ['muito', 'cansada'],
            ['a', 'chegar'], ['muito', 'doente'], ['um', 'pandemonio']]

    for i in range(len(mat)):
        mat[i]=mat[i][::-1]
    print(mat)    
if __name__ == "__main__":
    main()         