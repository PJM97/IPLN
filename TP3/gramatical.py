import nltk
from args import args_Parser
from pickle import load

texto = "um texto muito bonito"
matrix = [texto,texto,'nove é um numero',texto[:2]]

def getTagger():
    input = open('mac_morpho.pkl', 'rb')
    tagger = load(input)
    input.close()
    return tagger

def filterGrammer(grammar_Matrix,gram):
    #filter
    palavras = list(map(lambda y: list(filter(lambda x: x[1]==gram, y)),grammar_Matrix))
    #list
    return [item[0] for s in palavras for item in s]
    

def main():
    args=args_Parser()
    textm = list(map (lambda x: x.rsplit(),matrix))
    print(textm)
    tagger = getTagger()
    grammar_Matrix = list(map(tagger.tag,textm))
    print(grammar_Matrix)
    gram=args.word

    flat_list = filterGrammer(grammar_Matrix,gram)
    print(flat_list)

if __name__ == "__main__":
    main()   




 