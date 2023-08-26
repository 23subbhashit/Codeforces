t = int(input())
for _ in range(t):
    x,y,n = [int(x) for x in input().split()]
    arr = [y]*n
    c = 1
    for i in range(n-2,-1,-1):
        arr[i] = arr[i+1]-c
        c+=1
    if x<=arr[0]:
        arr[0] = x
        print(*arr)
    else:
        print(-1)
