# 완전이진트리이므로 부모 노드는 노드 번호 // 2로 구할 수 있다.
_, n1, n2 = map(int,input().split())
ans = 0
while n1 != n2:
    n1= (n1+1)//2
    n2= (n2+1)//2
    ans += 1
print(ans)