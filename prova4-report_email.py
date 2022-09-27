#!/usr/bin/env python3

import json
import locale
import sys
import reports
import os
import re
import emails

keys = ['name', 'weight', 'description', "image_name"]
text = ""

os.chdir("/home/student-01/supplier-data/descriptions/")
for files in os.listdir():

  keycount = 0
  names_dict = {}
  with open(files) as file:
    for line in file:
      for names in line.splitlines():
        if keycount <= 1:
          names_dict[keys[keycount]] = names
          keycount += 1

  result = json.dumps(names_dict)
  result = re.sub('[^A-Za-z0-9: ,]+', '', result)
  result = re.sub(', ', '<br/>', result)
  result = re.sub('lbs', 'lbs<br/><br/>', result)
  for item in result:
    text += item

  print (text)
  reports.generate("/tmp/processed.pdf", "Processed Update", text)
  # TODO: send the PDF report as an email attachment
  emails.generate("automation@example.com", "student-01@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
  emails.send(emails.generate("automation@example.com", "student-01@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",  "/tmp/processed.pdf"))
