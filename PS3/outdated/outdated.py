def main():
    while convert(input("Date: ")) == 0:
        pass

def convert(date):
    date = date.replace('"', '').strip()
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    if '/' in date:
        date = date.split('/')
        if len(date[0]) > 2:
            return 0
        if int(date[0]) <= 12 and int(date[1]) <= 31 and len(date[2]) == 4:
            for n in range(2):
                date[n] = check_date(date[n])
            print("{}-{}-{}".format(date[2], date[0], date[1]))
            return 1
        else:
            return 0
    elif ',' in date:
        date = date.split(' ')
        for m in months:
            if m in date[0]:
                if len(date[1]) == 2:
                    date[1] = f'0{date[1][:1]}'
                elif len(date[1]) == 3:
                    date[1] = date[1][:2]

                date[1] = check_date(date[1])
                if date[1] == 0:
                    return 0
                if (months.index(m) + 1) < 10:
                    date[0] = f'0{months.index(m) + 1}'
                else:
                    date[0] = months.index(m) + 1
                print("{}-{}-{}".format(date[2], date[0], date[1]))
                return 1
        return 0
    else:
        return 0

def check_date(day):
    if int(day) > 31:
        return 0
    if int(day) < 10 and not day.startswith('0'):
        return f'0{day}'
    return day
main()