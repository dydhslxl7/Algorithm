# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    for query in queries:
        temp = []
        for i in arr[query[0]:query[1]+1]:
            if i > query[2]: temp.append(i)
        answer.append(-1 if len(temp) == 0 else min(temp))
    return answer

def solution(arr, queries):
    answer = []
    for s, e, k in queries: # 변수 언패킹 사용법 숙지
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

# 수열과 구간 쿼리 3
def solution(arr, queries):
    answer = []
    temp = 0
    for i, j in queries:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr

def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a] # 변수 언패킹 사용법 숙지
    return arr

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    return ((x1 or x2) and (x3 or x4))

def solution(x1, x2, x3, x4):
    return ((x1 | x2) & (x3 | x4)) # 비트 연산자

# 글자 이어 붙여 문자열 만들기 -> join과 문자열 인덱싱
def solution(my_string, index_list):
    answer = ''.join(my_string[i] for i in index_list)
    return answer

# 문자열 여러번 뒤집기
def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for i, j in queries:
        # my_string[i:j+1] = reversed(my_string[i:j+1])
        my_string[i:j+1] = my_string[i:j+1][::-1]  # 문자열 슬라이싱과 역순
    return ''.join(my_string)

# 접미사 배열
"""
* sorted()와 sort()의 차이점에 대해 알아보자!
sorted()는 원본 리스트를 건드리지 않고 정렬된 새 리스트를 반환
sort()는 원본 리스트를 직접 정렬해서 None을 반환해
둘 다 파이썬에서 엄청 최적화된 정렬 알고리즘(Timsort)을 사용해서 시간 복잡도는 O(n log n)으로 거의 비슷해. 그러니까 성능 걱정은 안 해도 돼! 
결론적으로, 원본을 바꾸고 싶으면 sort()를 쓰고, 원본은 그대로 두고 정렬된 새 버전을 얻고 싶으면 sorted()를 쓰면 돼! 상황에 맞게 잘 골라 쓰면 된다!
"""
def solution(my_string):
    answer = []
    for i in range(0, len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

# 접미사인지 확인하기 -> -len()
def solution(my_string, is_suffix):
    answer = 0
    if my_string[-len(is_suffix):] == is_suffix:
        answer = 1
    return answer

# 배열 만들기 2
def solution(l, r):
    answer = []
    cnt = 1
    while True:
        n = int(bin(cnt).replace('0b', '')) * 5 # 2진수로 변환 후 '0b' 제거하고 5를 곱함
        cnt += 1
        if l <= n <= r:
            answer.append(n)
        elif n > r:
            break
    return answer if len(answer) != 0 else [-1]

def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']): # set을 사용하여 숫자에 '0'과 '5'만 있는지 확인
            answer.append(num)
    return answer if answer else [-1]

# 접두사인지 확인하기 -> startswith()
def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0

# 문자열 뒤집기 -> [::-1]
def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

# 세로 읽기 -> [c-1::m]
def solution(my_string, m, c):
    answer = ''
    while my_string != '':
        answer += my_string[0:m][c-1]
        my_string = my_string[m:]  # 슬라이싱과 문자열 인덱싱
    return answer

def solution(my_string, m, c):
    return my_string[c-1::m]

# qr code -> 풀이 2
def solution(q, r, code):
    return code[r::q]