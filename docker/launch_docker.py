#!/usr/bin/python3
print("content-type: text/html\n\n")
print("")

import subprocess
import cgi


data = cgi.FieldStorage()
os_name = data.getvalue("os_name")
image_name = data.getvalue("image_name")

launch_out = subprocess.run("sudo docker run -dit --name {} {}".format(os_name,image_name),shell=True)
    

if launch_out.returncode !=0:
        print("\nSome error happened.. :(")
if launch_out.returncode == 0 :
        print("\nContainer Launched  :)")
