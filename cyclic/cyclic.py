#!/usr/bin/python3
import sys
import string

DEFAULT_REPS = 4

args = sys.argv
letters = string.ascii_uppercase

def printUsage():
    msg = '[?] Usage:\n\t-n,--number: -n {numOfDigits} {numOfRepetition}\n\t-l,--location: {numOfDigits} {subString}'
    print(msg)

def cyclic(length,reps = DEFAULT_REPS):
    reps = abs(int(reps))
    length = abs(int(length))
    n = int(length/reps)
    r = length % reps
    return ''.join([letters[i]*reps for i in range(n)]) + letters[n if n<len(letters) else 0]*r

def location(sub_s,reps = DEFAULT_REPS):
    length = len(letters)*reps
    series = cyclic(length,reps)
    if sub_s in series:
        for i in range(length):
            if series[i:i+reps] == sub_s:
                print('[+] location: {}'.format(i))
    else:
       print("[-] Couldn't locate the given sub string..")


if len(args) < 3:
    printUsage()
    exit(0)

elif args[1] == '-n' or args[1] == '--number':
    try:
        if len(args) == 4:
            if len(letters)*int(args[2]) < int(args[3]):
                print('[!] Please choose shorter length or more repetitions..')
                exit(1)
            print(cyclic(args[3],args[2]))
        else:
            if len(letters)*DEFAULT_REPS < int(args[2]):
                print('[!] Please choose shorter length or more repetitions..')
                exit(1)
            print(cyclic(args[2]))
    except:
        printUsage()
        exit(1)
    exit(0)
elif args[1] == '-l' or args[1] == '--location':
    try:
        if len(args) == 4:
            if len(args[3]) != int(args[2]):
                print("[!] Incorrect sub string length..") 
            else:
                location(args[3].upper(),int(args[2]))
        else:
            if len(args[2]) != DEFAULT_REPS:
                print("[!] Incorrect sub string length..") 
            else:
                location(args[2].upper())
    except:
        printUsage()
        exit(1)

else:
    printUsage()
    exit(0)


