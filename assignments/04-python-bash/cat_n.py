#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    #args = sys.argv[1]
   
    #print('{}'.format(args))
    if len(sys.argv) == 1: #assuming that the only argument is the script name
       print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
       sys.exit(1)
    args = sys.argv[1]
    if os.path.isfile(args) == False:
       print('{} is not a file'.format(args))
       sys.exit(1)
    if os.path.isfile(args) == True:
       line = open(args, 'r')
       letters = line.readline()
       i = 0
       while letters:
             i += 1
             print('    {}: {}'.format(i, letters.strip()))
             letters = line.readline()
             
           

# --------------------------------------------------
main()
