#!/bin/bash
printf "\n[+] Start installation..\n ------------------\n"
cp textractor.py /usr/local/bin/textractor && pip3 install pytesseract;
if [[ $? -ne 0 ]]; then
    printf "[!] The installation has failed.\n"
    rm /usr/local/bin/textractor 2>/dev/null
    exit 1
fi
printf " ------------------\n[+] Installation Complete.\n"
exit 0
