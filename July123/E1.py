import math
def equationroots( a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
     
    if dis > 0:
        a = (-b + sqrt_val)/(2 * a)
        b = (-b - sqrt_val)/(2 * a)
        return a,b
     
    else:
        return -b / (2 * a),-b / (2 * a)
     
t = int(input())

for _ in range(t):
    n,c = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    l = len(arr)
    a = l
    b = sum(arr)
    c1 = 0

    for i in arr:
        c1+=i*i
    c = c - c1
    print(a,b,c)
    root1,root2 = equationroots(a,b,c)
    #root1,root2 = math.ceil(root1),math.ceil(root2)
    print(root1,root2)
    
