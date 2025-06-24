# 주사위 게임 3
"""
* list.count() /  max(origin, key=origin.count) 의 활용
"""
def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    arr = list(set(origin))
    n = len(arr)

    if n == 1:
        answer = 1111 * a
    elif n == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))  
    elif n == 3:
        p = max(origin, key=origin.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    elif n == 4:
        answer = min(origin)
    return answer

"""
* list.count() / list.index()의 활용
"""
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]

    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)