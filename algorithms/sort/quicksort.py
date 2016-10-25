# Name: Quicksort (partition-exchange sort) algorithm.
# History: Tony Hoare, 1959
# Description:
#  1. select point in array - pivot
#  2. partition: move all less than pivot to left part,
#     all those greater - to the right
#  3. recursively repeat above steps
#  How to chose pivot and do partitioning greatly affects
#  on algorithm performance. There are two main approaches:
#    1. Lomuto partitioning scheme
#       1.
#    2. Hoare partitioning scheme:
#       1.
# Specifics:
#  * device & conquer
#  * in-place sort (uses the same container for sorting
#    result or no auxilary data structures involved during the sort)
#  * low memory consumption
#  * main competitors: merge sort, heapsort
#  * not a stable sort (dont preserve original order if criterion equals)
#  * complexity: B: O(n*log(n))-A: O(n*log(n))-W: O(n^2) (when already sorted)


import random


def lomuto_quicksort(a, lo, hi):
    if lo < hi:
        p = lomuto_partition(a, lo, hi)
        lomuto_quicksort(a, lo, p - 1)
        lomuto_quicksort(a, p + 1, hi)


def lomuto_partition(a, lo, hi):
    p = a[hi]  # always choose upper bound
    i = lo         # swap point
    for j in range(lo, hi):
        if a[j] <= p:
            swap(a, i, j)
            i += 1
    swap(a, i, hi)
    return i


def hoare_quicksort(a, lo, hi):
    if lo < hi:
        p = hoare_partition(a, lo, hi)
        hoare_quicksort(a, lo, p)
        hoare_quicksort(a, p + 1, hi)


def hoare_partition(a, lo, hi):
    p = a[lo]
    i = lo
    j = hi
    while True:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i >= j:
            return j
        swap(a, i, j)


def swap(a, i1, i2):
    global swaps
    c = a[i1]
    a[i1] = a[i2]
    a[i2] = c
    swaps = swaps + 1


unsorted = [random.randint(0, 1000) for r in range(1000)]
unsorted1 = list(unsorted)

swaps = 0
lomuto_quicksort(unsorted, 0, len(unsorted) - 1)
print("Lomuto sort swaps count = " + str(swaps))

swaps = 0
hoare_quicksort(unsorted, 0, len(unsorted) - 1)
print("Hoare sort swaps count = " + str(swaps))
