a = [7, 11, 9]
l = 0
r = len(a) - 1
count = 0
while l < r:
    i, j = r, l
    t = a[j]
    while j <= r:
        t = t & a[j]
        count += t
        j+= 1
    t = a[i]
    while i > l:
        t = t & a[i]
        count += t
        i -= 1
    # inc,dec
    l += 1
    r -= 1

        
if l == r:
    count += a[l]
    
print(count)