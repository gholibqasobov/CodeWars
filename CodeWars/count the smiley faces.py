# def countSmilesy(lis):
#     count = 0
#     l = [':)', ';)', ':D', ';D', ':-)', ';-)', ':-D', ';-D', ':~)', ';~)', ':~D', ';~D']
#     for i in lis:
#         if i in l:
#             count += 1
#
#     return count
#
# print(countSmilesy([';]', ':[', ';*', ':$', ';-D']))


def count_smileys(arr):
    count = 0
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']

    for i in arr:
        if len(i) == 3:
            if i[0] in eyes and i[1] in nose and i[2] in mouth:
                count += 1

        if len(i) == 2:
            if i[0] in eyes and i[1] in mouth:
                count += 1

    return count


print(count_smileys([';]', ':[', ';*', ':$', ';-D']))