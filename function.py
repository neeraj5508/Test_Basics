def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def power(x, y):
    return x ** y


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0



























# def fibonacci(n):
#     if n <= 0:
#         raise ValueError("n must be a positive integer")
#     if n == 1 or n == 2:
#         return 1
#     else:
#         fib = [1, 1]
#         for i in range(2, n):
#             fib.append(fib[i-1] + fib[i-2])
#         return fib[-1]


# def is_even(num):
#     """
#     Returns True if the given number is even, False otherwise.
#     """
#     if not isinstance(num, int):
#         raise TypeError("Expected an integer.")
#     return num % 2 == 0



# # def factorial(n):
# #     if n < 0:
# #         raise ValueError("n must be a non-negative integer")
# #     elif n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
