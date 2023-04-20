import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    for x in string.punctuation:
        if x in s:
            return False
    for x in string.digits:
        if x in s[0:1]:
            return False
    if len(s) > 2:
        check = s[2:]
        if check.isalpha():
            return True
        if check.endswith(string.ascii_letters):
            return False
        alpha_index = -1
        num_index = []
        for c, x in enumerate(check):
            if x.isalpha():
                alpha_index = c
            if x.isdigit():
                num_index.append(c)
        if int(check[num_index[0]]) == 0:
            return False
        for n in num_index:
            if n < alpha_index:
                return False
    return True

if __name__ == '__main__':
    main()