#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-02-08
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]    

    if len(sys.argv) == 1:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    lines = sys.argv[1]

    if os.path.isfile(lines) == False:
       print('{} is not a file'.format(lines))
       sys.exit(1)

    if os.path.isfile(lines) == True:
       line = open(lines, 'r')
       
       if len(args) == 1: 
         letters = line.readline()
         i = 0
         while letters:
             i += 1
             print('{}'.format(letters.strip()))
             letters = line.readline()
             if i == 3:
               break
       elif len(args) == 2:
         nums = int(sys.argv[2])
         if nums > 0:
           letters = line.readline()
           i = 0
           while letters:
              i += 1
              print('{}'.format(letters.strip()))
              letters = line.readline()
              if i == nums:
                break
         elif nums <= 0:
           print('lines ({}) must be a positive number'.format(nums))  
           sys.exit(1)
        
# --------------------------------------------------
main()
