#!/usr/local/bin/python3
'''Dictionary Program for birthdays entries and lookups'''

import json # for saving birthdays entries
import os
bday = {}

try:
    with open('data_file.json', 'r') as f: # create a new file if no files created
        bday = json.load(f)

except FileNotFoundError: # no files yet
        print('Ready for new files entry')


entry = True


def add_bday(k, v): # entry for dictionary
     bday[k] = v
     return bday


while entry:
    k = input('Enter name: ')
    if k in bday.keys():
        print('You already have this entry')
        y_n = input('Would you like to continue? y/n: ')
        if y_n != 'y':
            continue

    v = input('Enter birthday: ')
    d = add_bday(k, v)
    os.system('clear')
    print(d)
    with open('data_file.json', 'w') as f:  # save the entries  to a file
        json.dump(bday, f)
    yn = input('Entry one more Y/N: ')
    if yn != 'y':
        entry = False
        print('bye')

