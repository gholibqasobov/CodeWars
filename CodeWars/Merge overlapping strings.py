def merge_strings(first, second):
    for i in range(len(second), -1, -1): # check the second word by removing one char each time
        # print(second[:i])
        if first.endswith(second[:i]): # checking for longest common overlap
            # print(second[i:])
            return first + second[i:]


print(merge_strings('abc', 'abc'))