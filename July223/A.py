t = int(input())

for _ in range(t):
    n,m,k,H = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    cnt = 0
    for i in range(n):
        curr = abs(arr[i]-H)
        for j in range(1,m):
            if curr == j*k:
                #print(arr[i],H)
                cnt+=1
    print(cnt)
    
            
