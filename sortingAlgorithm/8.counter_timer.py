# Iterative solutions

import time
#
# def iter_countdown_timer(n):
#     while n > 0:
#         print(n)
#         time.sleep(1)
#         n -= 1
#     print(n)
# timer = int(input("set timer:"))
# iter_countdown_timer(timer)

# Recursive solution

def recur_countdown_timer(n):
    if n == 0:
        print(n)
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_timer(n-1)

z = 10
recur_countdown_timer(z)
