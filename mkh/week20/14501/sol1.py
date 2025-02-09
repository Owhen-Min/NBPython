n = int(input())
tps = [list(map(int,input().split())) for _ in range(n)]

# 진행한 일차수, 마지막으로 상담이 끝난 날을 기록하는 last, 여태까지 얻은 이익을 기록하는 value
def dist_counsel(depth, last, value):
    if depth == n:
        return value
    # 이전에 맡은 일을 하는 중이라면
    if last > depth:
        return dist_counsel(depth+1, last, value)

    # 지금 맡을 수 있고, 퇴사하기 전에 일을 끝낼 수 있다면
    if depth + tps[depth][0] <= n:
        return max(dist_counsel(depth+1, depth+tps[depth][0], value+tps[depth][1]), dist_counsel(depth+1, last, value))
    return dist_counsel(depth+1, last, value)

ans = dist_counsel(0,0, 0)

print(ans)