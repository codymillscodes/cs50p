import csv
import sys
import os.path

def main():
    if check_arg():
        scourgify(sys.argv[1], sys.argv[2])

def check_arg():
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit(1)
    elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
        print('Not a CSV file')
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f'Could not read {sys.argv[1]}')
        sys.exit(1)
    else:
        return True

def scourgify(c, out):
    data = []
    with open(c, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    data_after = []
    for x in data:
        name = x['name']
        name = name.split(',')
        data_after.append({'first': name[1].lstrip(), 'last': name[0], 'house': x['house']})


    with open(out, 'w', newline='') as csvfile:
        fieldnames = ['first','last','house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for x in data_after:
            writer.writerow(x)


if __name__ == '__main__':
    main()