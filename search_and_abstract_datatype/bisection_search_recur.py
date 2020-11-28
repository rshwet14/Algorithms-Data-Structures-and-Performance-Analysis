def binary_recursive_search(num, arr, start, stop):
    if start > stop:
        return f"{num} not found."
    else:
        mid = (start + stop)//2
        if num == arr[mid]:
            return f"{num} is found at index {mid}"
        elif num > arr[mid]:
            return binary_recursive_search(num, arr, mid+1, stop)
        else:
            return binary_recursive_search(num, arr, start, mid-1)



l = [1,2,3,4,5,6,7,8,9,10]
print(binary_recursive_search(1,l,0,len(l)-1))
