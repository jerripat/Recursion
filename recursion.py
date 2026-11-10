# Recursion

def factorial(num):
    """Return the factorial of a number using recursion."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(4))

def countdown(n):
    """Print numbers from n down to 1 using recursion."""
    if n <= 0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
def count_up(n):
    """Print numbers from 1 up to n using recursion."""
    if n <= 0:
        print("Count finished!")
    else:
        count_up(n - 1)
        print(n)
count_up(20)