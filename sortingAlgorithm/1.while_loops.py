# truth_condition = True
#
# while truth_condition:
#     print("hello")
#     break;
# i = 1
# while i<=10:
#     print(i)
#     i+=1

'''
question: 1. create a randint i.e random interger with certain value example
1,1000
2. find the given number at certain index.
'''
'''
from random import randint

l1 = [randint(1,100) for num in range(1,1000)]
num_to_search = 25
# index = 0
# while index < len(l1):
#     if l1[index] == num_to_search:
#         print(f"{num_to_search} is found on index {index}")
#         break
#     index+=1

# We can also do it using for loop
#
# for num in l1:
#     index+=1
#     if num == num_to_search:
#         print(f"{num_to_search} is found on index {index}")
# we can also do this using enumerate function so we don't need to declare index variable for this.
'''
'''
for index,num in enumerate(l1):
    if num == num_to_search:
        print(f"{num_to_search} is found on index {index}")
'''

'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
'''
l1 = [1,2,3,4,5]
l2 = ["shwet", "roy", "mannu", "raj", "rahul", "sk"]

my_tuple = list(zip(l1, l2))
print(my_tuple)
