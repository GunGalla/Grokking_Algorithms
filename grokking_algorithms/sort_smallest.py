"""Find the smallest function"""


def smallest_i(items):
    smallest = items[0]
    smallest_index = 0
    for item in range(1, len(items)):
        if items[item] < smallest:
            smallest = items[item]
            smallest_index = item
    return smallest_index


def sorting(items):
    new_items = []
    for item in range(len(items)):
        smallest = smallest_i(items)
        new_items.append(items.pop(smallest))
    return new_items


