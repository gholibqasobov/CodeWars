import re


# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         return bool(re.search('^[0-9]{4}$|^[0-9]{6}$', pin))
#     return False
#
#
# print(validate_pin('1234'))

def validate_pin(pin):
    return bool(re.fullmatch('\d{4}|\d{6}', pin))

print(validate_pin('123466'))