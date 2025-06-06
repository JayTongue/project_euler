from tqdm import tqdm
from math import prod

def main():
    answers = set()
    ref = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for a in tqdm(range(1, 100000)):
        for b in range(1, 10000):
            c = a*b
            digits = list(str(a)+str(b)+str(c))
            if len(digits) > 9:
                break
            if set(digits) == ref:
                answers.add(c)

    print(sum(answers))
main()
