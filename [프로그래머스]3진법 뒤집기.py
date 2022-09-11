# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
#
# n은 1 이상 100,000,000 이하인 자연수입니다.

def conv(n):
    answer = []
    while n > 0:
        answer.append(n % 3)
        n //= 3
    return answer

def solution(n):
    val = conv(n)
    total = 0
    for i in range(len(val)):
        total += int(val[i]) * (3 ** (len(val) - i - 1))
    return total