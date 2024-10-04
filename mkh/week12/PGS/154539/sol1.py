def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    l_n = numbers[n-1]
    for i in range(n-1, -1, -1):
        if numbers[i] >= l_n:
            l_n = numbers[i]
            continue
        for j in range(i, n):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
    return answer