n = int(input())
num = list(map(int, input().strip().split()))
print(len(num))
k = int(input())
num.sort()
dp = set()
def dfs(g, index, length, mcost, cost, depth):
    global dp
    if index == (length - 1) or cost + g[index] >= mcost:
        return (cost + g[index], depth)
    else:
        cost += g[index]
        dep =  -1
        ncos = cost
        for i in range(index +1, length):
            key = (i,cost,depth + 1)
            if key in dp:
                continue
            val, d = dfs(g, i, length, mcost,cost, depth + 1 )
            dp.add(key)
            if val == mcost and dep < d:
                dep = d
                cost = val
        return (cost, dep)


v, d = 0, -1
for i in range(len(num)):
    val, dep = dfs(num, i, len(num),k, 0, 1)
    if val == k and dep > d:
        d = dep
        v = val
print(d)