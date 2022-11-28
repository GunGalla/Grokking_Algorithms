"""Binary search function"""


def binary_search(items, item):
    low = 0
    high = len(items) - 1
    iterations = 0

    while low <= high:
        mid = int((low + high) / 2)
        guess = items[mid]
        if guess == item:
            iterations += 1
            print(iterations)
            return mid
        if guess > item:
            high = mid - 1
            iterations += 1
        else:
            low = mid + 1
            iterations += 1
    return None
