import datetime
import inflect
import re
import sys

def main():
    dob = input('Date of Birth: ')
    result = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', dob)

    if result:
        print(convert(dob))
    else:
        sys.exit(1)

def convert(d):
    p = inflect.engine()

    dob = d.split('-')
    for x, d in enumerate(dob):
        dob[x] = int(d)

    difference = datetime.date.today() - datetime.date(dob[0],dob[1],dob[2])
    num_str = p.number_to_words(difference.days*24*60, andword='').capitalize()
    return f'{num_str} minutes'

if __name__ == '__main__':
    main()