line = "aaa\nbbb\nccc\n"
print(line.split('\n'))
print(line.splitlines())

mystr = "xxxSPAMxxx"
print(mystr.find("SPAM")) # 3
mystr = "xxaaxxaa"
print(mystr.replace("aa","SPAM")) #xxSPAMxxSPAM
mystr = "xxxSPAMxxx"
print("SPAM" in mystr) # True
print("NI" in mystr) # False
print(mystr.find("NI")) #-1

mystr = "\t NI\n"
print(mystr.strip()) #'NI'
print(mystr.rstrip()) #'\t  NI'
mystr = "UPPER"
print(mystr.lower())#upper
print(mystr.isalpha())#True
print(mystr.isdigit())#False

import string 
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters) #lower followed by upper
print(string.whitespace)

mystr = "aaa,bbb,ccc"
print(mystr.split(","))

mystr = "a b\nc\nd"
print(mystr.split())

delim = "NI"
print(delim.join(['aaa','bbb','ccc']))
print(' '.join(['A','nice','parrot']))

chars = list('lorreta')
print(chars)
print(chars.append('!'))
print(''.join(chars))

mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa')))

#convertion between string and int
print(int('42'))
print(eval('42'))

print(str(42))
print(repr(42))

print('%d'%42,'{:d}'.format(42))
print("42"+str(1),int("42")+1)