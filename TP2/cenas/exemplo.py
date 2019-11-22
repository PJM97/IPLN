import pronto
import sys


"""
def getFile():
    try:
        
         ms = pronto.Ontology.from_obo_library("ms.obo")
         print("ok")
    except:
        sys.exit("Erro na abertura do ficheiro input")   
    return ms     
"""

def main():
    #ms=getFile()
    ms = pronto.Ontology.from_obo_library("ms.obo")
    instruments = set(ms['MS:1000031'].subclasses())

    data = []
    for term in instruments:
        value = {"id": int(term.id[3:]), "name": term.id, "desc": term.name}
        parents = instruments.intersection(term.relationships.get(ms['is_a'], set()))
        if parents:
            value['parent'] = int(parents.pop().id[3:])
        data.append(value)
    
    for a in data:
        print(a)
        
if __name__ == "__main__":
    main()        