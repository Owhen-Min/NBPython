t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    num_set = tuple(map(int, input().split()))
    print(f"#{test_case} {sum(num_set) / n:.20g}")