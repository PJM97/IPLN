#!/usr/bin/env python3
import sys
import re

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
    if(len((re.findall(r'[\w]+',sys.argv[3]))[0]) != len(sys.argv[3])):
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
    return(re.split(r"[\ .,;]", text))
  
def loadMatrix(w,wl):
    # print("Funcao para povoar a matriz")
    l=[]
    r=[]
    k=0
    for i in wl:
    	if(k>=1):
    		l.append(i)
    		k+=1
    		if(k==3):
    			k=0;
    			r.append(l)
    			l=[]
    	if(i==w): k=1

    return r



def outputMaker():
    print("Funçao que vai atravessar a estrutura e criar o output")

def main():
    ordem,number,word,fd=validInput()
    wordList = wordParser(fd)
    print(wordList)
    


    print(loadMatrix(word,wordList))
    #outputMaker()

if __name__ == "__main__":
    main()    