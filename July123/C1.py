t = int(input())

for _ in range(t):
    res = ""
    for i in range(8):
        a = input()
        for j in a:
            if j!='.':
                res+=j
    print(res)
                
