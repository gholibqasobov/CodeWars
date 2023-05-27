def computer_to_phone(numbers):
    new_num = ''
    const = '0456'
    upper = '789'
    lower = '123'
    for i in numbers:
        if i in const:
            new_num += i
        elif i in upper:
            new_num += str(int(i) - 6)
        elif i in lower:
            new_num += str(int(i) + 6)

    return new_num

print(computer_to_phone('0789456123'))