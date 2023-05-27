import re
from re import sub
# # def filter_words(phrase):
# #     return sub("(bad|mean|ugly|horrible|hideous)","awesome",phrase)
# def filter_words(phrase):
#     lis = "bad mean ugly horrible hideous".split()
#     for i in lis:
#         if i in phrase.lower():
#             phrase = sub(i, 'awesome', phrase.lower())
#     phrase = phrase.capitalize().split()
#     for i in range(len(phrase)):
#         if phrase[i] == 'soo':
#             phrase[i] = 'Soo'
#     return " ".join(phrase)

# print(filter_words("You're Soo Bad and Bad!"))


def filter_words(phrase):
    return sub("(bad|mean|ugly|horrible|hideous)", 'awesome', phrase, flags=re.I)

print(filter_words("You're Soo Bad and Bad!"))
