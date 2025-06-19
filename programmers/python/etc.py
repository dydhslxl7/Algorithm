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
