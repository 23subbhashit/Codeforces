t = int(input())
for _ in range(t):
    b,c,h = [int(x) for x in input().split()]
    s = c+h
    if b<=s:
        res = 2*b-1
        print(res)
    else:
        res = s*2+1
        print(res)
        
    
