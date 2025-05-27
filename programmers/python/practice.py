# 홀짝에 따라 다른 값 반환하기 -> range + sum
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

# 조건 문자열 -> eval
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