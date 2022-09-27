#!/usr/bin/env python3
import os, sys
from PIL import Image

os.chdir ("/home/student-01/supplier-data/images/")

for infile in os.listdir():
    print ("Imagem : " + infile)
    if infile.endswith('.tiff'):
       outfile = os.path.splitext(infile)[0]+".jpeg"
       im = Image.open(infile)
       print ("Nova imagem: " + outfile)
       im.thumbnail((600,400))
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=100)
