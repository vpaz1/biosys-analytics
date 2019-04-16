#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-04-11
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        'positional',
        help='File inputs',
        metavar='FILE',
        nargs=2)

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        default=False,
        action='store_true')

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
def dist(s1, s2):
    """take two strings & return an integer value-Hamming distance"""
    diffs = 0
    if len(s1) != len(s2): 
        space = abs(len(s1) - len(s2))
        for ch1, ch2 in zip(s1, s2):
              if ch1 != ch2:
                 diffs += 1
        diffs = diffs + space
    else:
        for ch1, ch2 in zip(s1, s2):
              if ch1 != ch2:
                 diffs += 1
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2,diffs))
    return diffs
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file_input = args.positional
    dists = 0 
    
    logging.basicConfig(
         filename='.log',
         filemode='w',
         level=logging.DEBUG if args.debug else logging.CRITICAL
    )
    logging.debug('file1 = {}, file2 = {}'.format(file_input[0],file_input[1]))

    
    for filenames in file_input:
        if not os.path.isfile(filenames):
            die('"{}" is not a file'.format(filenames))
    for filenames in file_input:
        if os.path.isfile(filenames):
            with open(file_input[0]) as lines1, open(file_input[1]) as lines2:
                content1 = lines1.readlines()
                content2 = lines2.readlines()
    if (len(content1)) == 1:
        for x1 in content1:
            s1 = x1.split()
        for x2 in content2:
            s2 = x2.split()  
        for str1, str2 in zip(s1, s2):
            dists += dist(str1, str2)
        print((dists))
    else:
        for str1, str2 in zip(content1, content2):
            dists += dist(str1, str2)
        print((dists))


# --------------------------------------------------
if __name__ == '__main__':
    main()
