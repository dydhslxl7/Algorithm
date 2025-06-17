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

# 코드 처리하기 => 홀짝에 따라 다른 값 반환하기 -> 삼항 연산자 : 조건에 따라 값을 선택하는 간단한 방법
def solution(code):
    mode = 0
    answer = ""
    for i in range(0, len(code)): # range, len 함수 사용법 확인
        if code[i] == "1":
            mode = 1 if mode == 0 else 0 # 삼항 연산자 사용
            continue
        if mode == 0 and i % 2 == 0: answer += code[i]
        elif mode == 1 and i % 2 != 0: answer += code[i]
    
    if answer == '': answer = "EMPTY"
    return answer

def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1 # XOR 연산자 사용
        else:
            if i % 2 == mode: # mode 홀짝에 따라 인덱스 선택
                answer += code[i]

    return answer if answer else 'EMPTY'
