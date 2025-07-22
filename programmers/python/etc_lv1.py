# 크기가 작은 부분문자열
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer

# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    for i in range(count+1):
        answer += price * i
    return 0 if money - answer > 0 else abs(money - answer)

# 숫자 문자열과 영단어
def solution(s):
    num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for i in num_dic:
        if i in s:
            s = s.replace(i, str(num_dic[i]))
    return int(s)

# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    temp = 0
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(a, b+1):
        answer += i
    return answer

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    return answer if len(answer) > 0 else [-1]

# 같은 숫자는 싫어
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer