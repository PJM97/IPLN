# Python3 code to demonstrate working of 
# Check if string matches regex list 
# Using join regex + loop + re.match() 
import re 
  



test_list = ["gee*", "gf*", "df.*", "re"]  #lista com expressoes regulares
  
# printing list  
print("The original list : " + str(test_list)) 
  
# initializing test_str  
test_str = "geeksforgeeks"
  
# Check if string matches regex list 
# Using join regex + loop + re.match() 

temp = '(?:% s)' % '|'.join(test_list) 

print('temp: ',temp)

res = False
if re.match(temp, test_str): 
    res = True
  
# Printing result 
print("Does string match any of regex in list ? : " + str(res)) 

