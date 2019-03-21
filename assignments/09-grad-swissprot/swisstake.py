#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO
from Bio.SwissProt import KeyWList

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        nargs='+',
        metavar='STR',
        type=str,
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o', 
        '--output',
        help='Output filename',
        metavar='FILE',
        default = 'out.fa')

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
    file_arg = args.FILE
    skip_arg = args.skip
    key_arg = args.keyword
    out_arg = args.output
 
    if not os.path.isfile(file_arg):
        die('"{}" is not a file'.format(file_arg))
    skip_arg = [j.lower() for j in skip_arg]
    key_arg = [key_arg]
    num_skip = 0
    no_match = 0
    total = 0
    new = []
    out_file = open(out_arg, 'wt')
    print('Processing "{}"'.format(file_arg))
    for seq_record in SeqIO.parse(file_arg, 'swiss'):
        all_species = (seq_record.annotations)
        
        keyword = all_species.get('keywords')
        keyword = [x.lower() for x in keyword]
        match = any([e for e in key_arg if e in keyword]) #True or false
        total += 1
       
        if match != True:
           no_match += 1
           continue
        else:
           taxa = all_species.get('taxonomy')
           taxa = [y.lower() for y in taxa]
           if skip_arg:
              match_taxa = any([e for e in skip_arg if e in taxa]) #True or false
              if match_taxa == True:
                 num_skip += 1
                 continue
           if out_arg:
              SeqIO.write(seq_record, out_file, 'fasta')
        
    num_skips = num_skip+no_match
    total_num = total - num_skips
    print('Done, skipped {} and took {}. See output in "{}".'.format(num_skips, total_num, out_arg))
   
 
# --------------------------------------------------
if __name__ == '__main__':
    main()
