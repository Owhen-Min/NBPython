def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()

        if stack:
            answer[i] = stack[-1]

        stack.append(numbers[i])

    return answer
