"""
Ngrams - Calculate ngrams frequency
"""

import re
import subprocess
import sys
from getopt import getopt
import fileinput
from collections import Counter

N = 5

def calc_ngrams(texto):
    freqs = {}
    
    for seq1,seq2 in re.findall(f"(.)(?=(.{{{N-1}}}))",texto): 
        freqs[seq1+seq2] = freqs.get(seq1+seq2,0) +1
    
#   for seq in re.finditer(f"(.)(?=(.{{{N-1}}}))",texto): 
#       print(seq[1]+seq[2])

#   for i in range(0,len(texto)-N-1):
#       print(texto[i:i+N])


    return freqs

def print_sorted(freqs):
    for p in sorted(freqs.items(),key=lambda p:p[1],reverse=True):
        print(f"{p[0]}\t{p[1]}")



def main():
    opts, resto = getopt(sys.argv[1:], "albdc")
    dop = dict(opts)
    
    texto = ""

    # Reads file
    for line in fileinput.input(resto):
        texto += line

    print_sorted(calc_ngrams(texto))


main()
