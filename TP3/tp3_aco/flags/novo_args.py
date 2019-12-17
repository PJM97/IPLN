import argparse
parser = argparse.ArgumentParser()
#Tem a flag e dá parse do seguinte tb
parser.add_argument("-v","--verbosity", help="increase output verbosity")
parser.add_argument("-f","--file", help="input file")
args = parser.parse_args()
if args.verbosity:
    print ("verbosity turned on")

print(args.verbosity)
print(args.file)      