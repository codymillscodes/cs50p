import pyfiglet
import argparse
import random
import sys

def main():
    figlet = pyfiglet.Figlet()

    parser = argparse.ArgumentParser(prog='figlet')
    parser.add_argument('-f', '--font', dest='font')

    args = parser.parse_args()

    if args.font == None:
        font = random.choice(figlet.getFonts())
    else:
        try:
            font = figlet.setFont(font=args.font)
        except (NameError, pyfiglet.FontNotFound):
            print("Invalid usage")
            sys.exit(1)

    i = input("Input: ")
    print(figlet.renderText(i))
main()