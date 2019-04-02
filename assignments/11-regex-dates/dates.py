#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-03-29
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]
   # dates = sys.argv[1]
   # dates = list(dates)
    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
 
    
    month_dict = dict(jan='01', feb='02', mar='03', apr='04', may='05', jun='06', jul='07', aug='08', sep='09',
                  oct='10', nov='11', dec='12')
    
    for date in args:
        date_one = re.compile(
                       '(?P<year>\d{4})'
                       '[-]?''\s*'
                       '(?P<month>\d{2})'
                       '[-]?''\s*'
                       '(?P<day>\d{2})')

        date_two = re.compile('(?P<year>\d{4})'
                       '[-]?'
                       '(?P<month>\d{2})'
                       '(?P<day>\d{0})')

        date_three = re.compile('(?P<month>\d{2})'
                       '[/]?'
                       '(?P<year>\d{2})'
                       '(?P<day>\d{0})')
        
        date_four = re.compile('(?P<month>(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).?)'
                             '[/,-]?'
                             '\s*'
                             '(?P<year>\d{4})'
                             '(?P<day>\d{0})')
        date_five = re.compile(
                       '(?P<year>\d{4})'
                       '[-]?''\s*'
                       '(?P<month>\d{1})'
                       '[-]?''\s*'
                       '(?P<day>\d{1})')

        date_six = re.compile('(?P<year>\d{4})'
                       '[-]?''\s*'
                       '(?P<month>\d{1})'
                       '(?P<day>\d{0})')

        date_seven = re.compile('(?P<month>\d{1})'
                       '[/-]?''\s*'
                       '(?P<year>\d{2})'
                       '(?P<day>\d{0})')
        
        date_eight = re.compile(
                       '(?P<year>\d{2})'
                       '[/-]?'
                       '(?P<month>\d{0})'
                       
                       '(?P<day>\d{0})')
         
        #date_nine = re.compile('(?P<month>\d{1})'
         #              '[/]?''\s*'
          #             '(?P<year>\d{4})'
           #            '(?P<day>\d{0})')
   # for date in args:
        if date_one.match(date): #or date_two.match(date) or date_three.match(date)
            match = date_one.match(date)
            tmpl = '{year}-{month}-{day}'
            standard = tmpl.format(year=match.group('year'), 
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_two.match(date):
            match = date_two.match(date)
            tmpl = '{year}-{month}-01'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_three.match(date):
            match = date_three.match(date)
            tmpl = '20{year}-{month}-01'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_four.match(date):
            match = date_four.match(date)
            tmpl = '{year}-{month}-01'
            standard = tmpl.format(year=match.group('year'),
                               month=month_dict[match.group('month').lower()[:3]],
                               day=match.group('day'))
        elif date_five.match(date):
            match = date_five.match(date)
            tmpl = '{year}-0{month}-0{day}'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_six.match(date):
            match = date_six.match(date)
            tmpl = '{year}-0{month}-01'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_seven.match(date):
            match = date_seven.match(date)
            tmpl = '20{year}-0{month}-01'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
        elif date_eight.match(date):
            match = date_eight.match(date)
            tmpl = '{year}-01-01'
            standard = tmpl.format(year=match.group('year'),
                               month=match.group('month'),
                               day=match.group('day'))
       # elif date_nine.match(date):
        #    match = date_nine.match(date)
         #   tmpl = '{year}-0{month}-01'
          #  standard = tmpl.format(year=match.group('year'),
           #                    month=match.group('month'),
            #                   day=match.group('day'))
        else:
            print('No match')

        print('{}'.format(standard))
# --------------------------------------------------
main()
