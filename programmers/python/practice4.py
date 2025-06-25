# 배열 만들기 1
'''
range와 list comprehension을 사용하여
1부터 n까지의 숫자 중 k의 배수를 포함하는 리스트를 반환하는 함수
'''
def solution(n, k):
    return [i for i in range(k, n+1, k)]