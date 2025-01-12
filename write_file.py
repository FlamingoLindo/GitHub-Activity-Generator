import random
import string

def write_file():
    stringa = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9999))
    with open('activity.txt', 'w') as file:
        file.write(stringa)