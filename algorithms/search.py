"""Search algorithms examples"""


def binary_search(source, target):
    """Binary Search."""

    head = 0
    tail = len(source) - 1

    while head <= tail:
        mid = (head + tail) // 2
        print(f"check {mid} element")
        value = source[mid]
        if value > target:
            tail = mid - 1
            print(f"value is greater then target, search in head: [{head}:{tail}]")
        elif value < target:
            head = mid + 1
            print(f"value is lower then target, search in tail: [{head}:{tail}]")
        else:
            print("target found")
            return mid

    print("target not found")
    return -1
