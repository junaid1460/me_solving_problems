from collections import defaultdict
import itertools as it
import math
math.inf = float('Inf')
def inf():
    return math.inf
# n = 3
def infdict():
    return defaultdict(inf)




path = defaultdict(defaultdict)
def floyd(dist, v):
    for i in range(v):
        for j in range(v):
            for k in range(v):
                dist[j][k] = min(dist[j][i] + dist[i][k], dist[j][k])
                
                    
    return dist

t = int(input())
for _ in range(t):
    n = int(input())
    cc = defaultdict(infdict)
    ff = defaultdict(infdict)
    for i in range(n):
        cc[i][i], ff[i][i] = 0, 0
        
    c = []
    f = []
    for _ in range(5):
        c.append(list(map(int, input().strip().split())))
    for _ in range(5):
        f.append(list(map(int, input().strip().split())))
    for i,j,w in c:
        i, j = i-1, j -1
        cc[i][j] = w
        cc[j][i] = w
    for i,j,w in f:
        i, j = i-1, j -1
        ff[i][j] = w
        ff[j][i] = w
        
    cc = floyd(cc, n)
    ff = floyd(ff, n)
    count = 0
    for i, j in it.combinations(range(n), 2):
        count += min(cc[i][j], ff[i][j])
    print(count)