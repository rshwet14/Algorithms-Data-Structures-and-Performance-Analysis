def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)






l = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
selection_sort(l)
