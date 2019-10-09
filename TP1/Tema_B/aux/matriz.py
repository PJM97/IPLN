import sys
import re


s1="um lindo"
s2="a chegar"
s3="muito cansada"
s4="a chegar"
s5="muito doente"
s6="um pandemonio"



mat=[s1,s2,s3,s4,s5,s6]

def main():
  
    #for i in range(len(mat)):
    #    mat[i]=re.split(r"\s",mat[i])

    #for i in range(len(mat)):
    #    print(mat[i])

    myDic={}
    myDic[("ola","xau")]=0
    myDic[("ola","adeus")]=1
    myDic[("ola","dab")]=3
    myDic[("nada","haver")]=69

    #for i in range(myDic.keys()):
    #    print(myDic[i])

    #for x in myDic:
    #    print(x.value())



if __name__ == "__main__":
    main()  