import argparse
def args_Parser():
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    parser.add_argument("-i","--input",help="Ficheiro input para processar")
    parser.add_argument("-o","--output", help="Indicar o ficheiro output")

    """
    Ainda tenho de ver as opções que fazem sentido com geração de grafos
    """
    parser.add_argument("-g","--graph", help="Gerar grafo com as relações")


    """
    Indicar opções mutuamente exclusivas,
    ou seja, invocação simultaniamente que produz multiplos outputs.
    """
    group = parser.add_mutually_exclusive_group()
    group1 = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbs",action='store_true', help="Indicar relações com verbos")
    group.add_argument("-n","--nomes",action='store_true', help="Indicar relações com nomes")


    #group1.add_argument("-n","--nomes",action='store_true', help="Indicar relações com nomes")
    #group1.add_argument("-g","--graph", help="Gerar grafo com as relações")

    group.add_argument("-r","--regex",nargs=3,help="Ficheiro input para processar")
    group.add_argument("-w","--word", help="Encontrar todas as palavras com um dado valor gramatical")
    group.add_argument("-p","--palavra", help="Indicar relações com esta palavra")  


    return parser.parse_args()


def main():
    args_Parser()
    
    
if __name__ == "__main__":
    main() 