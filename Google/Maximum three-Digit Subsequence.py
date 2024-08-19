'''
There is an array, named digits, consisting of N digits.
Choose at most three digits (not necessarily adjacent) and 
merge them into a new integer without changing the order of the digits. 
What is the biggest number that can be obtained this way?
Write a function:
def solution(digits)
that, given an array of N digits, returns the biggest number that can be built.
Examples:
1. Given digits = [7, 2, 3, 3, 4, 9], the function should return 749.
2. Given digits = [0, 0, 5, 7], the function should return 57.
Assume that:
• N is an integer within the range [3..50];
• each element of array, named digits', is an integer within the range [0..9].
In your solution, focus on correctness. The performance of your solution will 
not be the focus of the assessment.
'''

def solution(digits):
    n = len(digits)
    # get first n - 2 digits
    first_digit = max(digits[:n - 2])
    first_index = digits.index(first_digit)
    second_digit = max(digits[first_index + 1: -1])
    second_index = digits[first_index + 1: -1].index(second_digit) + first_index + 1
    third_digit = max(digits[second_index + 1:])
    return first_digit * 100 + second_digit * 10 + third_digit

digits = [9, 5, 1, 1, 0, 3]

print(solution(digits))


