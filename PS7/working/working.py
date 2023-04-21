import re

def main():
    print(convert(input("Hours: ")))

def convert(s: str) -> str:
    if not isinstance(s, str) or 'to' not in s:
        raise ValueError

    result = re.findall(r'[1]?[0-9]{1}[:]?[0-5]?[0-9]?\s[AP]M', s)

    if not result:
        raise ValueError

    modified_time = []
    for x in result:
        time, meridian = x.split(' ')
        if ':' in time:
            hour, minute = time.split(':')
        if ':' not in time:
            hour = time
            minute = '00'

        if int(hour) > 12 or int(hour) < 0 or int(minute) >= 60 or int(minute) < 0:
            raise ValueError

        if meridian == 'PM':
            if hour != '12':
                hour = int(hour) + 12
        elif meridian == 'AM':
            if len(hour) < 2:
                hour = f'0{hour}'
            if hour == '12':
                hour = '00'

        x = f'{hour}:{minute}'
        modified_time.append(x)
    return f'{modified_time[0]} to {modified_time[1]}'

if __name__ == "__main__":
    main()