from pronto import *
import os
import csv

def create_file(path):
    f = open(path,"x")
    f.close(f)

onto_filename = "nomes.obo"
directory = "Pronto_Ontologies"
csv_filename = "nomes.csv"

onto = Ontology("Ontologies/nomes.obo")
print(list(onto.terms()))
print(list(onto.relationships()))

"""
#Finds path to current program
path = os.path.dirname(os.path.abspath(__file__))
#Checks if directory exists
if not os.path.exists(path+"/"+directory):
    os.makedirs(directory)
    print("Created directory!")
#Checks if file exists
if not os.path.exists(path+"/Ontologies/"+onto_filename):  
    create_file(path+"/Ontologies/"+onto_filename)
    print("Created file!")


with open(path+"/Ontologies/"+onto_filename,"wb") as f:
    onto.dump(f)"""
