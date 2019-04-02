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
 
    
    month_dict = {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09','oct':'10', 'nov':'11', 'dec':'12'}
    
    for date in args:
        date_one = re.compile(
                       '(?P<year>\d{4})'
                       '[-/,]'
                       '(?P<month>\d{1,2})'
                       '[-/,]'
                       '(?P<day>\d{1,2})'
                       '[$|\D]')

        date_two = re.compile('(?P<year>\d{4})'
                       '[-/,]'
                       '(?P<month>\d{1,2})'
                       )

        date_three = re.compile('(?P<month>\d{1,2})'
                       '[-/,]'
                       '(?P<year>\d{2})'
                       '(?P<day>\d{0})')
        
        date_four = re.compile('(?P<month>(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).?)'
                             '[/,-]?'
                             '\s*'
                             '(?P<year>\d{4})'
                             '(?P<day>\d{0})')
        date_five = re.compile(
                       '(?P<year>\d{4})'
                       
                       '(?P<month>\d{1,2})'
                       
                       '(?P<day>\d{1,2})')
        #date_six = re.compile('(?P<month>\d{1,2})'
         #              '[-/,]'
          #             '(?P<year>\d{2})'
           #            '(?P<day>\d{0})')


        match = date_one.match(date) or date_two.match(date) or date_three.match(date) or date_three.match(date) or date_four.match(date) or date_five.match(date)
        if match:
            match_dict = match.groupdict()
           # print(match_dict)
            day = match_dict.get('day')
            month = match_dict.get('month')
           # print(month)
            year = match_dict.get('year') 
      # print(month)
            if day:
               if len(day) == 1:
                  day = '0'+ day
            else:
               day = '01'
            if len(month) == 1:
               month = '0'+ month
             #  print(month) 
            if len(month) >= 3:
               month = month_dict[month.lower()[:3]]
              # print(month)
            if len(year) == 2:
               year = '20' + year
            tmpl = '{year}-{month}-{day}'
           # standard = tmpl.format(year, 
            #                   month,
             #                  day)
            print('{}-{}-{}'.format(year, month, day))
        else:
            print('No match')

       # print('{}'.format(standard))
# --------------------------------------------------
main()
