# 시간 초과
def solution(numbers):
    answer = []  # 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열
    N = len(numbers)

    # 정수 배열 순회하면서 뒷 큰수 구하기
    for i in range(N):
        found = False  # 뒷 큰수 찾았는 지 여부
        # 뒷 큰수 찾기
        for j in range(1, N - i):
            if numbers[i] < numbers[i + j]:  # 뒷 큰수라면
                answer.append(numbers[i + j])
                found = True  # 뒷 큰수 찾았다!
                break
        # j for문을 끝까지 순회+뒷 큰수가 없다 => -1 할당
        if not found:
            answer.append(-1)

    return answer

numbers=[2, 3, 3, 5]
result = solution(numbers)
print(result) # [3, 5, 5, -1]
