from utils import generate_tasks1d, print_matrix, generate_tasks, col
import os
import sys
import numpy as np

# critical path


def sort_crit_decrease(tasks, m, n):
    tasks = [j for sub in tasks for j in sub]
    tasks.sort()
    tasks.reverse()
    res = [[0 for x in range(0)] for y in range(n)]

    for task in tasks:
        load = [sum(el) for el in res]
        minind = load.index(min(load))
        res[minind].append(task)

    # print(tasks)
    # print_matrix(res)
    return res


def sort_crit_random(tasks, m, n):
    tasks = [j for sub in tasks for j in sub]
    res = [[0 for x in range(0)] for y in range(n)]

    for task in tasks:
        load = [sum(el) for el in res]
        minind = load.index(min(load))
        res[minind].append(task)

    # print(tasks)
    # print_matrix(res)
    return res


def sort_crit_increase(tasks, m, n):
    tasks = [j for sub in tasks for j in sub]
    tasks.sort()
    res = [[0 for x in range(0)] for y in range(n)]

    for task in tasks:
        load = [sum(el) for el in res]
        minind = load.index(min(load))
        res[minind].append(task)

    # print(tasks)
    # print_matrix(res)
    return res


# kron
def kron1(arr):
    load = [sum(el) for el in arr]
    delta = max(load)-min(load)
    minind = load.index(min(load))
    maxind = load.index(max(load))

    for el in arr[maxind]:
        if el < delta and el != 0:
            # arr[maxind].remove(el)
            arr[maxind][arr[maxind].index(el)] = 0
            arr[minind].append(el)
            # print("#THIS IS IT")
            # print_matrix(arr)
            # print("-----------")
            return False

    return True


def kron2(arr):
    load = [sum(el) for el in arr]
    delta = max(load)-min(load)
    minind = load.index(min(load))
    maxind = load.index(max(load))

    for i in range(len(arr[maxind])):
        for j in range(len(arr[minind])):
            if arr[maxind][i] - arr[minind][j] < delta and arr[maxind][i] > arr[minind][j] and arr[maxind][i] != 0 and arr[minind][j] != 0:
                t = arr[maxind][i]
                arr[maxind][i] = arr[minind][j]
                arr[minind][j] = t
                while not kron1(arr):
                    pass


def kron(arr):
    iters = 0
    while not kron1(arr):
        iters += 1
    print(iters)
    kron2(arr)


print('############################')
N = int(input('Enter device count:'))
M = int(input('Enter task count per device:'))
l = int(input('Enter lower limit:'))
h = int(input('Enter higher limit:'))
a = generate_tasks(M, N, l, h)
print("-----------------RANDOM---------------")
print_matrix(a)
kron(a)
print_matrix(a)
print("-----------------CRITICAL PATH DECREASE---------------")
a = sort_crit_decrease(a, M, N)
print_matrix(a)
kron(a)
print_matrix(a)
print("-----------------CRITICAL PATH RANDOM---------------")
a = sort_crit_random(a, M, N)
print_matrix(a)
kron(a)
print_matrix(a)
print("-----------------CRITICAL PATH INCREASE---------------")
a = sort_crit_increase(a, M, N)
print_matrix(a)
kron(a)
print_matrix(a)
