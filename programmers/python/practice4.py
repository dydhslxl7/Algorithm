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
