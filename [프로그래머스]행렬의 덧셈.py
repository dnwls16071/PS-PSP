# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
#
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)
    return answer

def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer

# 이 문제를 풀면서 zip() 함수를 알게 되었다.
# zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

# ex. 예제
# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]
# for pair in zip(numbers, letters):
#     print(pair)

# (1, 'A')
# (2, 'B')
# (3, 'C')