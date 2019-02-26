#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
       'direct', nargs='+', type=str)

    parser.add_argument(
        '-w',
        '--width',
        help='A named string argument',
        dest='width',
        type=int)

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
    args = get_args()
    input_direct = args.direct
    width = args.width

    if len(input_direct) == 0:
        print('usage: first_lines.py [-h] [-w int] DIR [DIR ...]\nfirst_lines.py: error: the following arguments are required: DIR'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    i = 0
    for i in range(len(input_direct)):
        if os.path.isdir(input_direct[i]) == False:
           warn('"{}" is not a directory'.format(input_direct[i]))
           continue
        print('{}'.format(input_direct[i]))
        files = os.listdir(input_direct[i])
        j = 0
        line_list = []
        lines = []
        first = []
        for j in range(len(files)):
           file_length = len(files[j]) 
           path_name = (os.path.join(input_direct[i],files[j]))
           with open(path_name) as f:
              line_one = f.readline()
              line_one = line_one.rstrip()
              length_other = 50 - (len(line_one) + (file_length))
             
              
              if line_one not in line_list:
                 if width:
                    length_other= width - (len(line_one) + (file_length))
                    line = line_one + ' ' + '.'*length_other + ' ' + files[j] +'\n'
                 else:
                    line = line_one + ' ' + '.'*length_other + ' ' + files[j] +'\n'
                 line_list.append(line)
           lines = sorted(line_list)
        j += 1

        for k in range(len(files)):
           print(lines[k], end = "")
        k += 1 
    
    i += i
# --------------------------------------------------
if __name__ == '__main__':
    main()
