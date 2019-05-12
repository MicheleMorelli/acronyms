import os
from typing import Dict
import re
import random

ROUNDS = 10
PATH = os.path.dirname(os.path.realpath(__file__))
DATA = "{}/acronyms_list".format(PATH)

def get_all_acronyms(file_name:str)->Dict[str,str]:
    all_acronyms={}
    with open(file_name, 'r') as fh:
        for line in fh.readlines():
            if (re.search('^.*?=.*?.$',line)):
                acronym, meaning = re.split('=',line)
                all_acronyms[acronym.strip()] = meaning.strip()
    return all_acronyms


def process_answer(answer:str, inp:str)->None:
    if (inp.lower() == answer.lower()):
        print("-------> CORRECT!")
    else:
        print("-------> WRONG! CORRECT ANNSWER: {}".format(answer))

    print("{}\n".format("="*20))


def print_title()->None:
    print("{}\n".format("+"*20))
    print("IWT ACRONYMS PRACTICE\n")
    print("{}\n".format("+"*20))


def run(all_acronyms:Dict[str,str])->None:
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
