from collections import Counter
import collections
# from prettytable import PrettyTable

#Funcao que dá a coluna.
def column(matrix, i):
    return [row[i] for row in matrix]

#Gerador da matriz de incidencia
def matrixGen(mat,n,ordem):
    matrix={}
    if(ordem=='B'):
        for i in range(len(mat)):
            mat[i]=mat[i][::-1]

     #get first column
    column1=column(mat,0) 
    # numero de ocorrencias da next word
    count=Counter(column1)

    #calcular o top n de elementos.
    sort= sorted(count.items(), key=lambda x: x[1], reverse=True)
    top=sort[:n]
    
    #inicializar a matrix de incidencia:
    for i in range(len(top)):
        matrix[top[i][0]]={}
    
    #povoar a matriz com a matriz identidade do proprio elemento
    for i in range(len(top)):
        for j in range(len(top)):
            if(i==j):
                matrix[top[i][0]][top[i][0]]=top[i][1]
            else:    
                matrix[top[i][0]][top[j][0]]=0

    #calcular as ocorrencias da next next word.
    column2=[]
    for i in range(len(top)):
        for j in range(len(mat)):
            if(top[i][0]==mat[j][0]):
                column2.append(mat[j][1])
    
    #povoação inicial da matriz para alem da identidade
    for i in range(len(top)):
        for j in range(len(column2)):
            matrix[top[i][0]][column2[j]]=0
    #get keys que interessam.
    topk=[i[0] for i in top]      

    #conver ter a matriz input em matriz de tuplos
    mattuples=[tuple(l) for l in mat]
    mattuples=[item for item in mattuples if item[0] in topk]
    
    #calcular as ocorrencias.
    for i in range(len(mattuples)):
        matrix[mattuples[i][0]][mattuples[i][1]]+=1
        
    #Return das keys dos elems do top  e a matriz de incidencia.
    return(topk,matrix)                
    
#Funcao para gerar o output.
def outputMaker(matrix,word,keys,n,ordem):
    output =[]
    s=[]

    #filtrar os elementos a imprimir(numero de ocorrencias >0)
    for i in matrix:
        for j in (matrix[i]):
            if(i==j):
                s.append(i+" "+"("+str(matrix[i][i])+")")
            else:
                 if(matrix[i][j]!=0 and ordem=='A'):
                    s.append(i+" "+j+" "+"("+str(matrix[i][j])+")") 
                 if(matrix[i][j]!=0 and ordem=='B'):
                       s.append(j+" "+i+" "+"("+str(matrix[i][j])+")") 
        output.append(s)
        s=[] 

    #Normalizar a matriz -> todas as linhas com o mesmo tamanho.
    maxLen = max(map(len, output))
    for row in output:
        i=len(row)
        if i < maxLen:
            while(i < maxLen):
                row.extend([' ' * (maxLen - len(row))])  
                i+=1

    #calculo da matriz transposta
    trans=list(map(list, zip(*output)))
    
    #Inserir a coluna com com a palavra procurada e o resto a vazio.
    trans[0].insert(0,word)

    for j in range(len(trans)):
        if(trans[j][0]!=word):
            trans[j].insert(0," ")

    print(trans)
    #Pretty printing -> é preciso a biblioteca 
    # p = PrettyTable()
    # for row in trans:
    #     p.add_row(row)
    # print(p.get_string(header=False, border=False))

