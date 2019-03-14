#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-03-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import csv

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   
   # parser.add_argument(
    #    'input', nargs='+', type=str)

    parser.add_argument(
        'FILE', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    annot = args.annotations
    tab_file = args.FILE
    out_file = args.outfile

    
   # tab_file = file_name[0] 
    if not os.path.isfile(tab_file):
        die('"{}" is not a file'.format(tab_file))
   
    if not os.path.isfile(annot):
        die('"{}" is not a file'.format(annot)) 
   
    

    with open(annot, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter ='\t')
        for row_csv in reader:
            genus = row_csv[6][0:]
            species = row_csv[7][0:]
    
    with open(tab_file, 'r') as tabfile:
        readers = csv.reader(tabfile, delimiter = '\t')
        print('seq_id\t')
        for rows in readers:
           # row = list(rows)
            seq_id = rows[1][0:]
            pident = rows[2][0:] 
            print(seq_id)
            print(pident)
    if out_file:
        out = open('out.txt', 'w')
        out.writelines(seq_id, pident, genus, species)
        out.close()
 # print(','.join(seq_id, pident, genus, species)
           #outfile.write('\t',join(seq_id, pident)
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
