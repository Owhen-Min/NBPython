# 시간초과

def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    for front in range(length):
        for rear in range(front + 1, length):
            if numbers[front] < numbers[rear]:
                answer[front] = numbers[rear]
                break
    return answer