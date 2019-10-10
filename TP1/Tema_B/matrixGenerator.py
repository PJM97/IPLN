from collections import Counter
import collections
# from prettytable import PrettyTable

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
    #print(top)
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

    return([i[0] for i in top],matrix)                

def outputMaker(matrix,word,keys,n):
    output =[]
    s=[]
    #s.append(word)
    for i in matrix:
        for j in (matrix[i]):
            if(i==j):
                s.append(i+" "+"("+str(matrix[i][i])+")")
               # s.append("(")
             # print(i,"(",matrix[i][i],")")
            else:
                 if(matrix[i][j]!=0):
                    #print(i,j,"(",matrix[i][j],")")  
                    s.append(i+" "+j+" "+"("+str(matrix[i][j])+")") 
        output.append(s)
        s=[] 

    maxLen = max(map(len, output))
    for row in output:
        i=len(row)
        if i < maxLen: 
            #row.insert(0,' ')
            #i+=1
            while(i < maxLen):
                row.extend([' ' * (maxLen - len(row))])  
                i+=1

    trans=list(map(list, zip(*output)))
    
    leng=len(trans[0])

    trans[0].insert(0,word)

    i=1
    while(i<leng):
        trans[i].insert(0," ")
        i+=1
    print(trans)
    #print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in trans]))
    
    # p = PrettyTable()
    # for row in trans:
    #     p.add_row(row)


    # print(p.get_string(header=False, border=False))

'''
def main():
    word='está'
    
    #lista com as palavras separadas que temos como input.
    mat = [['um', 'lindo'], ['a', 'chegar'], ['muito', 'cansada'],
    ['a', 'chegar'], ['muito', 'doente'], ['um', 'pandemonio']]
    n=3
    keys,matrix=matrixGen(mat,n)
    #print(matrix)
    outputMaker(matrix,word,keys,n)

if __name__ == "__main__":
    main() 
'''
