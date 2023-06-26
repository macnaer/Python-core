# def sum(a, b):
#     return a + b


# result = sum(2, 8)

# print(result)


# def test(a, b):
#     print(f"Sum = {a} + {b} = {a + b}")


# test(5, 12)


def plus(*numbers):
    sum = 0
    for item in numbers:
        sum += item
    return sum


print(plus(2, 2, 1, 12))
