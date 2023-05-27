def narcissistic(value):
    n = 0
    s = 0
    temp = temp2 = value
    while temp > 0:
        temp //= 10
        n += 1
    while temp2 > 0:
        r = temp2 % 10

        s += pow(r, n)
        temp2 //= 10

    if s == value:
        return True

    return False



print(narcissistic(1652))