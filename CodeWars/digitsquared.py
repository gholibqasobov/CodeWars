def square_digits(num):
    num = str(num)
    l = []
    for i in num:
        r = (pow(int(i), 2))
        l.append(str(r))

    l = ''.join(l)
    return int(l)


print(square_digits(9119))
