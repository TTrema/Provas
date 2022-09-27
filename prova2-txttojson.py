#!/usr/bin/env python3
import os
import requests

keys = ['title', 'name', 'date', 'feedback']

os.chdir("/data/feedback/")

for files in os.listdir():
  keycount = 0
  names_dict = {}
  with open(files) as file:
    for line in file:
      for names in line.splitlines():
        names_dict[keys[keycount]] = names
        keycount += 1

  response = requests.post("http://xx.xxx.xxx.xxx/feedback/", json=names_dict)
print (response.request.body)
print (response.status_code)
