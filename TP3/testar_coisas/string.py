myString = "spam\\neggs"
decoded_string = bytes(myString, "utf-8").decode("unicode_escape") # python3 
decoded_string = myString.decode('string_escape') # python2
print(decoded_string)
