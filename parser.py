import calendar

def parse_string(string, type):
   """
    Given a cron string parses it depending on the type.
   """
   # valid ranges for the different type 
   values = {
      'week': [i for i in range(1, 8)],
      'month': [i for i in range(1, 13)],
      'hour': [i for i in range(0, 24)],
      'day': [i for i in range(1, 32)],
      'minute': [i for i in range(0, 60)],
      'month_abbr': [
         'JAN', 'FEB', 'MAR',
         'APR', 'MAY', 'JUN',
         'JUL', 'AUG', 'SEP',
      ],
      'week_abbr': [
         'SUN', 'MON', 'TUE',
         'WED', 'THU', 'FRI',
         'SAT'
      ]
      
   }
   
   if string == '*':
      return ' ' .join(map(str,values[type]))

   if ',' in string:
      return ' '.join(string.split(','))

   if '-' in string:
      return display_range(string, values, type)
   
   if '/' in string:
      return display_step_values(string, values[type],type)

   return string
   
def display_range(string, values, type):
   start, stop = string.split('-')
   try:
      start, stop  = int(start), int(stop)
   except ValueError:
      start, stop  = values[type + '_abbr'].index(start), values[type + '_abbr'].index(stop)
      return ' '.join(values[type + '_abbr'][start:stop + 1])

   return ' '.join(map(str, [i for i in range(int(start), int(stop)+1)]))

def display_step_values(string, values, type):
   start, stop = string.split('/')
   return ' '.join(map(str, [i for i in values if i % int(stop) == 0]))


        

