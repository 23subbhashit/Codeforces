import math
t = int(input())
for _ in range(t):
    n = int(input())
    ans = [n]
    if n%2 ==1:
        n-=1
        ans.append(n)
    while n!=2:
        temp = 1
        while n%(2*temp)==0:
            temp*=2
        if temp ==n:
            temp //=2
        n-=temp
        ans.append(n)
    ans.append(1)
    print(len(ans))
    print(*ans)
    
