import argparse

def args_Parser():
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    parser.add_argument("-v","--verbosity", help="increase output verbosity")
    parser.add_argument("-i","--input",help="input file")
    parser.add_argument("-g","--graph", help="Generate output File")
    parser.add_argument("-o","--output", help="Indicar o ficheiro output opnd")
    return parser.parse_args()

"""
#Depois aqui indicamos que caminho seguir na execução.
if args.file:
    print ("verbosity turned on")

print(args.output)
teste = parser.parse_args()

#print(args.verbosity)
#print(args.file)
"""
def main():
    args= args_Parser()
    if(args.verbosity):
        print(args.verbosity)
    else:
        print("flag nao foi passada")   

    print(args.input)

if __name__ == "__main__":
    main()       
