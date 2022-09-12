# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
#
# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    calendar = 0
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        calendar += months[i]
    calendar += b - 1
    calendar = calendar % 7
    return days[calendar]

# 달력 문제의 접근법은 다음과 같다.
# months 리스트를 통해 각 달의 일수를 저장하고 a월만큼 반복문으로 돌려준다.
# 그 다음 b-1일(왜냐면 1부터 시작하므로)만큼 더해준다.
# 마지막으로 일주일이 7일이므로 값을 7로 나눈 나머지에 대응시키면 된다.
