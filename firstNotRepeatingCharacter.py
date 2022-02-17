def solution(s):
    chars = {}
    for i in s:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] = chars[i] + 1
    for ch in s:
        if chars[ch] == 1:
            return ch
    return "_"