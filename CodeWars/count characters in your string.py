def count(string):
    cnt = {}
    for i in string:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    return cnt



# def count(string):
#     return {i: string.count(i) for i in string}
