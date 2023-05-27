import re


def camel_case(s):
    return ''.join([i.capitalize() for i in s.split()])


print(camel_case('hello world it is me'))