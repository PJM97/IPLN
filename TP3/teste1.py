import re

string = "1996"
b= False 

if(re.match(r"^([A-Z][a-z])+"),string):
    b=True

print(b)    


