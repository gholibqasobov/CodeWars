numbers = {}

for i in range(10):
    numbers[i] = False


def compute_depth(n):
    if n == 0:
        return 9
    else:
        count = 1
        while not all(numbers.values()):
            num = n * count
            while num > 0:
                digit = num % 10
                numbers[digit] = True
                num //= 10

            print(numbers)
            count += 1

        return count - 1


print(compute_depth(3))