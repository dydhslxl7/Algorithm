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

# 주사위 게임2 => 세 수의 연산 -> set : 중복된 값을 제거하고 고유한 값만을 저장하는 자료형
def solution(a, b, c):
    answer = a+b+c
    if len({a, b, c}) <= 2: answer *= a**2 + b**2 + c**2 # pow(a, 2) 대신 a**2 사용
    if len({a, b, c}) == 1: answer *= a**3 + b**3 + c**3 # pow(a, 3) 대신 a**3 사용
    return answer

# 원소들의 곱과 합 => !! eval과 sum 사용법 확인 !!
def solution(num_list):
    ans1 = 1
    ans2 = 0
    for i in num_list:
        ans1 *= i
        ans2 += i
    return 1 if ans1 < ans2**2 else 0

def solution(num_list):
    ans = 1
    for i in num_list:
        ans *= i
    return 1 if ans < sum(num_list)**2 else 0

def solution(num_list):
    s = sum(num_list)**2
    p = eval('*'.join([str(n) for n in num_list])) # eval과 join, str 사용법 숙지!!
    return 1 if s > p else 0

# 이어 붙인 수
def solution(num_list):
    n1 = ""
    n2 = ""
    for i in num_list:
        if i % 2 == 0: n1 += str(i)
        else: n2 += str(i)
    return int(n1) + int(n2)

# 마지막 두 원소 -> 배열의 -1, -2 인덱스 사용법 숙지
def solution(num_list):
    n = len(num_list)
    if num_list[n-2] < num_list[n-1]:
        num_list.append(num_list[n-1] - num_list[n-2])
    else:
        num_list.append(num_list[n-1]*2)
    return num_list

def solution(num_list):
    num_list.append(num_list[-1]-num_list[-2] if num_list[-1]>num_list[-2] else num_list[-1]*2)
    return num_list

# 수 조작하기
def solution(n, control):
    for i in control:
        if i == "w": n += 1
        elif i == "s": n -= 1
        elif i == "d": n += 10
        else: n -= 10
    return n

def solution(n, control):
    answer = n
    c = {'w':1, 's':-1, 'd':10, 'a':-10} # 딕셔너리 사용법 숙지
    for i in control:
        answer += c[i] # 딕셔너리에서 키를 통해 값에 접근
    return answer