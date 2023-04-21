import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    result = re.search(r'\d+\.\d+\.\d+\.\d+', ip)
    if result:
        ip = ip.split('.')
        if len(ip) > 4:
            return False
        for i in ip:
            i = int(i)
            if i < 0 or i > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()