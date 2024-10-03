def solution(numbers):
    answer = [-1] * len(numbers)  # 최종 결과 배열 // 초기값 : -1
    stack = []

    for i in range(len(numbers)):
        # 현재 숫자(numbers[i])가 스택의 최상단 인덱스의 숫자보다 클 경우
        while stack and numbers[i] > numbers[stack[-1]]:
            # 뒷 큰수를 찾으면 // 스택 안에 있는 값 = 뒷 큰수보다 작은 값들
            answer[stack.pop()] = numbers[i]  # 스택에서 pop한 해서 뒷 큰수 저장
        stack.append(i)  # 현재 순회의 인덱스를 스택에 쌓기 // 뒷 큰수를 찾지 못한 인덱스 저장

    return answer

# numbers = [2, 3, 3, 5]
# result = solution(numbers)
# print(result)  # [3, 5, 5, -1]
