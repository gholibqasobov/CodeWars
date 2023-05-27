import re


def validate_code(code):
    code = str(code)
    return bool(re.match('^[1-3]', code))


print(validate_code(123))


# def validate_code(code):
#     return str(code)[0] in '123'