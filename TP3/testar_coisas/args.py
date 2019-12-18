import argparse
def args_Parser():
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    parser.add_argument("-i","--input",help="Ficheiro input para processar")
    parser.add_argument("-r","--regex",nargs=3,help="Ficheiro input para processar")
    parser.add_argument("-g","--graph", help="Gerar grafo com as relações")
    parser.add_argument("-o","--output", help="Indicar o ficheiro output")
    parser.add_argument("-v","--verbs",action='store_true', help="Indicar relações com verbos")
    parser.add_argument("-n","--nomes",action='store_true', help="Indicar relações com nomes")
    parser.add_argument("-p","--palavra", help="Indicar relações com esta palavra")
    return parser.parse_args()


 