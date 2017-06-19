import random

ToSort = [2, 52, 3, 76, 643, 43, 12, 1]


def quicksort(array):
    if len(array) < 2:
        return array

    else:
        holder = len(array)

        pivot = array[random.randint(0, holder - 1)]

        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort(ToSort)