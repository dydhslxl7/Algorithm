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