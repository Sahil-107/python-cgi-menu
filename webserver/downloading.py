#!/usr/bin/python3
print("content-type: text/html\n")
print()

import subprocess
import cgi

download = subprocess.run("sudo yum install httpd -y",shell=True)
    

if launch_out.returncode !=0:
        print("\nSome error happened.. :(")
if launch_out.returncode == 0 :
        print("\nWebserver Downloaded.. :)")

