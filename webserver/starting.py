#!/usr/bin/python3
print("content-type: text/html\n")
print()

import subprocess
import cgi

start = subprocess.run("sudo systemctl start httpd",shell=True)
    

if start.returncode !=0:
        print("\nSome error happened.. :(")
if start.returncode == 0 :
        print("\nWebserver Started.. :)")
