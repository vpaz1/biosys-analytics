#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys



# --------------------------------------------------
def main():
    names = sys.argv[1:]
    nums = len(sys.argv)-1

    if len(names) == 0:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
	
    if len(names) == 1:
        print('Hello to the 1 of you: ' + names[0] + '!')
    elif len(names) == 2:
        print('Hello to the {} of you: {}!'.format(nums, " and " .join(names)))
    elif len(names) > 2:
        names[-1] = 'and ' + names[-1]
        print('Hello to the {} of you: {}!'.format(nums, ", ".join(names)))
# --------------------------------------------------
main()
