def longest_repetition(chars):
    count = 0
    ch = chars[0]

    for i in range(len(chars)):
        currnt_count = 1
        for j in range(i + 1, len(chars)):
            if chars[i] != chars[j]:
                break
            currnt_count += 1

        if currnt_count > count:
            count = currnt_count
            ch = chars[i]

    return ch, count

print(longest_repetition('abbaa'))