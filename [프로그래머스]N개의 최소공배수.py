# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
#
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.

def GCD(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        arr[i+1] = (arr[i] * arr[i+1]) // GCD(a, b)
    return arr[-1]

# 두개씩 짝을 지어서 최소공배수를 구하는 방식으로 누적 개념을 활용했다.
# arr = [2, 6, 8, 14]

# 2와 6의 최소공배수를 구해서 값을 갱신하면 다음과 같다. => [2, 6, 8, 14]
# 6과 8의 최소공배수를 구해서 값을 갱신하면 다음과 같다. => [2, 6, 24, 14]
# 24와 14의 최소공배수를 구해서 값을 갱신하면 다음과 같다. => [2, 6, 24, 168]
