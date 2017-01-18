import sys

def mean(arr):
    sum = 0
    n = len(arr)
    for e in arr: sum += e
    return sum / n

def median(arr):
    arr.sort()
    n = len(arr)
    d, m = divmod(n, 2)
    if (m != 0): return arr[d]
    return (arr[d - 1] + arr[d]) / 2

def mode(arr):
    pop = {}
    n = len(arr)
    arr.sort()
    for e in arr:
        k = str(e)
        if k in pop: pop[k] += 1
        else: pop[k] = 1
    srt = sorted(pop.items(), key=lambda x: (-x[1], int(x[0])))
    return int(srt[0][0])

def median(arr):
    d, m = divmod(len(arr), 2)
    if (m == 0):
        med = (arr[d-1] + arr[d]) / 2
    else:
        med = arr[d]
    return round(med)

def get_quartiles(arr):
    arr.sort()
    n = len(arr)
    d, m = divmod(n, 2)
    if (m != 0):
        upper_left_bound = d + 1
    else:
        upper_left_bound = d

    q1 = median(arr[0:d])
    q2 = median(arr)
    q3 = median(arr[upper_left_bound:n+1])

    return [q1, q2, q3]

def interquartile_range(arr):
    q = get_quartiles(arr)
    return q[2] - q[0]

def get_s(x, f):
    s = []
    
    for i in range(len(x)):
        for j in range(f[i]):
            s.append(x[i])
            
    s.sort()
    return s