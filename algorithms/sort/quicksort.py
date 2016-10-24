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


def quicksort(a, lo, hi):
    if lo < hi:
        p = lomuto_partition(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)


def lomuto_partition(a, lo, hi):
    pivot = a[hi]  # always chose upper bound
    i = lo         # swap point
    for j in range(lo, hi):
        if a[j] <= pivot:
            swap(a, i, j)
            i = i + 1
    swap(a, i, hi)
    return i


def swap(a, i1, i2):
    c = a[i1]
    a[i1] = a[i2]
    a[i2] = c


unsorted = [2, 1, 2, 5, 4]
quicksort(unsorted, 0, len(unsorted) - 1)

print(', '.join(str(x) for x in unsorted))
