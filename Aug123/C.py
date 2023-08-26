t = int(input())

for _ in range(t):
    n = int(input())
    curr = 0
    for i in range(n-1,-2,-1):
        l= 0
        mx = 0
        cnt = 1
        h = n
        st = 1
        for j in range(i+1):
            l += cnt*st
            mx = max(cnt*st, mx)
            st += 1
            cnt += 1
        for j in range(i+1, n):
            l += cnt*h
            mx = max(cnt*h, mx)
            h -= 1
            cnt += 1
        curr = max(curr, l-mx)
    print(curr)
