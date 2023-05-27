def number_of_pairs(gloves):
    l = gloves
    d = {}

    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    count = 0

    for i, j in d.items():
        if j > 1:
            count += j // 2

    return count


print(number_of_pairs(['red', 'green', 'red', 'blue', 'blue']))


# red green red blue blue