def longest_palindrome(s):
    n = len(s)
    max_len = 1
    if s == s[::-1]:
        return len(s)
    else:
        # here we got to check each substring
        # first get length of each substring:
        for substring_len in range(n, 0, -1):
            for start_point in range(n-substring_len + 1):
                end_point = start_point + substring_len
                # print(start_point, end_point)
                temp = s[start_point:end_point]
                if temp == temp[::-1]:
                    if len(temp) > max_len:
                        max_len = len(temp)
    return max_len


print(longest_palindrome('aa'))
