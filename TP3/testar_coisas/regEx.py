import re
from args import args_Parser
import sys 
import os
from pickle import load
"""
    Ou seja isto dá match a tudo que quisermos, podemos apanhar uma regex
"""


def func(args):
    palavra="Carlos"
    print(args[0])
    regEx=args[0]
    print(regEx)
    p = re.compile(regEx)
    m=p.match(palavra)
    if(m):
        print(m.span())

def main():
    args= args_Parser()
    func(args.regex)
if __name__ == "__main__":
    main()      

