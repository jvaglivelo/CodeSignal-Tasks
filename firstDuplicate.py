def solution(a):
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)
    return -1
