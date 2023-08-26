t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    mini = min(arr)
    maxi = max(arr)
    if mini == maxi:
        print(-1)
    else:
        b = []
        c = []
        for i  in arr:
            if i==maxi:
                c.append(i)
            else:
                b.append(i)
        print(len(b),len(c))
        print(*b)
        print(*c)
            
