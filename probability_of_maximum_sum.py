"""
in an array A of integers, find probabilty that two chosen elements sums upto maximum.
where index of element i < element j. 

"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    m, sm = -1, -1
    for i in a :
        if m < i:
            sm = m
            m = i
            continue
        if sm < i:
            sm = i
    m, sm
    count  = 0
    if sm == m:
        for i in a:
            if i == m or i == sm:
                count += 1
        p = (count * ( count - 1)) / 2
    else:
        cm, csm = 0, 0
        for i in a:
            if i == m:
                cm += 1
            if i == sm:
                csm += 1
    #     print(cm, csm)
        p = max(cm, csm)
    t = (n * ( n -1 )) / 2

    print("{:.8f}".format(p/t))

