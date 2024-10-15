### 내장모듈을 이용한 방법
# 기본값을 설정해주지 않고 사용
# math모듈을 통해 반복문을 통해 곱연산하는 과정 생략

from collections import defaultdict
import math
def solution(clothes):
    costumes = defaultdict(lambda :1)
    for _, cloth_type in clothes:
        costumes[cloth_type] += 1
    answer = math.prod(costumes.values()) - 1
    return answer