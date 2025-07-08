# 배열 만들기 1
'''
range와 list comprehension을 사용하여
1부터 n까지의 숫자 중 k의 배수를 포함하는 리스트를 반환하는 함수
'''
def solution(n, k):
    return [i for i in range(k, n+1, k)]

# 글자 지우기 -> del 
def solution(my_string, indices):
    m = list(my_string)  # 문자열을 리스트로 변환
    m = [m[i] for i in range(len(m)) if i not in indices]  # 인덱스에 해당하는 문자 제거
    return ''.join(m)

def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i] 
    return ''.join(my_string)

# 가까운 1 찾기
'''
1. if else 문 먼저 작성 후 for 문을 사용하여 리스트 생성
2. index 메서드에 시작 인덱스를 지정하는 방법
'''
def solution(arr, idx):
    arr = [0 if arr[i] == 1 and i < idx else arr[i] for i in range(len(arr))]
    return arr.index(1) if 1 in arr else -1

def solution(arr, idx):
    return arr.index(1, idx)

## unpacking
# 리스트 자르기 -> 풀이 2
def solution(n, slicer, num_list):
    a, b, c = slicer
    return [num_list[:b+1], num_list[a:], num_list[a:b+1], num_list[a:b+1:c]][n-1]

# 배열 만들기 3
def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return arr[a1:b1+1]+arr[a2:b2+1]

# 2의 영역 -> 역순으로 index를 찾는 방법
def solution(arr):
    tmp = [i for i in range(len(arr)) if arr[i] == 2]
    return arr[min(tmp):max(tmp)+1] if len(tmp) > 0 else -1

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2):len(arr)-arr[::-1].index(2)+1]

# 조건에 맞게 수열 변환하기 2
'''
🚨 잠깐! '얕은 복사'와 '깊은 복사'는 알아둬야 해!
리스트를 복제해서 완전히 독립적인 새 리스트를 만드는 방법들([:], list(), .copy())은 모두 '얕은 복사(Shallow Copy)'야.
이게 무슨 말이냐면, 리스트 안에 또 다른 리스트(혹은 딕셔너리 같은 변경 가능한 객체)가 들어있을 때, 그 '안쪽 리스트'는 복제되지 않고 여전히 원본과 같은 객체를 가리키게 돼.
만약 리스트 안에 또 다른 리스트가 있는데, 그것까지 완전히 독립적으로 복제하고 싶다면 '깊은 복사(Deep Copy)' 를 사용해야 해. 이건 copy 모듈의 deepcopy() 함수를 써야 해!
'''
def solution(arr):
    answer = -1
    temp = []
    
    while temp != arr:
        temp = arr.copy()

        for k, v in enumerate(arr):
            if v >= 50 and v % 2 == 0:
                arr[k] = v // 2
            elif v < 50 and v % 2 != 0:
                arr[k] = v * 2 + 1
        answer += 1

    return answer

# 길이에 따른 연산
'''
1. math.prod(): 일반적인 반복 가능한(iterable) 객체의 곱셈
math 모듈에 있는 prod 함수는 리스트, 튜플 등 일반적인 반복 가능한 객체(iterable) 안에 있는 숫자들을 전부 곱해줘.

사용법: math.prod(iterable, *, start=1)
iterable: 곱셈을 할 숫자 요소들이 들어있는 리스트, 튜플 등.
start: 곱셈을 시작할 초기값. 기본값은 1이야. (만약 0으로 설정하면 결과는 항상 0이 되겠지?)
'''
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)

# 원하는 문자열 찾기 -> find와 in을 활용한 문자열 검색
def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    
    if myString.find(pat) > -1:
        return 1
    else:
        return 0

def solution(myString, pat):
    return int(pat.lower() in myString.lower())

# 배열에서 문자열 대소문자 변환하기 -> replace
def solution(myString):
    return myString.lower().replace('a', 'A')

# 공백으로 구분하기1 -> split()은 리스트로 반환
def solution(my_string):
    return my_string.split(' ')

# 문자열 바꿔서 찾기
def solution(myString, pat):
    # 'A'를 'B'로, 'B'를 'A'로 바꾸는 테이블 생성
    # 첫 번째 인자: 바꿀 문자들 (원본)
    # 두 번째 인자: 바뀔 문자들 (대상)
    translation_table = str.maketrans("AB", "BA") 

    # 테이블을 적용해서 문자열 치환
    new_text = myString.translate(translation_table)

    return 1 if pat in new_text else 0

# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    answer = []
    for k, v in enumerate(arr):
        if flag[k]:
            for i in range(v * 2):
                answer.append(v)
        else:
            for i in range(v):
                answer.pop()
    return answer

'''
zip()의 특징 및 활용
튜플 형태로 묶어줌: zip()은 각 요소들을 튜플 형태로 묶어서 반환해.

가장 짧은 이터러블에 맞춰 작동: 만약 입력받은 이터러블들의 길이가 다르면, zip()은 가장 짧은 이터러블의 길이에 맞춰서 요소를 묶어. 나머지 긴 이터러블의 남은 요소들은 무시돼.

names = ["철수", "영희", "민수"]
scores = [90, 85] # 영희의 점수가 빠졌네!

zipped_students = list(zip(names, scores))
print(f"길이가 다른 리스트 묶기: {zipped_students}")
# 결과: 길이가 다른 리스트 묶기: [('철수', 90), ('영희', 85)]
# 민수는 scores에 짝이 없어서 묶이지 않아.
'''
'''
파이썬에서 리스트 * 숫자의 의미
파이썬에서 리스트에 정수를 곱하면, 그 리스트의 내용이 곱한 횟수만큼 반복되어 새로운 리스트를 만들어.
'''
def solution(arr, flag):
    arr1 = []
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1

# 날짜 비교하기
'''
튜플뿐만 아니라 리스트도 부등호(>, <, >=, <=) 비교가 가능합니다.
파이썬에서는 리스트와 튜플 모두 내부 요소를 왼쪽부터 순서대로 차례차례 비교합니다.
'''
def solution(date1, date2):
    return int(date1 < date2)