t = int(input())

for _ in range(t):
    a = [int(x) for x in input().split()]
    a.sort()
    if a[1]+a[2]>=10:
        print("YES")
    else:
        print("NO")
