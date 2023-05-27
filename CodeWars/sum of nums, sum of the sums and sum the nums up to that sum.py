def sum_of_sums(n):

    def partial_sum(n):
        s = 0
        for i in range(1, n + 1):
            s += i
        return s

    total = 0
    for i in range(1, n + 1):
        total += partial_sum(i)

    def total_sum(totl):
        t = 0
        for i in range(1, totl + 1):
            t += i

        return t

    return total_sum(total)