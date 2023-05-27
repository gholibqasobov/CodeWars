def mappping(l):
    to_upper = {}

    for i in l:
        to_upper[i] = i.capitalize()

    return to_upper

print(mappping(["a", "v", "y", "z"]))