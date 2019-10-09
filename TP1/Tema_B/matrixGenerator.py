from collections import Counter
import collections

#Funcao que dá a coluna.
def column(matrix, i):
    return [row[i] for row in matrix]


def matrixGen(mat,n):
    matrix={}
    #get first column
    column1=column(mat,0) 
    count=Counter(column1)
    sort= sorted(count.items(), key=lambda x: x[1], reverse=True)
    top=sort[:n]    #por enquanto para 3, mas depois o top é o valor passado pelo arg.

    #inicializar a matrix:
    for i in range(len(top)):
        matrix[top[i][0]]={}

    #popular a matriz
    for i in range(len(top)):
        for j in range(len(top)):
            if(i==j):
                matrix[top[i][0]][top[i][0]]=top[i][1]
            else:    
                matrix[top[i][0]][top[j][0]]=0
    
    column2=column(mat,1)  
    for i in range(len(top)):
        for j in range(len(column2)):
            matrix[top[i][0]][column2[j]]=0

    #calcular as ocorrencias.
    for i in range(len(mat)):
        matrix[mat[i][0]][mat[i][1]]+=1

    return(matrix)                


def main():
    #lista com as palavras separadas que temos como input.
    mat = [['um', 'lindo'], ['a', 'chegar'], ['muito', 'cansada'],
    ['a', 'chegar'], ['muito', 'doente'], ['um', 'pandemonio']]

    matrix=matrixGen(mat,3)
    print(matrix)

    
if __name__ == "__main__":
    main() 

