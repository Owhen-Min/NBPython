# 모든 사람들은 각각 테이블에 둘러 앉은 사람들 중 `한 명`을 지목 (경로 1개)

def min_M(n, k, graph):
    visited = [False] * n
    current = 0
    count = 1 # 최소 횟수

    while not visited[current]:
        visited[current] = True
        next_person = graph[current]

        if next_person == k: # 보성이 만남
            return count # 영기가 말해야 하는 가장 작은 양의 정수 M

        current = next_person
        count += 1

    return -1  # 보성이 못 만남

# 참여자수 / 보성이 번호
n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]

print(min_M(n, k, graph))
