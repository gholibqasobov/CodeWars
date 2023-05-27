def create_phone_number(n):
    num = ['(']
    for i in range(3):
        num.append(str(n[i]))
    num.extend([')', ' '])
    for i in range(3, 6):
        num.append(str(n[i]))
    num.append('-')
    for i in range(6, 10):
        num.append(str(n[i]))
    num = "".join(num)
    return num

# print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))

print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))



# def create_phone_number(n):
#     num = ['(']
#     for i in range(n[2]):
#         num.append(str(n[i]))
#     num.extend([')', ' '])
#     for i in range(n[2], n[5]):
#         num.append(str(n[i]))
#     num.append('-')
#     for i in range(n[5], len(n)):
#         num.append(str(n[i]))
#     num = "".join(num)
#     return num