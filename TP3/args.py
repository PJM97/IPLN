import argparse
def args_Parser():
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    parser.add_argument("-i","--input",help="Ficheiro input para processar")
    parser.add_argument("-o","--output", help="Indicar o ficheiro output")
    parser.add_argument("-g","--graph", help="Gerar grafo com as relações")

    #Opções mutuamente exclusivas: invocação simultânea iria produzir multiplos resultados misturados
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbs",action='store_true', help="Indicar relações centradas em verbos")
    group.add_argument("-n","--nomes",action='store_true', help="Indicar relações com nomes")
    group.add_argument("-r","--regex",nargs=3,help="Filtro de triplos de relações com expressões regulares")
    group.add_argument("-w","--word", help="Encontrar todas as palavras com um dado valor gramatical")
    group.add_argument("-p","--palavra", help="Indicar relações com palavra passada por argumento")
    
    return parser.parse_args()


def main():
    args_Parser()
    
    
if __name__ == "__main__":
    main() 