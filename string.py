from collections import Counter

    
def answer():
    n, m = list(map(int, input().strip().split()))
    mat = []
    for _ in range(n):
        mat.append(Counter(input().strip()))
    s = str(input().strip())
    i = 0
    # print(mat)
    for e in s:
        if e in mat[i] and mat[i][e] > 0 :
            mat[i].subtract(e)
        else:
            print('No')
            return
        i = (i + 1) % n
    print('Yes')



t = int(input())
for _ in range(t):
    answer()