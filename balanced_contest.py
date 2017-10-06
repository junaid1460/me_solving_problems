t = int(input())
for _ in range(t):
    n, p = list(map(int, input().strip().split()))
    elms = list(map(int, input().strip().split()))
    p = p * 1.0
    hard = round(p / 10)
    cake = p / 2
    if cake - int(cake) >= 0.5:
        cake = int(cake) + 1

    # print(cake, hard)
    cakecount, hardcount = 0, 0
    for i in elms:
        if i >= cake:
            cakecount += 1
        elif i <= hard:
            hardcount += 1
    if hardcount == 2 and cakecount == 1:
        print('yes')
    else:
        print('no')
        