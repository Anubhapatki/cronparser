
### Description 

The  program allows to visualise a cron command in a table format described below

The approach is as follows :

- Cron format supports multiple input types :

      - 5 : a fixed value
      - 5-10 : a range
      - */5 : a frequency
      - 5,7 : a list of values 
      
#### Installation

Dependencies :

Install python if not installed. 

To run the program use
python main.py "CRON_STRING"

For example:

python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"

For this input, you should then get the following output:

    Minutes: 0 15 30 45
    Hours: 0
    Day of month: 1 15
    Month: 1 2 3 4 5 6 7 8 9 10 11 12
    Day of Week: 1 2 3 4 5
    Command: /usr/bin/find

#### Notes