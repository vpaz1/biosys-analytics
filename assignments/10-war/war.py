#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-03-21
Purpose: Rock the Casbah
"""

import argparse
import sys
from itertools import product
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

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
    seed_arg = args.seed

    symbols = list('♥♠♣♦')
    num = list(range(2, 11))
    letters = list('JQKA')
    num_lett = num + letters
    deck = list(product(symbols, num_lett))
    cards = []
    for char in deck:
        deck_cards = (''.join(map(str, char)))
        cards.append(format(deck_cards))
        
    cards.sort()
   # print(cards)
   # cards.reverse()
    if seed_arg:
        random.seed(seed_arg)
        random.shuffle(cards)
    else:
        random.shuffle(cards)

    hand1 = []
    hand2 = []
    for i in range(len(cards)):
        if len(cards) == 0: break
        card = cards.pop()
        if i % 2 == 0:
            hand1.append(card)
        else:
            hand2.append(card)
    
    num1 = 0
    num2 = 0     
    for card1, card2 in zip(hand1, hand2):
         if card1[1] == card2[1]:
             print('{:>3}{:>4} WAR!'.format(card1, card2))
         elif card1[1] > card2[1]:
             if card2[1] == 'A':
                 print('{:>3}{:>4} P2'.format(card1, card2))
                 num2 += 1
             elif card1[1] == '2':
                 print('{:>3}{:>4} P2'.format(card1, card2))
                 num2 += 1
             elif card2[1] == 'K' and card1[1] == 'Q':
                 print('{:>3}{:>4} P2'.format(card1, card2))
                 num2 += 1
             elif card2[1] == '1' and card1[1] == '4':
                 print('{:>3}{:>4} P2'.format(card1, card2))
                 num2 += 1
             else:
                 print('{:>3}{:>4} P1'.format(card1, card2))
                 num1 += 1
         elif card1[1] < card2[1]:
             if card1[1] == 'A':
                 print('{:>3}{:>4} P1'.format(card1, card2))
                 num1 += 1
             elif card2[1] == '2':
                 print('{:>3}{:>4} P1'.format(card1, card2))
                 num1 += 1
             elif card1[1] == 'K' and card2[1] == 'Q':
                 print('{:>3}{:>4} P1'.format(card1, card2))
                 num1 += 1
             elif card1[1] == '1' and card2[1] == '4':
                 print('{:>3}{:>4} P1'.format(card1, card2))
                 num1 += 1
             else:
                 print('{:>3}{:>4} P2'.format(card1, card2))
                 num2 += 1           

    if num1 > num2:
         print('P1 {} P2 {}: Player 1 wins'.format(num1, num2))
    elif num2 > num1:
         print('P1 {} P2 {}: Player 2 wins'.format(num1, num2))
    else:
         print('P1 {} P2 {}: DRAW'.format(num1, num2))



# --------------------------------------------------
if __name__ == '__main__':
    main()
