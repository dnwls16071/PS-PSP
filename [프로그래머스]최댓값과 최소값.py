# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
#
# s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

def solution(s):
    s = s.split(" ")
    answer = ""
    lst = []
    for i in s:
        lst.append(int(i))
    lst.sort()
    answer += str(lst[0])
    answer += " "
    answer += str(lst[-1])
    return answer

def solution(s):
    s = list(map(int, s.split(" ")))
    return str(min(s)) + " " + str(max(s))

# list(map(int, input().split())) => 입력값을 공백을 기준으로 리스트에 정수형으로 저장하는 코드문
# list(map(int, s.split(" "))) => 리스트 s를 공백을 기준으로 정수형으로 저장하는 코드문
