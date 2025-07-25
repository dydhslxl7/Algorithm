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

# 카운트 다운
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num-1, -1)]

# 리스트 자르기 -> 풀이 1
def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        answer = num_list[:slicer[1]+1]
    elif n == 2:
        answer = num_list[slicer[0]:]
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1]+1]
    else:
        answer = num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return answer

# 첫 번째로 나오는 음수 -> for문 돌리는 방법이 더 간단하고 불필요한 리스트 생성 안해도 됨
def solution(num_list):
    answer = [i for i in range(len(num_list)) if num_list[i] < 0]
    return answer[0] if len(answer) else -1

# 배열 조각하기
def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr

# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

# 순서 바꾸기
def solution(num_list, n):
    return num_list[n:]+num_list[:n]

# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

# n개 간격의 원소들
def solution(num_list, n):
    answer = []
    return num_list[::n]

# 홀짝에 따라 다른 합 구하기
def solution(num_list):
    return max(sum(num_list[0::2]), sum(num_list[1::2]))

# 5개씩
def solution(names):
    return names[::5]

# 할 일 목록
def solution(todo_list, finished):
    return [todo_list[k] for k, v in enumerate(todo_list) if not finished[k]]

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            break
    return answer

# 수열과 구간 쿼리 1
def solution(arr, queries):
    for s, e in queries:
        for k, v in enumerate(arr):
            if s <= k and k <= e:
                arr[k] += 1
    return arr

# 왼쪽 오른쪽
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
    return []

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    for k, v in enumerate(arr):
        if v >= 50 and v % 2 == 0:
            arr[k] = v // 2
        elif v < 50 and v % 2 != 0:
            arr[k] = v * 2
    return arr

# 1로 만들기
def solution(num_list):
    answer = 0
    for i in num_list:
        while i > 1:
            if i % 2 == 0:
                i //= 2
            else:
                i = (i - 1) // 2
            answer += 1
    return answer

# 길이에 따른 연산
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(str(i) for i in num_list))
    else:
        return eval('*'.join(str(i) for i in num_list))

# 대문자로 바꾸기    
def solution(myString):
    return myString.upper()

# 소문자로 바꾸기
def solution(myString):
    return myString.lower()

# 배열에서 문자열 대소문자 변환하기
def solution(myString):
    myString = myString.lower()
    flag = myString.find('a')
    while flag > -1:
        myString = myString[:flag] + 'A' + myString[flag+1:]
        flag = myString.find('a', flag+1)
    return myString

# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    flag = myString.rfind(pat)
    return myString[:flag+len(pat)]

# ad 제거하기
def solution(myString, pat):
    cnt = 0
    flag = myString.find(pat)
    while flag > -1:
        myString[flag:len(pat)]
        cnt += 1
        flag = myString.find(pat, flag+1)
    return cnt

# 공백으로 구분하기2 -> 빈 배열 제거
def solution(my_string):
    return [i for i in my_string.split(' ') if i != '']

# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for k, v in enumerate(strArr):
        if k % 2 != 0:
            strArr[k] = v.upper()
        else:
            strArr[k] = v.lower()
    return strArr

# ad 제거하기
def solution(strArr):
    return [v for v in strArr if 'ad' not in v]

# x 사이의 개수
def solution(myString):
    return [len(i) for i in myString.split('x')]

# 문자열 잘라서 정렬하기
def solution(myString):
    myString = [i for i in myString.split('x') if i != '']
    myString.sort()
    return myString

# 간단한 식 계산하기
def solution(binomial):
    return eval(binomial)

# rny_string
def solution(rny_string):
    return rny_string.replace('m', 'rn')

# 세 개의 구분자
def solution(myStr):
    newStr = [i for i in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ') if i != '']
    return newStr if newStr else ['EMPTY']

# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer

# 무작위로 K개의 수 뽑기
def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and k > len(answer):
            answer.append(i)
    return answer + [-1] * (k-len(answer))

# 배열 만들기 6
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer and arr[i] == answer[-1]:
            answer.pop()
        else:
            answer.append(arr[i])
    return answer or [-1]

# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    answer = []
    n = len(arr)
    cnt = 0
    while(n > 1):
        n /= 2
        cnt += 1
    if n > 0:
        arr += [0] * (2 ** cnt - len(arr))
    return arr

# 배열 비교하기
def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    
    if a != b:
        return 1 if a > b else -1
    else:
        if sum(arr1) == sum(arr2):
            return 0
        temp = max(sum(arr1), sum(arr2))
        return 1 if temp == sum(arr1) else -1

def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    answer = []
    start = 1 if len(arr) % 2 == 0 else 0
    for i in range(start, len(arr), 2):
        arr[i] += n
    return arr

# 뒤에서 5등까지
def solution(num_list):
    num_list.sort()
    del num_list[5:]
    return num_list

# 문자열 묶기
def solution(strArr):
    answer = {}
    for i in strArr:
        if answer.get(len(i)):
            answer[len(i)] += 1
        else:
            answer[len(i)] = 1
    return max(answer.values())

# 뒤에서 5등 위로
def solution(num_list):
    return sorted(num_list)[5:]

# 전국 대회 선발 고사
def solution(rank, attendance):
    answer = 0
    n = 2
    for i in range(1, len(rank)+1):
        k = rank.index(i)
        if attendance[k]:
            answer += k*(100**n)
            n -= 1
        if n == -1:
            break
    return answer

# 정수 부분
def solution(flo):
    return int(flo)

# 문자열 정수의 합
def solution(num_str):
    return eval('+'.join(list(num_str)))

# 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

# 0 떼기
def solution(n_str):
    return str(int(n_str))

# 두 수의 합
def solution(a, b):
    return str(int(a)+int(b))

# 문자열로 변환
def solution(n):
    return str(n)

# 부분 문자열인지 확인하기
def solution(my_string, target):
    return int(target in my_string)

# 배열의 원소 삭제하기
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]

# 부분 문자열
def solution(str1, str2):
    return 1 if str1 in str2 else 0

# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

# 정수 찾기
def solution(num_list, n):
    return 1 if n in num_list else 0

# 주사위 게임 1
def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:
        answer = a ** 2 + b ** 2
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a+b)
    else:
        answer = abs(a-b)
    return answer

# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    for i, j in enumerate(arr):
        if k % 2 == 0:
            arr[i] += k
        else:
            arr[i] *= k
    return arr

# 커피 심부름
def solution(order):
    answer = 0
    for i in order:
        if 'americano' in i or 'anything' in i: 
            answer += 4500
        else:
            answer += 5000
    return answer

# 특별한 이차원 배열 2
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# 정사각형으로 만들기
def solution(arr):
    h = len(arr)
    w = len(arr[0])

    if h > w:
        for i in range(h):
            arr[i] += [0] * (h-w)
    elif h < w:
        arr += [[0] * w] * (w-h)
    return arr

# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j <= k:
                answer += board[i][j]
    return answer