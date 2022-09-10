# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
#
# 1 ≤ left ≤ right ≤ 1,000

def isCount(number):    # 약수의 개수를 리턴
    cnt = 0
    for i in range(1 ,number+1):
        if number % i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if isCount(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer