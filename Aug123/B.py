t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    d = {}
    s=0
    mini = float('inf')
    for i in range(n):
        m = int(input())
        arr = [int(x) for x in input().split()]
        firstmin = float('inf')
        secmin = float('inf')
 
        for i in range(m):
            if arr[i] < firstmin:
                secmin = firstmin
                firstmin = arr[i]
            elif arr[i] < secmin:
                secmin = arr[i]
        mini = min(mini,firstmin)
        d[firstmin]=secmin
        s+=secmin
    maxi = float('-inf')
    for i in d:
        maxi = max(maxi,mini+s-d[i])
    print(maxi)
            
        
