#!/usr/bin/env python3
import unicodedata
import os
import re

def convert_to_nfc(string):
    return unicodedata.normalize('NFC', string)

# Hangul checker from chandong83/python_hangul_check_fucntion
def ishangul(string):
    hangul_count = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', string))
    return hangul_count > 0

def change_name(root, name, new_name):
    src = os.path.join(root, name)
    dst = os.path.join(root, new_name)
    os.rename(src, dst)
    print(f'Changed: {src}')

def fix_filenames():
    counter = 0
    # current_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(current_dir):
        dirs_and_files = dirs + files
        for name in dirs_and_files:
            new_name = convert_to_nfc(name)
            if ishangul(new_name):
                counter += 1
                change_name(root, name, new_name)

    print(f'{counter} changes made!')


if __name__ == '__main__':
    fix_filenames()
