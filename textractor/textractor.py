#!/usr/local/bin/python3.7

#####################################################
# Author: Amit Nizri                                #
# Repository: github.com/AmitNiz/toolBox/textractor #
# Date: Aug, 2019                                   #
#####################################################

#TODO: 
#add capture mode.

import sys,pytesseract,os


def __scan(ls):
    for path in ls:
        try:
            data = pytesseract.image_to_string(path)
        except:
            sys.stderr.write("[!] Couldn't scan the file: %s\n" %(path.split('/')[-1]))
            continue
        print("[+] %s: %s" % (path.split('/')[-1],data))

def files():
    __scan(sys.argv[2:])

def capture():
    print("Capture mode is currently in progress")

def directory():
    try:
        path = sys.argv[2]
        ls = [os.path.join(path,name) for name in os.listdir(path)]
    except:
        sys.stderr.write("[!] The given path isn't valid\n\n")
        exit(1)
    __scan(ls)

def help_page():
    print("Modes: [-f --files],[-c --capture],[-d --directory],[-h --help]\n"
        +"\t[?] Files: textExtractor -f/--files file1 file2 ..\n"
        +"\t[?] Screenshot: textractor -c/--capture\n"
        +"\t[?] Directory: textractor -d/--directory path")

def main():

    modes = {'-f':files,'--files':files,'-c':capture,'--capture':capture,
     '-d':directory,'--directory':directory,'-h':help_page,'--help':help_page}
    try:
        modes[sys.argv[1]]()
    except:
        help_page()
        exit(1)

if __name__ =='__main__':
    main()
