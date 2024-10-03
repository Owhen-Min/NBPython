# 스택

def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    stack = []
    # 맨 마지막은 항상 -1이라는 점에서 힌트를 얻자
    for i in range(length - 1, -1, -1):
        # 뒤에서 부터 확인 했을 때 현재값이랑 비교했을 때 더 큰 것만 남길 것
        # 다시말해서 뒤에서 부터 봤을 때 현재 최대값
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        # 위 과정을 거쳤음에도 남아있다면 지금 값보다 크다는 것
        if stack:
            answer[i] = stack[-1]
        # 비교를 위해 일단 집어넣기
        stack.append(numbers[i])
    return answer