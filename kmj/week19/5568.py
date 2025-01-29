# 카드 놓기

# dfs 재귀(k,방문표시)를 사용해서 카드를 k번 뽑고
# 만들 수 있는 정수 조합을 중복없이(set) 저장하고 조합 갯수(len()) 출력

n = int(input())  # 총 카드 개수
k = int(input())  # 뽑을 카드 개수
n_list = [int(input()) for _ in range(n)]  # 카드 리스트
# print(n_list)

result_list = set() # 만들 수 있는 카드의 경우 / 중복 제거
visited = [0]*n # 방문 표시로 경우의 수 찾기

# 재귀 : 지금까지 카드 뽑은 횟수, 지금까지 뽑은 카드로 만든 나열된 정수
def dfs(K,num_string):
    # 종료 조건 : 뽑은 카드가 k가 됐냐?? -> k 횟수만큼 뽑혀야함
    if K == k:
        result_list.add(num_string) # 완성된 숫자 조합 저장
        return

    # 카드를 뽑자
    for i in range(n):
        if not visited[i]: # 카드 중복 선택 방지
            visited[i] = 1 # 방문 표시 -> 사용했다~~
            dfs(K+1,num_string+str(n_list[i]))
            visited[i] = 0  # 백트래킹: 현재 선택을 취소하고, 다음 경우의 수를 탐색하기 위해 방문 초기화


dfs(0,"")

print(len(result_list))
