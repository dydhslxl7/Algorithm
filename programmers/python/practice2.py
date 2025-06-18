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