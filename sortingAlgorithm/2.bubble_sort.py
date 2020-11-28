from random import randint
def Bubble_sort(arr):
    flag = True
    comparisions = 0
    while flag:
        comparisions += 1
        flag = False
        for num in range(0, len(arr)-1):
            comparisions += 1
            if arr[num] > arr[num+1]:
                flag = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    print(arr)
    print(comparisions)
# arr = [5,10,9,99,66,2,1,3,4]
#arr = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

arr = [randint(1,100)for i in range(1,10000)]
Bubble_sort(arr)

#
# def Bubble_sort(arr):
#
#     # length = len(arr) - 1
#     index = 0
#     iteration = 0
#     while index < len(arr):
#         print(f"swapped happend at iteration{iteration} : {arr}")
#         for num in range(0,len(arr)-1):
#             if arr[num] > arr[num+1]:
#                 arr[num], arr[num+1] = arr[num+1], arr[num]
#         # print(f"swapped happend at iteration{iteration} : {arr}")
#         iteration += 1
#         index +=1
#
# arr = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
# Bubble_sort(arr)
