"""convert upper case to lower case"""
import sys
print("enter a char")
ch=input()
if len(ch)>1:
   print("one char allow")
   sys.exit()
if ch>='A'and ch<='Z':    #if 65<ch<90
    ch=chr(ord(ch)+32)
    print(ch)