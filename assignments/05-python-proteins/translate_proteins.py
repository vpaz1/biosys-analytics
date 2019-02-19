#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-02-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
       'STR', metavar='str', help='DNA/RNA sequence')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename (default: out.txt)',
        metavar='FILE',
        type=str,
        default='out.txt')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations (default: None)',
        metavar='FILE',
        type=str,
        default=None)

   # parser.add_argument(
       # '-o FILE', '--outfile FILE', help='Output filename (default: out.txt)', action='store_true')

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
    str_codon = args.codons
    int_outfile = args.outfiles
   # flag_arg = args.flag
    pos_arg = args.positional

    if not os.path.isfile(int_codon):
       print('--codons "{}" is not a file'.format(int_codon))
       exit(1)

    print('str_arg = "{}"'.format(str_codon))
    print('int_arg = "{}"'.format(int_outfile))
   # print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
