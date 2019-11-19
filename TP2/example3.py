import pronto


def main():
    ms = pronto.Ontology.from_obo_library("ms.obo")
    print(len(ms))
    print(len(ms.terms()))
    print(len(ms.relationships()))
    
if __name__ == "__main__":
    main() 