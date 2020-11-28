def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)

print(f"Factorial of 25 : {factorial_recur(0)}")
