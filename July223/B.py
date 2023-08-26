t = int(input())


for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    odd = []
    even = []
    for i in arr:
        if i&1:
            odd.append(i)
        else:
            even.append(i)
    odd.sort()
    even.sort()
    newarr = []
    codd = 0
    ceven = 0
    for i in arr:
        if i&1:
            newarr.append(odd[codd])
            codd+=1
        else:
            newarr.append(even[ceven])
            ceven+=1
    if newarr == sorted(newarr):
        print("Yes")
    else:
        print("No")
