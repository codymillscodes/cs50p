import requests
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(prog='bitcoin')
    parser.add_argument('n', nargs='?', default = -1)

    args = parser.parse_args()
    if args.n == -1:
        print('Missing command-line argument')
        sys.exit(1)
    try:
        n = float(args.n)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        btc_price = r['bpi']['USD']['rate_float']
        print(f'${(btc_price * n):,.4f}')
    except requests.RequestException:
        print('404')
        sys.exit(1)

if __name__ == '__main__':
    main()