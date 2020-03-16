#!/usr/bin/python
import sys
import string

args =sys.argv

upper_letters = string.ascii_uppercase*2
lower_letters = string.ascii_lowercase*2

def rot13(msg):
    out = []
    for i in msg:
        if i in string.ascii_uppercase:
            out.append(upper_letters[ord(i)-ord('A')+13])
        elif i in string.ascii_lowercase:
            out.append(lower_letters[ord(i)-ord('a')+13])
        else:
            out.append(i)
    return ''.join(out)

if len(args) == 1:
    try:
        while True:
            msg =input()
            if(len(msg)==0):
                exit(0)
            print(rot13(msg))
    except KeyboardInterrupt:
        print('\nGoodBye..')

try:
    out=[]
    for arg in args[1:]:
        out.append(rot13(arg))
    print(join(out))
    exit(0)
except:
    exit(1)


