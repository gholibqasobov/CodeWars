def solution(s):
    def split(s):
        temp = ''
        l = []
        for i in range(len(s)):
            temp += s[i]
            if i % 2 == 1:
                l.append(temp)
                temp = ''
        return l

    if len(s) % 2 == 0:
        return split(s)
    else:
        s += '_'
        return split(s)


print(solution('abc'))