# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
#
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

def solution(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        answer = True
    else:
        answer = False
    return answer

# 알아두면 좋은 파이썬 내장함수 정리

# isdigit() => 문자열이 숫자로만 이루어져있는지 확인하는 함수
# isalpha() => 문자열이 알파벳으로만 이루어져있는지 확인하는 함수
# isdecimal() => 문자열이 0부터 9 사이의 숫자로만 이루어져잇는지 판단하는 함수