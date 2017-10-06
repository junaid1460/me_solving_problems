import heapq
t = int(input())
def getZipIter(it):
    it1 = iter(it)
    it2 = iter(it)
    next(it2)
    return zip( it2, it1)
def dfs(g, src, depth, value):
    # print(src, depth)
    if src + 1 == depth:
        t = max(g[src + 1])
        return abs( t - value) * (src + 1)
    else:
        m = 0
        # print(g[src + 1])
        for s, o in g[src + 1]:
            t = abs(s - value) * (src +1)
            m = max(m, t + dfs(g, src + 1, depth, o))
        return m
    
for _ in range(t):
    n = int(input())
    # print(n)

    dishes = []
    for _ in range(n):
        tmp = list(map(int, input().strip().split()))
        dishes.append(tmp)
    
    dishes_ = [dishes[0] ]+ list(map(lambda dish:list(getZipIter([dish[-1]] + dish)), dishes[1:-1])) + [dishes[-1]]
    # print(dishes_)

    print(dfs(dishes_, 0 , len(dishes_) -1, min(dishes[0])))



        # print(max(getZipIter(dish)),min(getZipIter(dish)))

        # print(dish, newdish)
    # print("-"*50)


