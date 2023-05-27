# n = int(input())
# s = []
# for i in range(3, n):
#     if i % 3 == 0:
#         if i not in s:
#             s.append(i)
#
#     if i % 5 == 0:
#         if i not in s:
#             s.append(i)
#
#
# sum = 0
#
# for i in s:
#     sum += i
#
# print(sum)


n = int(input())

def solution(n):
    sum = 0

    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(solution(n))