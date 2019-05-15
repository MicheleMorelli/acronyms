'''
Simple program to help remember the networking/TCP/IP/Internet-related acronyms.
-Michele Morelli, May 2019-
'''

import os
from typing import Dict
import re
import random

ROUNDS = 10
PATH = os.path.dirname(os.path.realpath(__file__))
DATA = "{}/acronyms_list".format(PATH)


def get_all_acronyms(file_name: str)->Dict[str, str]:
    lines = []
    with open(file_name, 'r') as f_h:
        lines = list(filter(lambda x: re.search('^.*?=.*?.$', x), f_h.readlines()))
    acronyms = [tuple(re.split('=', line)) for line in lines]
    return {k.strip(): v.strip() for k, v in acronyms}


def process_answer(answer: str, inp: str)->None:
    #normalising strings to ensure that 'hypertext', 'hyper text' and
    #'hyper-text' match
    normalise = lambda string: re.sub('[ -]', "", string).lower()
    if normalise(inp) == normalise(answer):
        print("-------> CORRECT!")
    else:
        print("-------> WRONG! CORRECT ANNSWER: {}".format(answer))
    print_line("=")


def print_line(char: str)->None:
    print("{}\n".format(char*20))


def print_title()->None:
    print_line("/")
    print("IWT ACRONYMS PRACTICE\n")
    print_line("/")


def run(all_acronyms: Dict[str, str])->None:
    print_title()
    for i in range(ROUNDS):
        key = random.choice(list(all_acronyms))
        print("{}:".format(key), end='')
        process_answer(all_acronyms[key], input())
    print("\nPRACTICE SESSION OVER!\n")


def main()->None:
    all_acronyms = get_all_acronyms(DATA)
    run(all_acronyms)


if __name__ == '__main__':
    main()
