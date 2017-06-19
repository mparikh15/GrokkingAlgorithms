ToSort = [2, 52, 3, 76, 643, 43, 12, 1]


def quicksort(array):
    if len(array) < 2 :
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort(ToSort)