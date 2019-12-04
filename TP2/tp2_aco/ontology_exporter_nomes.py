from owlready2 import *
import os
import csv

def create_file(path):
    f = open(path,"x")
    f.close()

def create_group(name1,name2,weight):
    group = Group(name1+"_"+name2)
    name1_ind = create_name(name1)
    name2_ind = create_name(name2)
    group.name_1 = [name1_ind]
    group.name_2 = [name2_ind]
    group.weight = [weight]

    return group

def create_name(name):
    name_individual = Name(name)
    return name_individual

def save_ontology(onto):
    onto.save()


onto_filename = "nomes.obo"
directory = "Ontologies/"
csv_filename = "nomes.csv"

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
#Loads ontology
onto = get_ontology("file://"+path+"/Ontologies/"+onto_filename).load()

with onto:
    class Word(Thing): pass
    class Name(Word): pass
    class Group(Thing): pass
    #Properties of Group
    class name_1(Group >> Name): pass
    class name_2(Group >> Name): pass
    class weight(Group >> int): pass


#Iterates over csv file
with open(path+"/"+csv_filename) as csv_file:
    
    reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in reader:
        if line_count != 0:
            name1 = row[0]
            name2 = row[1]
            weight = row[2]
            create_group(name1,name2,weight)
        line_count+=1

save_ontology(onto)

############# EXEMPLOS ##############
print(list(Word.subclasses()))
print(list(onto.classes()))
print(list(onto.individuals()))