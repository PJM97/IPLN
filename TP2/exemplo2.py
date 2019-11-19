import pronto
import sys
import json
import urllib.request
from vega import Vega


def main():

    ms = pronto.Ontology.from_obo_library("ms.obo")
    instruments = set(ms['MS:1000031'].subclasses())

    data = []
    for term in instruments:
        value = {"id": int(term.id[3:]), "name": term.id, "desc": term.name}
        parents = instruments.intersection(term.relationships.get(ms['is_a'], set()))
        if parents:
            value['parent'] = int(parents.pop().id[3:])
        data.append(value)
    
    #for a in data:
    #    print(a)

    print("dab")  
    #view = json.load(urllib.request.urlopen("https://github.com/vega/vega/blob/master/docs/examples/radial-tree-layout.vg.json"))

    with open("radial-tree-layout.vg.json", "r") as read_file:
        view = json.load(read_file)
    # First replace the default data with our own
    view['data'][0].pop('url')
    view['data'][0]['values'] = data
    view['marks'][1]['encode']['enter']['tooltip'] = {"signal": "datum.desc"}
    view['signals'][4]['value'] = 'cluster'
    #r= 
    r=Vega(view)
    print(r)
    #print("dab")

if __name__ == "__main__":
    main() 