#!/usr/bin/python3
print("content-type: text/html\n")
print()

import subprocess
import cgi

stop = subprocess.run(("sudo systemctl stop httpd",shell=True)
    

if launch_out.returncode !=0:
        print("\nSome error happened.. :(")
if launch_out.returncode == 0 :
        print("\nWebserver Started.. :)")

