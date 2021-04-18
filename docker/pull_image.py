#!/usr/bin/python3
print("content-type: text/html\n\n")
print("")

import subprocess
import cgi


data = cgi.FieldStorage()
image_name = data.getvalue("image_name")

launch_out = subprocess.run("sudo docker pull {}".format(image_name),shell=True)
    

if launch_out.returncode !=0:
        print("\nSome error happened.. :(")
if launch_out.returncode == 0 :
        print("\nImage Pulled  :)")