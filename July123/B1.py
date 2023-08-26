import heapq

t = int(input())

for _ in range(t):
    h = []
    n = int(input())
    for i in range(n):
        wlen , q = [int(x) for x in input().split()]
        heapq.heappush(h,[-q,wlen,i+1])
    while h:
        q,w,i = heapq.heappop(h)
        if w <= 10:
            print(i)
            break
        else:
            continue
        
        
