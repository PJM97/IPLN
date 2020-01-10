

def quared(l1):
    for i in range(len(l1)):
        l1[i]=l1[i]*2
    return l1 

def main():
    l = [1,2,3]
    print(l)
    l = quared(l)
    l2=l
    print(l)
    print(l2)
if __name__ == "__main__":
    main()    