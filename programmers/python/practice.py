# 홀짝에 따라 다른 값 반환하기 -> range + sum : range 함수 사용법 확인
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

# 조건 문자열 -> eval : 문자열을 수식으로 변환하여 실행하는 함수
def solution(ineq, eq, n, m):
    if eq == "=" and n == m: return 1

    if ineq == "<" and n < m: return 1
    elif ineq == ">" and n > m: return 1

    return 0

def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n} {ineq}{eq} {m}'))

# 등차수열의 특정한 항만 더하기 -> enumerate : 반복 가능한 객체를 순회할 때 (인덱스, 값) 형태로 반환
def solution(a, d, included):
    answer = 0
    for index, flag in enumerate(included):
        if flag: answer += a + (d * index)
    return answer