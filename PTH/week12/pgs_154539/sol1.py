# def solution(numbers):
#     N = len(numbers)
#     answer = [-1] * N  # 결과를 담을 배열, 기본값은 -1
#
#     for i in range(N):
#         for j in range(i + 1, N):  # j는 i + 1부터 N까지
#             if numbers[i] < numbers[j]:
#                 answer[i] = numbers[j]
#                 break  # 더 큰 수를 찾으면 반복문 종료
#
#     return answer
#------------------------------------------------------------------------

# def solution(numbers):
#     answer = [-1]*len(numbers)
#     for i in range(len(numbers)-1,-1,-1):
#         for j in range(i-1,-1,-1):
#             if numbers[j] >= numbers[i]:    break
#             answer[j] = numbers[i]
#     return answer
#------------------------------------------------------------------------


def solution(numbers):
    N = len(numbers)
    answer = [-1] * N  # 결과를 담을 배열, 기본값은 -1
    stack = []  # 인덱스를 저장할 스택

    for i in range(N):
        # 현재 숫자가 스택의 마지막 인덱스의 숫자보다 클 때
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()  # 스택에서 인덱스를 꺼냄
            answer[idx] = numbers[i]  # 더 큰 숫자를 찾은 인덱스에 저장
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return answer





# 테스트 케이스
print(solution([2, 3, 3, 5]))  # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))  # [-1, 5, 6, 6, -1, -1]
