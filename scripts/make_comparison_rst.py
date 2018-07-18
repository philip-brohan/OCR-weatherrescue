#!/usr/bin/env python

# Make a document page (rst format) comparing image and transcribed data


# Get month and size from arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--year", help="Year (1889 to 1904)",
                    type=int,required=True)
parser.add_argument("--month", help="Month (1 to 12)",
                    type=int,required=True)
parser.add_argument("--imagew", help="Image width (pixels)",
                    type=int,default=800)
parser.add_argument("--textw", help="Text width",
                    type=int,default=800)
args = parser.parse_args()

# rst file location
rst_file="../docs/individual_months/%04d-%02d.rst" % (args.year,args.month)

# Image path (from rst file)
ipath="../../images/%04d-%02d.jpg" % (args.year,args.month)

# Data file location
dpath="../../data/%04d-%02d.csv"  % (args.year,args.month)
with open(rst_file,'w') as opfile:
    opfile.write("%04d-%02d\n" % (args.year,args.month))
    opfile.write("=======\n\n")

    opfile.write("Document\n")
    opfile.write("--------\n\n")

    opfile.write(".. figure:: %s\n" % ipath)
    opfile.write("   :width: %dpx\n" % args.imagew)
    opfile.write("   :align: center\n\n")
   

    opfile.write("Transcription\n")
    opfile.write("-------------\n\n")
    opfile.write(".. literalinclude:: %s" % dpath)

    
