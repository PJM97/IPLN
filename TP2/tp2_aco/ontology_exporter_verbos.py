from owlready2 import *
import os
import csv

def create_file(path):
    f = open(path,"x")
    f.close()

def create_phrase(nv,vn,phrase_name):
    #Creates a new phrase (Phrases are unique so it doesn't matter if you don't append)
    phrase_ind = Phrase(phrase_name)

    #Allocates the Names, Verb and weight as properties of Phrase
    phrase_ind.name_verb = [nv]
    phrase_ind.snd_name = [vn]

    return phrase_ind

def create_name_verb(name,verb,weight):
    #Creates a new phrase (Phrases are unique so it doesn't matter if you don't append)
    name_verb_ind = Name_Verb(name+"_"+verb)
    name_ind = create_name(name)
    verb_ind = create_name(verb)

    #Allocates the Names, Verb and weight as properties of Phrase
    name_verb_ind.fst_name = [name_ind]
    name_verb_ind.verb_nv = [verb_ind]
    name_verb_ind.weight_nv = [weight]

    #Two-Way Relationship
    #Allocates the verb to the names
    name_ind.has_verb.append(verb_ind)

    #Allocates the names to the verb
    verb_ind.has_name.append(name_ind)

    return name_verb_ind

def create_verb_name(verb,name,weight):
    #Creates a new phrase (Phrases are unique so it doesn't matter if you don't append)
    verb_name_ind = Verb_Name(verb+"_"+name)
    verb_ind = create_name(verb)
    name_ind = create_name(name)

    #Allocates the Names, Verb and weight as properties of Phrase
    verb_name_ind.verb_vn = [verb_ind]
    verb_name_ind.snd_name = [name_ind]
    verb_name_ind.weight_nv = [weight]

    #Two-Way Relationship
    #Allocates the verb to the names
    name_ind.has_verb.append(verb_ind)

    #Allocates the names to the verb
    verb_ind.has_name.append(name_ind)

    return verb_name_ind


def create_name(name):
    name_individual = Name(name)
    return name_individual

def create_verb(verb):
    verb_individual = Verb(verb)
    return verb_individual

def save_ontology(onto):
    onto.save()

###############ALTERAR PARSE_TYPE#######################
onto_filename = "verbos.obo"
directory = "Ontologies/"

csv_filename = "verbs.csv"

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

#Creates classes for parsing
with onto:
    class Word(Thing): pass
    class Name(Word): pass
    class Verb(Word): pass
    class Phrase(Thing): pass
    class Name_Verb(Phrase): pass
    class Verb_Name(Phrase): pass
    #Properties of Phrase
    class name_verb(Phrase >> Name_Verb): pass
    class verb_name(Phrase >> Verb_Name): pass
    #Properties of Name_Verb
    class fst_name(Name_Verb >> Name): pass
    class verb_nv(Name_Verb >> Verb): pass
    class weight_nv(Name_Verb >> int): pass
    #Properties of Verb_Name
    class verb_vn(Verb_Name >> Verb): pass
    class snd_name(Verb_Name >> Name): pass
    class weight_vn(Verb_Name >> int): pass
    #Properties of Name
    class has_verb(Name >> Verb): pass
    #Properties of Verb
    class has_name(Verb >> Name): pass

#Iterates over csv file
with open(path+"/"+csv_filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in reader:
        if line_count != 0:
            if line_count%2 == 1:
                fst_name = row[0]
                verb = row[1]
                weight = row[2]
                nv = create_name_verb(fst_name,verb,weight)
            else:
                verb = row[0]
                snd_name = row[1]
                weight = row[2]
                vn = create_verb_name(verb,snd_name,weight)
                create_phrase(nv,vn,fst_name+"_"+verb+"_"+snd_name)

        line_count+=1

save_ontology(onto)

############# EXEMPLOS ##############
print(list(Word.subclasses()))
print(Name.is_a)
print(Name.has_verb)