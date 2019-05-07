#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
import string

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'STR', metavar='STR', nargs='+',help='Input a text or a file')

   # parser.add_argument(
    #    '--FILE',
     #   help='input file',
      #  metavar='File',
      #  type=str,
      #  default='')

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
    args = args.STR
    #args = sys.argv[1:]
    #print(args)

  
    if len(args) != 1:
        print('Usage: {} ORD-WAY'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    #pig_latin = []
    #word_match = []
   # if os.path.isfile(args) == True:
    #    print(args)

    #else: 
    for words in args:
        if os.path.isfile(words):
            with open(words) as f:
                for line in f:
                    #word = line.rstrip()
                    word_list = line.split()
                    for word in word_list:
                        word = re.sub("[^a-zA-Z0-9']", '', word)
                        #print(word)
                        match = re.match('^([' + consonants + ']+)(.+)', word)   
                        if match:
                           word_match = '-'.join([match.group(2), match.group(1) + 'ay'])
                        else:
                           word_match = word + '-yay'
                        print(word_match, end=' ')
                    print()
                    
        else: 
            #words = re.sub("[^a-zA-Z0-9']", '', words)
            word_list = words.split()
            pig_latin = []
            for word in word_list:
                word = re.sub("[^a-zA-Z0-9']", '', word)
                match = re.match('^([' + consonants + ']+)(.+)', word)
                if match:
                    word_match = '-'.join([match.group(2), match.group(1) + 'ay'])
                else:
                    word_match = word + '-yay'
                pig_latin.append(word_match)
            print(' '.join(pig_latin))

# --------------------------------------------------
if __name__ == '__main__':
    main()
