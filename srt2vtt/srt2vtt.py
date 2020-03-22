#!/usr/bin/python3

#  /-----------------------------------------------------------------------\  #
# |                        ~srt to vtt converter~                           | #
# |                           -----------------                             | #
# |                       github.com/AmitNiz/toolBox                        | # 
# |                                March 2020                               | #
#  \-----------------------------------------------------------------------/  #

import sys
import os

MAGIC_BYTES = 'WEBVTT\n\n'

input_files = []

#convert srt file to vtt
def convert2vtt(file_name,srt_file):
    arr = srt_file.split('\n')
    converted =[]
    for i in arr[1:]:
        if(not i.isdigit()):
            if('-->' in i):
                converted.append(i.replace(',','.'))
            else:
                converted.append(i)
    print('[+] Converted: {}'.format(file_name))
    return MAGIC_BYTES + '\n'.join(converted)


def shift_time(sub_file):
    pass

#recursive directory converting.
if ('-r' in sys.argv):
    input_files = [i for i in os.listdir() if '.srt' in i]
    if(len(input_files) >0):
        print('[+]Converting: {}'.format(input_files))
    else:
        print('[-] No .srt files were found..')
        exit(1)
else:
    try:
        input_files = [sys.argv[1]]
    except:
        print('[!] Error: Invalid Input File..')

try:
    
    for file in input_files:
        with open(file,'r') as f:
            content = f.read()
            new_name = file.split('.')[0] +'.vtt'
            converted_file = convert2vtt(file,content)
            with open(new_name,'w') as f:
                f.write(converted_file)
except:
    print('[!] Something went wrong..')


