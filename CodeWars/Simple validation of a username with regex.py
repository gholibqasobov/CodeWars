import re


# def validate_usr(username):
#     if 4 <= len(username) <= 16:
#         result = re.search(r'^[a-z0-9_]*$', username)
#         if result:
#             return True
#     return False
#
# print(validate_usr('asd43_34'))

def validate_usr(username):
    return bool(re.search('^[a-z0-9_]{4,16}$', username))


print(validate_usr('Hass'))