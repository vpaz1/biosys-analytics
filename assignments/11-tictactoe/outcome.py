#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-04-02
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    for state in args:
        if re.match('[XO.]{9}', state):
            rows = re.search(r'^(\w)\1\1(\.|X|O){6}$|^(\.|X|O){3}(\w)\4\4(\.|X|O){3}$|^(\.|X|O){6}(\w)\7\7$',state)
            columns_one = re.search(r'^(\w)(\.|X|O){2}\1(\.|X|O){2}\1(\.|X|O){2}$' ,state) 
            columns_two = re.search(r'^(\.|X|O)(\w)(\.|X|O){2}\2(\.|X|O){2}\2(\.|X|O)$' ,state)
            columns_three = re.search(r'^(\.|X|O){2}(\w)(\.|X|O){2}\2(\.|X|O){2}\2$' ,state)
            left_diag = re.search(r'^(\w)(\.|X|O){3}\1(\.|X|O){3}\1$' ,state)
            right_diag = re.search(r'^(\.|X|O){2}(\w)(\.|X|O)\2(\.|X|O)\2(\.|X|O){2}$' ,state)
 
            wins = rows or columns_one or columns_two or left_diag or right_diag or columns_three
           # print(wins.group(1))
           # print(wins.group(2)) 
            if wins: 
              # if wins.group(1) != '.' or wins.group(4) != '.' or wins.group(7) != '.':
               #     if wins.group(1) == 'O' or wins.group(4) == 'O' or wins.group(7) == 'O':
                #        print('O has won')
                 #   elif wins.group(1) == 'X' or wins.group(4) == 'X' or wins.group(7) == 'X':
                  #      print('X has won')
              # elif wins.group(2) != '.' or wins.group(4) != '.' or wins.group(7) != '.':
               #     if wins.group(2) == 'O' or wins.group(4) == 'O' or wins.group(7) == 'O':
                #        print('O has won')
                 #   elif wins.group(2) == 'X' or wins.group(4) == 'X' or wins.group(7) == 'X':
                  #      print('X has won')
               if wins.group(1) == 'X' or  wins.group(2) == 'X' or wins.group(4) == 'X' or wins.group(7) == 'X':
                   print('X has won')
               elif wins.group(1) == 'O' or  wins.group(2) == 'O' or wins.group(4) == 'O' or wins.group(7) == 'O':
                   print('O has won')
            else:
               print('No winner')
        else:
            print('State "{}" must be 9 characters of only ., X, O'.format(args[0]))

# --------------------------------------------------
main()
