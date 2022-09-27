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

#!/usr/bin/env python3
import os
import requests
import re

keys = ['name', 'weight', 'description', "image_name"]

os.chdir("/home/student-01/supplier-data/descriptions/")

for files in os.listdir():
  
  keycount = 0
  names_dict = {}
  with open(files) as file:
    for line in file:
      for names in line.splitlines():
        if keycount == 1:     
          numb = int(re.sub(' lbs', '', names))  
          names_dict[keys[keycount]] = numb
          keycount += 1 
        elif keycount <= 2:       
          names_dict[keys[keycount]] = names
          keycount += 1

  img = re.sub('.txt', '.jpeg', files)
  names_dict["image_name"] = img

  print (names_dict)

  response = requests.post("http://xxx.xxx.xxx.xxx/fruits/", json=names_dict)
print (response.request.body)
print (response.status_code)