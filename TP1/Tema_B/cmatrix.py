#!/usr/bin/env python3
import sys
import re
import matrixGenerator as m



#Funcao faz o parse e valida se todos os args passados são validos
def validInput():
    validArgC()
    return(getOrdem(),getNumber(),getWord(),getInputFile())

#se o numero de args nao for valido acabar logo.
def validArgC():
    if(len(sys.argv)!= 5):
        sys.exit("Invalid number of arguments")

#Só podemos ter After ou Before
def getOrdem():
    if(not (sys.argv[1]=="-A" or sys.argv[1]=="-B")):
        sys.exit("Invalid order option: -A for After or -B for Before")      
    return(sys.argv[1][1:])

#parse do tamanho da rede a comparar 
def getNumber():
    p=re.compile(r'[\d]+')
    if(not p.match(sys.argv[2])):
        sys.exit("Invalid order number") 
    return(sys.argv[2])

#parse da word a comparar
'''
Penso que esta RegEx nao está a 100%
'''
def getWord():
    # p=re.compile(r'[a-zA-Z]+')
    # p = re.sub(r"[a-zA-Z]+",sys.argv[3])
    if(not isValidWord(sys.argv[3])):
        # print(str(sys.argv[3]))
        sys.exit("Invalid word")
    return(sys.argv[3])

#Parse do input file fd    
def getInputFile():
    try:
        fd=open(sys.argv[4], "r")
    except:
        sys.exit("Invalid input file")
    return(fd)

'''
Não está a 100%. Temos de arrumar pontos e assim.
'''
def wordParser(fd):
    text=fd.read()
    return(re.split(r"[\ \n]", text))
  
def loadMatrix(w,wl):
    # print("Funcao para povoar a matriz")
    l=[]
    r=[]
    k=0
    w=extractValidWord(w)
    if(sys.argv[1]=="-B"):
    	k1=""
    	k2=""
    	k3=""
    	for i in wl:
    		if(k3==""):
    			k3=k2
    			k2=k1
    			k1=i
    		else:
    			if(extractValidWord(i)==w):
    				r.append([k1,k2])
    		k3=k2
    		k2=k1
    		k1=i

    else:	
	    for i in wl:
	        if(k>=1):
	            if(isEndOfSentence(i)):
	                l.append(extractValidWord(i))
	                if(k==1):l.append(extractValidWord(i))
	                k=3
	            else:
	                l.append(extractValidWord(i))
	                k+=1
	            if(k==3):
	                k=0;
	                r.append(l)
	                l=[]
	        if(extractValidWord(i)==w): k=1

    return r

def isValidWord(w):
    return 0<len(w)==len((re.findall(r'[\w]+',w))[0])

def isEndOfSentence(w):
    return len(re.findall(r'[\.\n]+',w))>0

def extractValidWord(w):
    r = re.findall(r'[\w]+',w)
    return r[0] if len(r)>0 else []

def outputMaker():
    print("Funçao que vai atravessar a estrutura e criar o output")

def main():
    ordem,number,word,fd=validInput()
    #print("order: ",ordem)
    wordList = wordParser(fd)
   # print("\n",wordList,"\n")
    mat=loadMatrix(word,wordList)
    #print(mat)
    #Caso de nao haver match:
    if(len(mat)==0):
        sys.exit("No match found")

    #m.matrixGen(mat,int(number))

    keys,matrix=m.matrixGen(mat,int(number),ordem)
    m.outputMaker(matrix,word,keys,int(number),ordem)

    #outputMaker()

if __name__ == "__main__":
    main()    