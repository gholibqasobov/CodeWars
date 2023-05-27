# def duplicate_encode(s):
#     d = {}
#     new_s = ''
#     s = s.lower()
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     for ch in s():
#         for i, j in d.items():
#             if ch == i:
#                 if j > 1:
#                     new_s += ')'
#                 else:
#                     new_s += '('
#     return new_s
#
#
# print(duplicate_encode('hello'))


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])