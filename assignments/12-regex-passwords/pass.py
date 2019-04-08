#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-04-04
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    #args is only two arguments
    password =  args[0]
    alt_version = args[1]

    new_pass = password[0].upper() + password[1:]    
    if password == alt_version:
       print('ok')
    elif password.upper() == alt_version:
       print('ok')
    elif new_pass == alt_version:
       print('ok')
    elif re.match('.?' + password + '.?', alt_version):
       print('ok')
    else:
       print('nah')    

# --------------------------------------------------
main()
