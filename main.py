import sys
import calendar
from parser import parse_string

def cron_parser(cron_arg):
    print (cron_arg)
    try:
        minute, hour, month_day, month, week_day, command = cron_arg.split(" ")
    except:
        raise Exception("Invalid Input parameters")

    print ('\n'. join([
        'Minutes: {}'. format(parse_string(minute, 'minute')),
        'Hours: {}'. format(parse_string(hour, 'hour')),
        'Day of Month: {}'. format(parse_string(month_day, 'day')),
        'Month: {}'. format(parse_string(month, 'month')),
        'Day of Week: {}'. format(parse_string(week_day, 'week')),
        'Command: {}'.format(command)
        ])
    )


if __name__ == "__main__":
    cron_parser(sys.argv[1])
    
    