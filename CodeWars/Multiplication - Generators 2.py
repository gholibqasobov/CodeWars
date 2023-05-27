def generator(a):
    b = 1
    while a:
        yield str(a) + ' x ' + str(b) + ' = ' + str(a * b)
        b += 1






