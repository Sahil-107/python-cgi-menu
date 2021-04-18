#!/usr/bin/python3
print("content-type: text/html\n")
print()

import subprocess
import cgi

stop = subprocess.run(("sudo systemctl stop httpd",shell=True)
    

if stop.returncode !=0:
        print("\nSome error happened.. :(")
if stop.returncode == 0 :
        print("\nWebserver Started.. :)")

