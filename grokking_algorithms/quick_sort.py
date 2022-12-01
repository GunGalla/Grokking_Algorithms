'''Quick sorting algorithm'''


def quick_sort(items):
    if len(items) < 2:
        return items
    else:
        base = items[0]
        under_base = [x for x in items[1:] if x < base]
        above_base = [x for x in items[1:] if x > base]
        return quick_sort(under_base) + [base] + quick_sort(above_base)


print(quick_sort([4, 23, 35, 21, 65, 3]))
