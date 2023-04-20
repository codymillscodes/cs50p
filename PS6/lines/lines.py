import sys
import argparse
# test
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()

    if args.file == None:
        print('Too few command-line arguments')
        sys.exit(1)

    if args.file.endswith('.py') and args.file != None:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                file = list(f)
            file_copy = []
            for x in file:
                if not x.strip().startswith('#') and x.strip():
                    file_copy.append(x)
            print(len(file_copy))

        except FileNotFoundError:
            print('File does not exist')
            sys.exit(1)

    else:
        print('Not a python file')
        sys.exit(1)

if __name__ == '__main__':
    main()






