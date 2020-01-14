import random
import os
def getHexSum(s):
	num = 0
	for x in s:
		num+= ord(x)
		
	return num
    
key="";
while True:
    key+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
    if getHexSum(key) > 1381:
        key=""
    
    elif getHexSum(key) == 1381:
        print "Found Possible key: ", key
        