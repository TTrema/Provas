#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module
os.chdir ("/home/student-01/supplier-data/images/")

url = "http://xx.xxx.xxx.xx/upload/"
for infile in os.listdir():
    if infile.endswith('.jpeg'):
        with open(infile, 'rb') as opened:
             r = requests.post(url, files={'file': opened})