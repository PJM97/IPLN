released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}

def main():
    print(released)

    #Adicionar um elemento

    released["iphone 5S"] = 2013

    print(released)

    #apagar um elemento

    del released["iphone"]

    print(released)

    print(len(released))

if __name__ == "__main__":
    main()  


