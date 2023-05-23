import unittest
from function import *


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, -3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(6, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 0), 1)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(2))


if __name__ == '__main__':
    unittest.main()































# import unittest
# from function import fibonacci

# class TestFibonacci(unittest.TestCase):
    
#     def test_fibonacci(self):
#         self.assertEqual(fibonacci(1), 1)
#         self.assertEqual(fibonacci(2), 1)
#         self.assertEqual(fibonacci(3), 2)
#         self.assertEqual(fibonacci(4), 3)
#         self.assertEqual(fibonacci(5), 5)
#         self.assertEqual(fibonacci(6), 8)
#         self.assertEqual(fibonacci(7), 13)
    
#     def test_negative_input(self):
#         with self.assertRaises(ValueError):
#             fibonacci(-1)
    
#     def test_zero_input(self):
#         with self.assertRaises(ValueError):
#             fibonacci(0)

# if __name__ == '__main__':
#     unittest.main()





# # import unittest
# from function import is_even

# class TestIsEven(unittest.TestCase):

#     def test_is_even_with_even_number(self):
#         self.assertTrue(is_even(4))

#     def test_is_even_with_odd_number(self):
#         self.assertFalse(is_even(3))

#     def test_is_even_with_float(self):
#         with self.assertRaises(TypeError):
#             is_even(2.5)

# if __name__ == '__main__':
#     unittest.main()









# # import unittest
# # from function import factorial

# # class TestFactorial(unittest.TestCase):
# #     def test_factorial_of_positive_number(self):
# #         self.assertEqual(factorial(5), 120)
    
# #     def test_factorial_of_zero(self):
# #         self.assertEqual(factorial(0), 1)
    
# #     def test_factorial_of_negative_number(self):
# #         with self.assertRaises(ValueError):
# #             factorial(-1)
    
# #     def test_factorial_of_non_integer(self):
# #         with self.assertRaises(TypeError):
# #             factorial(2.5)

# # if __name__ == '__main__':
# #     unittest.main()






























# # import unittest
# # class TestCountVowels(unittest.TestCase):

# #     @staticmethod
# #     def count_vowels(word):
# #         """
# #         Returns the number of vowels in a given word.
# #         """
# #         vowels = "aeiouAEIOU"
# #         count = 0
# #         for char in word:
# #             if char in vowels:
# #                 count += 1
# #         return count
    
# #     def test_hello(self):
# #         self.assertEqual(self.count_vowels("hello"), 2)
        
# #     def test_world(self):
# #         self.assertEqual(self.count_vowels("world"), 1)
        
# #     def test_all_vowels(self):
# #         self.assertEqual(self.count_vowels("aeiou"), 5)


# # if __name__=='__main__':
# #     unittest.main()
