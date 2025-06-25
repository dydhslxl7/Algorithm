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