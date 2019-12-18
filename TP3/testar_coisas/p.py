import re
from args import args_Parser
import sys 

texto = "um texto muito bonito"

matrix = [texto,texto,'9 9 9 9 9 9','numero 9 nove',texto[:2]]

def func(t,ar):
    regEx1=ar[0]
    regEx2=ar[1]
    regEx3=ar[2]
    p1 = re.compile(regEx1)
    p2 = re.compile(regEx2)
    p3 = re.compile(regEx3)
    for line in t:
        if(len(line)>=3):   #se tiver pelo menos 3 elms na linha
            for i in range(len(line)-2):    #variar até penultimas posições
                m1=p1.match(line[i])
                m2=p2.match(line[i+1])
                m3=p3.match(line[i+2])
                #se obtivemos resultado e dá match com a regex
                if(m1 and m2 and m3 and (m1.span()[1] == len(line[i])) and 
                    (m2.span()[1] == len(line[i+1])) and
                    (m3.span()[1] == len(line[i+2]))):
                    print("(",line[i],",",line[i+1],",",line[i+2],")")




def main():
    args=args_Parser()
    textm = list(map (lambda x: x.rsplit(),matrix))
    print(textm)
    func(textm,args.regex)

if __name__ == "__main__":
    main()       