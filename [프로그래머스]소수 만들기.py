# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 반환하는 함수
def solution(nums):
    cnt = 0
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            for c in range(b+1, len(nums)):
                answer = nums[a] + nums[b] + nums[c]
                if isPrime(answer):
                    cnt += 1
    return cnt

# 소수를 판별하는 함수
def isPrime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
            break
    return True