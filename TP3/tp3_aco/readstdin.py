import fileinput

"""
Podemos correr, depois escrever .... e termina com ctrl d
Ou podemos < input.txt
"""
matrix = []
for line in fileinput.input():
    matrix.append(line)

print(matrix)    
