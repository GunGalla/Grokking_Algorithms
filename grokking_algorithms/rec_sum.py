'''Recursive sum function'''


def rec_sum(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + rec_sum(items[1:])


def biggest_i(items):
    biggest = items[0]
    for item in range(1, len(items)):
        if items[item] > biggest:
            biggest = items[item]
    return biggest


print(rec_sum([1, 2, 3, 1029, 4, 25]))
