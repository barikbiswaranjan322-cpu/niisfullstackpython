ch='A'
print(ch)
print(ord(ch))

#convert asce value to char:
 
ch=65
print(ch)
print(chr(ch)) 

#convert upper case to lowyer case:

ch='A'
print(ch)
ch=chr(ord(ch)+32)
print(ch)

import sys
print("enter a char")
ch=input()
if len(ch)>1:
	print("one char allow")
	sys.exit()
if ch>='A'and ch<='Z':
ch=chr(ord(ch)+32)
print(ch)
	