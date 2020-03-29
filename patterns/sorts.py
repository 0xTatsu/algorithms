#  Complexity: O(n ^ 2)


def QuickSort(array=[12, 4, 5, 6, 7, 3, 1, 15]):
    if len(array) <= 1:
        return array

    less = []
    equal = []
    greater = []

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)
    return QuickSort(less)+equal+QuickSort(greater)
