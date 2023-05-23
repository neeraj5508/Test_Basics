import pytest
from function import *


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1


def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 1) == 0
    assert pytest.raises(ValueError, divide, 4, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(0, 0) == 1


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True


def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(0) == False































# import pytest
# from function import fibonacci

# def test_fibonacci():
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
#     assert fibonacci(4) == 3
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8
#     assert fibonacci(7) == 13

# def test_negative_input():
#     with pytest.raises(ValueError):
#         fibonacci(-1)

# def test_zero_input():
#     with pytest.raises(ValueError):
#         fibonacci(0)




# # import pytest
# from function import is_even

# def test_is_even_with_even_number():
#     assert is_even(4) == True

# def test_is_even_with_odd_number():
#     assert is_even(3) == False

# def test_is_even_with_float():
#     with pytest.raises(TypeError):
#         is_even(2.5)





# # import pytest

# # # test_math_utils.py
# # from function import factorial

# # def test_factorial_of_zero():
# #     assert factorial(0) == 1

# # def test_factorial_of_one():
# #     assert factorial(1) == 1

# # def test_factorial_of_positive_number():
# #     assert factorial(5) == 120
# #     assert factorial(10) == 3628800

# # def test_factorial_of_negative_number():
# #     with pytest.raises(ValueError):
# #         factorial(-5)

# # def test_factorial_of_non_integer():
# #     with pytest.raises(TypeError):
# #         factorial(2.5)
































# # def count_vowels(word):
# #     vowels = "aeiouAEIOU"
# #     count = 0
# #     for char in word:
# #         if char in vowels:
# #             count += 1
# #     return count

# # def test_hello():
# #     assert count_vowels("hello") == 2

# # def test_world():
# #     assert count_vowels("world") == 1

# # def test_all_vowels():
# #     assert count_vowels("aeiou") == 5
