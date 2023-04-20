def convert(input: str):
    return input.replace(':)', '🙂').replace(':(', '🙁')

def main():
    print(convert(input('>>> ')))

main()