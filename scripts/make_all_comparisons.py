#!/usr/bin/env python

# Make all the monthly comparison pages (and the index page).

import subprocess

for year in range(1898,1905):
    for month in range(1,13):
        if year==1904 and month>9: continue
        proc = subprocess.Popen(
                   ("./make_comparison_rst.py --year=%d --month=%d" % 
                        (year,month)),
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
