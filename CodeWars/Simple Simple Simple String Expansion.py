# def string_expansion(s):
#     num = []
#     char = []
#     new_s = ''
#     if s.isdigit():
#         return ''
#     elif s.isalpha():
#         return s
#     elif len(s) == 0:
#         return ''
#     else:
#         if s[0].isalpha():
#             char.append(s[0])
#             num.append(1)
#             for i in range(1, len(s)):
#                 if s[i].isalpha() and s[i-1].isdigit():
#                     char.append(s[i])
#                     num.append(int(s[i-1]))
#                 elif s[i].isalpha() and s[i-1].isalpha():
#                     char.append(s[i])
#                     num.append(num[-1])
#         elif s[0].isdigit():
#             for i in range(1, len(s)):
#                 if s[i].isalpha() and s[i-1].isdigit():
#                     char.append(s[i])
#                     num.append(int(s[i-1]))
#                 elif s[i].isalpha() and s[i-1].isalpha():
#                     char.append(s[i])
#                     num.append(num[-1])
#
#     for i in range(len(char)):
#         new_s += char[i] * num[i]
#
#     return new_s

s = input()
new_s,num = '', 1

for i in s:
    if i.isdigit():
        num = int(i)
    else:
        new_s += i * num

print(new_s)