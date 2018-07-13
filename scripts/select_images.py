#!/usr/bin/env python

# Make the benchmark images from those Ed supplied
#  Select only Fort William Pressures
#  Trim the weatherescue instructions off the top
#  Rename with filename giving date.

import os
import subprocess

# Scratch data dir
ddir="%s/OCR-weatherrescue" % os.getenv('SCRATCH')

Ed_images=sorted(os.listdir("%s/PRES-1898-1904/" % ddir))

newdir="%s/benchmark_format" % ddir

year=1898
month=1
for image in Ed_images:
   # Take only the Fort William pages 
   if '_FW_' not in image: continue
   new_name="%04d-%02d.jpg" % (year,month)
   # Cute the weatherrescue addition off the top, and rename
   proc = subprocess.Popen(
          "convert -gravity South -crop 100%%x90%% %s %s" % 
                    ("%s/PRES-1898-1904/%s" % (ddir,image),
                     "%s/%s" % (newdir,new_name)),
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, shell=True)
   (out, err) = proc.communicate()
   month=month+1
   if month>12:
       month=1
       year=year+1

