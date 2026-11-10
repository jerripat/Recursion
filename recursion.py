# Recursion

def factorial(num):
    """Return the factorial of a number using recursion."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))