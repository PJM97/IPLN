import argparse
def args_Parser():
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    parser.add_argument("-i","--input",help="input file")
    parser.add_argument("-g","--graph", help="Generate output File")
    parser.add_argument("-o","--output", help="Indicar o ficheiro output")
    parser.add_argument("-v","--verbs", help="Indicar relações com verbos")
    parser.add_argument("-n","--nomes", help="Indicar relações com nomes")
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
     
