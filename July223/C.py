def check_path(n, arr):
    st = set(range(1, n + 1))
    st.discard(n)

    fl = 1
    left = -1

    if arr[0] in st:
        st.discard(arr[0])
    else:
        if left == -1:
            left = arr[0]
        else:
            fl = 0

    for i in range(1, n - 1):
        diff = arr[i] - arr[i - 1]
        if diff in st:
            st.discard(diff)
        else:
            if left == -1:
                left = diff
            else:
                fl = 0
                break

    if fl == 0:
        return "NO"
    else:
        total_sum = sum(st)
        if left == -1:
            req_sum = n * (n + 1) // 2
            if req_sum - arr[n - 2] == total_sum:
                return "YES"
            else:
                return "NO"
        else:
            if total_sum == left:
                return "YES"
            else:
                return "NO"


# Test cases
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = check_path(n, arr)
    print(result)
