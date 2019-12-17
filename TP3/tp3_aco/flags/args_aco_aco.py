import argparse

def args_parser():
    parser = argparse.ArgumentParser(description='Processador de')
    parser.add_argument('', metavar='Dab', type=str, nargs='+',
                   help='an integer for the accumulator')
    #parser.add_argument('--sum', dest='accumulate', action='store_const',
     #               const=sum, default=max,
      #              help='sum the integers (default: find the max)')

    args = parser.parse_args()
   # print(args.accumulate(args.integers))

def main():
    args_parser()
    
if __name__ == "__main__":
    main()     