def check_permutation(prefix_sums):
    n = len(prefix_sums) + 1
    max_sum = sum(range(1, n + 1))
    current_sum = 0

    for i, prefix_sum in enumerate(prefix_sums):
        current_sum += i + 1
        if prefix_sum != current_sum:
            return "NO"

    # Check if the last prefix sum is missing or exceeds the maximum possible sum
    last_sum = max_sum - current_sum + prefix_sums[-1]
    if last_sum < 1 or last_sum > n:
        return "NO"

    return "YES"

# Read input and process each test case
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        prefix_sums = list(map(int, input().split()))
        print(check_permutation(prefix_sums))

if __name__ == "__main__":
    main()
