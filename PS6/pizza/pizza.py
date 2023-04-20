import sys
import os.path
import csv
from tabulate import tabulate

def main():
    if check_arg():
        handle_csv(sys.argv[1])

def check_arg():
    if len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    elif not sys.argv[1].endswith('.csv'):
        print('Not a CSV file')
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print('File does not exist')
        sys.exit(1)
    else:
        return True

def handle_csv(c):
    data = []
    with open(c, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    print(tabulate(data, headers="keys", tablefmt="grid"))

if __name__ == '__main__':
    main()