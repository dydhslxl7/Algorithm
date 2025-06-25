# 수열과 구간 쿼리 4
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i == 0 or i % k == 0:
                arr[i] += 1
    return arr

# 카운트 업
def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

def solution(start, end):
    return list(range(start, end + 1)) # list 함수

# 콜라츠 수열 만들기
def solution(n):
    answer = [n]
    while(n > 1):
        n = n//2 if n%2==0 else n*3+1
        answer.append(n)
    return answer

# 9로 나눈 나머지
def solution(number):
    return int(number) % 9

# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        n = int(i[s:s+l])
        if n > k:
            answer.append(n)
    return answer

# 배열 만들기 4
def solution(arr):
    stk = [arr[0]]
    n = 1 
    while n < len(arr):
        if len(stk) == 0 or arr[n] > stk[-1]:
            stk.append(arr[n])
            n += 1
        else:
            stk.pop()
    return stk

# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i, str in enumerate(my_strings):
        answer += str[parts[i][0] : parts[i][1]+1]
    return answer

# 문자열의 뒤의 n글자
def solution(my_string, n):
    answer = my_string[-n:]
    return answer

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# qr code -> 풀이 1
def solution(q, r, code):
    answer = ''
    for k, v in enumerate(code):
        if k % q == r:
            answer += v
    return answer

# 문자 개수 세기 -> 풀이 1
def solution(my_string):
    answer = []
    ascii = 65
    while ascii < 123:
        answer.append(my_string.count(chr(ascii)))
        if ascii == 90:
            ascii += 7
        else: 
            ascii += 1
    return answer