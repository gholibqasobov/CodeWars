import re
# def to_camel_case(text):
#     result = re.split('[-_]', text)
#     for i in range(len(result)):
#         if i == 0:
#             continue
#         else:
#             result[i] = result[i].capitalize()
#
#     return ''.join(result)

def to_camel_case(text):
    result = re.split('[-_]', text)
    return result[0] + ''.join(item.capitalize() for item in result)


print(to_camel_case('the-stealth-warrior'))