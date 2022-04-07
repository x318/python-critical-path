import random


class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_matrix(arr):
    for r in arr:
        for c in r:
            print(f"{col.OKGREEN}{c}", end=' '+col.ENDC)
        print(f'{col.FAIL} =', f"{sum(r)}{col.ENDC}")


def generate_tasks(n, m, lower, higher):
    return [[random.randint(lower, higher) for x in range(n)] for y in range(m)]


def generate_tasks1d(m, lower, higher):
    r = [[]]
    r.append([random.randint(lower, higher) for x in range(m)])
    return r
