# import demo
import time
from demo import quicksort
from demo import mergesort
import random
def create_random_list(size, max_val):
    ran_list = list(random.randint(1,max_val) for num in range(size))
    return ran_list

def analyze_func(fun_name, arr):
    start = time.time()
    fun_name(arr)
    stop = time.time()
    second = stop - start
    print(f"{fun_name.__name__.capitalize()}\t->Elapsed time: {second} seconds")


size = int(input("What size list do you want to create?"))
max_val = int(input("What is the max value of the range?"))
l = create_random_list(size, max_val)
analyze_func(quicksort, l)
analyze_func(mergesort, l)



# print(l)
# print(demo.quick_sort(l)) we can made modification in import
# start = time.time()
# quick_sort(l)
# stop = time.time()
# print("Quicksort --> Elapsed time -->", stop - start)
#
# start = time.time()
# merge_sorting(l)
# stop = time.time()
# print("Mergesort --> Elapsed time -->", stop - start)
