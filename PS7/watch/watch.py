import re
import sys


def main():
    print(parse(input("HTML: ")))
    #print(parse('''<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'''))
def parse(s):
    # result = re.search(r"youtube\.com\/embed\/[a-zA-Z0-9_-]+",s)
    result = re.search(r'''src="http[s]?:\/\/[w]{,3}[.]?youtube\.com\/embed\/[a-zA-Z0-9_-]+''', s)
    if result:
        url = result.group().split('/')
        yt_id = url[-1]
        return f'https://youtu.be/{yt_id}'
    return None

if __name__ == "__main__":
    main()