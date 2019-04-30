# https://www.hackerrank.com/challenges/insertionsort1/problem


def insertion_sort_part_one(n, arr):
    idx = n - 1
    temp = arr[idx]
    while arr[idx - 1] > temp and idx > 0:
        arr[idx] = arr[idx - 1]
        print(' '.join(map(str, arr)))
        idx -= 1
    arr[idx] = temp
    print(' '.join(map(str, arr)))
    return arr
