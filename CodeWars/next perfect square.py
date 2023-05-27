from math import sqrt
def next_square(sq):
    n = int(sqrt(sq))
    if pow(n, 2) == sq:
        return pow(n+1, 2)
    else:
        return -1

print(next_square(1))

