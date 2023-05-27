def generate_hashtag(s):
    if len(s) != 0:
        new_s = "".join(word.capitalize() for word in s.split())
        if len(new_s) < 140:
            return '#' + new_s
    return False


print(generate_hashtag('hello world'))
