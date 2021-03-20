"""Sorting algorithms examples."""


def selection_sort(source):

    def pop_smallest():
        smallest = source[0]
        smallest_i = 0
        for i in range(1, len(source)):
            if source[i] < smallest:
                smallest = source[i]
                smallest_i = i
        return source.pop(smallest_i)

    target = []
    while source:
        target.append(pop_smallest())

    return target
