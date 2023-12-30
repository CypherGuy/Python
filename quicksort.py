def quicksort(array, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        pivotIndex = partition(array, leftIndex, rightIndex)
        quicksort(array, leftIndex, pivotIndex - 1)
        quicksort(array, pivotIndex + 1, rightIndex)

def partition(array, leftIndex, rightIndex):
    pivot = array[rightIndex]
    i = leftIndex - 1
    for j in range(leftIndex, rightIndex):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[rightIndex] = array[rightIndex], array[i+1]
    return i + 1

print(quicksort([3,6,1,7,2,5,4], 3,4))