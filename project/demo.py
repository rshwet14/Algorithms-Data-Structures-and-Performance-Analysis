def quicksort(arr):
    """
    Input: Unsorted list of integers
    Returns sorted list of integers using quick_sort
    Note: This is not an in-place implementation
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

def merge_sorted(arr1,arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)
