#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-02-01
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    arg = sys.argv[1:]
    
    if len(arg) == 0:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    elif len(arg) >= 1:
        num = 0
        for letters in arg[0]:
            if letters in 'aeiouAEIOU':
               num += 1   
        if num == 1:
            print('There is {} vowel in "{}."'.format(str(num), arg[0]))
        else:
            print('There are {} vowels in "{}."'.format(str(num), arg[0]))

# --------------------------------------------------
main()
