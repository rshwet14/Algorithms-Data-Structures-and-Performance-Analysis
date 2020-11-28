def bisection_search(num, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start + stop)//2
        if num == arr[mid]:
            return f"{num} is found at index {mid}"

        elif num > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return f"{num} is not found in list"


# num = 89
# l = [1,2,3,4,5,6,7,8,10]
def create_list(max_value):
    arr = []
    for num in range(1,max_value+1):
        arr.append(num)
    return arr
l = create_list(10)
for num in range(1,51):
    print(bisection_search(num,l))
