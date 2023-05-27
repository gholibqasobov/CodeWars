import re
def kebabize(st):
    result = ''
    for i in st:
        if i.isalpha():
            if i.isupper():
                result += '-' + i
            else:
                result += i
            if result[0] == '-':
                result = result[1:]
    return result.lower()

print(kebabize('camelsHave3Humps'))