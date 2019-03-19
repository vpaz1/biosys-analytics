#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-03-14
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

   # parser.add_argument(
    #    'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    bottles = args.num_bottles

    if bottles < 1:
         die('N() must be a positive integer')
    num = list(reversed(sorted(range(bottles+1))))
    for i in num[::1]:
   # for i in range(bottles, 0, -1):
        # if i > 1: 
         if i > 1:
             print('{} bottles of beer on the wall,'.format(i))
             print('{} bottles of beer,'.format(i))
             print('Take one down, pass it around,'.format(i))
            # print('{} bottle of beer on the wall!\n'.format(i))
             i = i - 1
             if i == 1:
                 print('{} bottle of beer on the wall!\n'.format(i))    
             else:
                 print('{} bottles of beer on the wall!\n'.format(i))
         else:
             # print('{} bottle of beer on the wall!\n'.format(i))
             # if i == 0:            
              print('{} bottle of beer on the wall,'.format(i))
              print('{} bottle of beer,'.format(i))
              print('Take one down, pass it around,'.format(i))
              
              i = i - 1
             # if i == 0:
              print('{} bottles of beer on the wall!'.format(i))
              exit(0)
     

# --------------------------------------------------
if __name__ == '__main__':
    main()
