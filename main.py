# 🔹 Problem 1: Reverse a String
#    Write a function that takes a string as input and returns the reversed string.
#    Example:
# 🔹 Input: "hello"
# 🔹 Output: "olleh"
# 💡 Hint: Use Python's slicing feature.


def reverse_string(s):
    return s[ : : -1]

print(reverse_string("hello"))




# 🔹 Problem 2: Count Vowels in a String
#    Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
#    Example:
# 🔹 Input: "Apple"
# 🔹 Output: 2
# 💡 Hint: Use a loop and check if each character is in a set of vowels.


def count_vowels(s):
    vowels = set("aeiou")
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("Apple"))




# 🔹 Problem 3: Sum of Digits
#    Write a function that takes a non-negative integer and returns the sum of its digits.
#    Example:
# 🔹 Input: 1234
# 🔹 Output: 10
# 💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))