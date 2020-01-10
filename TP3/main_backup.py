def main():
    args=args_Parser()  #obter as flags/respetivos argumentos
    tagger = getTagger() #obter gramatica

    if(args.input): #input file
        corpus=getFromOneFile(".",args.input)
        sent_Matrix=getSentenses(corpus)  
    else:   #stdin
        sent_Matrix = readStdIn()

    #grammar_Matrix = list(map(tagger.tag,sent_Matrix))
    #print(grammar_Matrix)



    #procurar algo gramatica, exemplo: python3 comando.py -i os_maias.txt -w N
    if(args.word):
        grammar_Matrix = list(map(tagger.tag,sent_Matrix))
        gw=filterGrammer(grammar_Matrix,args.word)
        for w in gw:
            print(w,"; ",end="")
        print("\n")
        exit(0)

 
    # >python3 comando.py -i os_maias.txt -r Carlos \\w+ \\w+
    if(args.regex):
        filterRegEx(sent_Matrix,args.regex)
        exit(0)

       


    """
        Estou aqui
    """
       
  
    grammar_Matrix = list(map(tagger.tag,sent_Matrix)) #matriz gramaticalmente notada

    if(args.nomes): #relações com todos os nomes
        filtered_gm=filterMatrix(grammar_Matrix)
        bigram = povoate_Bigrams(filtered_gm)

        if(args.graph): #caso gerar grafo output
            nomes_weight=weigthCounter(bigram)
            generateHTML(nomes_weight,args.graph)            

        if(args.output):    #guardar em ficheiro
            file = open(args.output,'w') 
            for l in bigram:
                file.write(str(l))
            file.close()        
        else:    #stdout
            print(bigram) 
        
    elif(args.verbs):   #trigramas de palavra-verb-palavra
            filtered_gm=filterMatrix(grammar_Matrix)
            trigram = povoate_Trigrams(filtered_gm)
            
            if(args.graph): #caso de gerar grafo
                tri_two=tritotow(trigram)
                verbs_weight=weigthCounter(tri_two)
                generateHTML(verbs_weight,args.graph)
            if(args.output):
                file = open(args.output,'w') 
                for l in trigram:
                    file.write(str(l))
                file.close()        
            else:
                print(trigram)

    elif(args.palavra):
            filtered_gm=filterMatrix(grammar_Matrix) 
            tri_palavra = wordRelation(args.palavra,filtered_gm)

            if(args.graph):
                tri_two_palavra=tritotow(tri_palavra)
                verbs_weight_palavra=weigthCounter(tri_two_palavra)
                generateHTML(verbs_weight_palavra,args.graph)

            if(args.output):
                file = open(args.output,'w')
                for l in tri_palavra:
                    file.write(str(l))
                file.close()        
            else:
                print(tri_palavra) 
           
  
    
if __name__ == "__main__":
    main()    
