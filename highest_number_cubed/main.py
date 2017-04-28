"""This is the entry point of the program."""


def highest_number_cubed(limit):
    num = 0
    while num ** 3 < limit:
        num += 1
    answer = num - 1
    return answer