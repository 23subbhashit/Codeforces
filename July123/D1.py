t = int(input())

for _ in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    l = len(arr)
    if l==1:
        print(0)
    else:
        cnt = 1
        res = cnt
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] <=k:
                cnt+=1
            else:
                res = max(cnt,res)
                cnt = 1
        res = max(res,cnt)
        
        print(l - res)
                
                
    
