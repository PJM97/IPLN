import argparse

def args_Parser():
    
   # 
    parser = argparse.ArgumentParser(description='Processamento de Texto')
    a_action = parser.add_argument('-a')
    c_action = parser.add_argument('-c')
    group1 = parser.add_mutually_exclusive_group()
    
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument(a_action)
    d_action = parser.add_argument('-d')
    
    return parser.parse_args()    
    
    #print("ola")


def main():
    args_Parser()
    
    
if __name__ == "__main__":
    main() 
