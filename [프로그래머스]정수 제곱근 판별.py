# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
#
# n은 1이상, 50000000000000 이하인 양의 정수입니다.

import math

def solution(n):
    lst = list(range(7071068))
    if math.sqrt(n) in lst:
        return (math.sqrt(n)+1)**2
    else:
        return -1

# 이런 풀이는 시간복잡도가 커져서 좋지 못한 코드가 된다.
# 정수 제곱근 판별의 테크닉은 다음과 같다.

def solution(n):
    sqrt = n ** 0.5

    if sqrt % 1 == 0:   # 이 말인즉슨, sqrt의 값이 정수냐 소수냐를 묻는 것
        return (sqrt+1)**2
    return -1