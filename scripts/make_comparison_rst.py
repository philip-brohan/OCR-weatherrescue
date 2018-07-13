#!/usr/bin/env python

# Make a document page (rst format) comparing image and transcribed data

# Get month and size from arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--year", help="Year (1889 to 1904)",
                    type=int,required=True)
parser.add_argument("--month", help="Month (1 to 12)",
                    type=str,required=True)
parser.add_argument("--imagew", help="Image width",
                    type=int,default=1000)
parser.add_argument("--textw", help="Text width",
                    type=int,default=1000)



