from typing import Dict
import re
import random

def main()->None:
    file_name = 'acronyms_list'
    all_acronyms = get_all_acronyms(file_name)
    for i in range(10):
        key = random.choice(list(all_acronyms))
        print("{}:".format(key), end='')
        process_answer(all_acronyms[key], input())
    print("PRACTICE SESSION OVER!")


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


if __name__ == '__main__':
    main()
