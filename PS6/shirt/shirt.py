import sys
import os.path
from PIL import Image, ImageOps

def main():
    if check_arg():
        wear_shirt(sys.argv[1], sys.argv[2])

def check_arg():
    file_formats = ('.jpg', '.jpeg', '.png')
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit(1)
    elif not sys.argv[1].lower().endswith(file_formats) or not sys.argv[2].lower().endswith(file_formats):
        print('Invalid input')
        sys.exit(1)
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        print('Input and output have different extensions')
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f'Input does not exist')
        sys.exit(1)
    else:
        return True

def wear_shirt(person, image):
    sh = Image.open('shirt.png')
    p = Image.open(person)
    rs_person = ImageOps.fit(p, sh.size)

    rs_person.paste(sh, sh)

    rs_person.save(image)

if __name__ == '__main__':
    main()