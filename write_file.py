import random
import string

stringa = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9999))

def write_file(stringa):
    with open('activity.txt', 'w') as file:
        file.write(stringa)