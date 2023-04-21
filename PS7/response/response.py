import validators

def main():
    email = input("What's your email address? ")
    result = validators.email(email)
    if result:
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()