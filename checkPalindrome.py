def solution(inputString):
    revStr = inputString[::-1]
    for x in range(len(revStr)):
        if revStr[x] != inputString[x]:
            return False
    return True