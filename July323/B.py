import heapq
import sys
sys.setrecursionlimit(100000)
t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    arr = []
    for i,x in enumerate(input().split()):
        heapq.heappush(arr,[-int(x),i+1])
        
    res = []
    while arr:
        h,ind = heapq.heappop(arr)
        h = -h
        h = h-k
        if h<=0:
            res.append(ind)
        else:
            heapq.heappush(arr,[-h,ind])
    print(*res)
