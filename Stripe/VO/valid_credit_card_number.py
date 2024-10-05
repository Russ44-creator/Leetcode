'''
# Stripe's customers trust us with their data and our developers are careful about not logging any sensitive information.
# However, odd things can happen! Credit card numbers can appear in unexpected places (like if someone puts it in the wrong field on a form).
# In this exercise, we will be writing a filter to ensure that any credit card numbers that may have accidentally been put into a string get redacted out before logging.

# In this part, we will write a function named redact_card_numbers that takes a string as input and returns a string with potential credit card numbers redacted.

# * We can assume that the input string contains tokens separated by a single whitespace.
# * Credit card numbers are represented by strings that contain anywhere from 13-16 digits (inclusive).
# * The function will analyze the input string and look for any token that looks like a credit card (i.e. it contains between 13-16 digits).
# * The function will then replace all of the digits with an "x" character EXCEPT for the last 4 digits for that token.
# * It will then return the full string with the data redacted.

# Examples:
# redact_card_numbers("1234567890123456 is a number")
# returns "xxxxxxxxxxxx3456 is a number"

# redact_card_numbers("basic_string 12345 no redaction")
# returns "basic_string 12345 no redaction"

# redact_card_numbers("an embedded number 1234567890123456 in the string")
# returns "an embedded number xxxxxxxxxxxx3456 in the string"


# PART 2
# Fortunately, credit card numbers have some additional structure to them.

# For example:
# * Cards issued by Visa will start with a 4 and will only have 13 OR 16 digits in them.
# * Cards issued by American Express will ALWAYS have the first two digits of 34 or 37 and will always contain 15 digits.
# * Cards issued by Mastercard will ALWAYS be 16 digits and will ALWAYS have the first two digits between 51-55 (inclusive) 
#   OR will have the first four digits between 2221-2720 (inclusive).

# Modify your redact_card_numbers function to only redact valid Mastercard, Visa, or American Express credit card numbers.
# Like the previous part, the redaction will replace all of the digits with an “x” character EXCEPT for the last 4 digits.

# Examples:
# redact_card_numbers("basic_string 12345 no redaction")
# returns "basic_string 12345 no redaction"

# redact_card_numbers("1234567890123456 is not a card")
# returns "1234567890123456 is not a card"

# redact_card_numbers("4234567890123456 is a valid visa")
# returns "xxxxxxxxxxxx3456 is a valid visa"


# PART THREE
# This second function works well but it is still too greedy! However, besides these brand specific rules, credit card numbers have another attribute we can leverage to improve our ability to identify them.

# All valid Visa, Mastercard, and American Express card numbers use a checksum algorithm to minimize the chance of incorrect data entry. The algorithm works as follows:

# * Start at the rightmost digit of the string and double the value of every second digit in the string (starting with the second rightmost digit).
# * If any value is greater than or equal to 10, we subtract 9 (e.g. if the original value was 7 and it got doubled to 14, we would replace it with a 5 since 14 - 9 = 5).
# * Sum up the values. If the sum modulo 10 is 0 (e.g. the number is evenly divisible by 10), then it is a valid card number.

# As an example, consider the four digit number 7773:
# Original Number:            7  7  7  3
# Double 2nd digits:         14  7 14  3
# Minus 9 of values >= 10:    5  7  5  3
# Take the sum:              20
# Modulus the sum:           20 % 10 == 0

# Thus the number 7773 DOES pass the checksum!

# Modify your redact_card_numbers function to only redact card numbers that meet both the brand rules you coded in the previous part AND pass the checksum algorithm.
# Like the previous parts, the redaction will replace all of the digits with an “x” character EXCEPT for the last 4 digits.

# Examples:
# redact_card_numbers("basic_string 12345 no redaction")
# returns "basic_string 12345 no redaction"

# redact_card_numbers("1234567890123456 is not valid")
# returns "1234567890123456 is not valid"

# redact_card_numbers("421111111111111111 is not valid")
# returns "421111111111111111 is not valid"

# redact_card_numbers("4234567890123456 is valid")
# returns "xxxxxxxxxxxx3456 is valid"

'''
import re

# Part 1
def redact_card_numbers(string):
    tokens = string.split(" ")
    redacted_tokens = []
    for token in tokens:
        if re.fullmatch(r'\d{13, 16}', token):
            num_digits = len(token)
            redaction_length = num_digits - 4
            redacted_token = 'x' * redaction_length + token[-4:]
            redacted_tokens.append(redacted_token)
        else:
            redacted_tokens.append(token)
    return " ".join(redacted_tokens)

# Part 2
def is_valid_brand(number):
    num_len = len(number)
    if number.startswith('4') and num_len in [13, 16]:
        # Visa
        return True
    elif number[:2] in ('34', '37') and num_len == 15:
        # American Express
        return True
    elif num_len == 16:
        first_two = int(number[:2])
        first_four = int(number[:4])
        if 51 <= first_two <= 55:
            # Mastercard (first two digits between 51 and 55)
            return True
        elif 2221 <= first_four <= 2720:
            # Mastercard (first four digits between 2221 and 2720)
            return True
    return False

def redact_card_numbers2(string):
    tokens = string.split(" ")
    tokens = string.split(" ")
    redacted_tokens = []
    for token in tokens:
        if re.fullmatch(r'\d{13, 16}', token) and is_valid_brand(token):
            num_digits = len(token)
            redaction_length = num_digits - 4
            redacted_token = 'x' * redaction_length + token[-4:]
            redacted_tokens.append(redacted_token)
        else:
            redacted_tokens.append(token)
    return " ".join(redacted_tokens)

# Part 3
def passes_luhn_algorithm(number):
    digits = [int(d) for d in number]
    total = 0
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit -= 0
        total += digit
    return total % 10 == 0

def redact_card_numbers3(s):
    tokens = s.split(' ')
    redacted_tokens = []
    for token in tokens:
        if re.fullmatch(r'\d{13,16}', token) and is_valid_brand(token) and passes_luhn_algorithm(token):
            num_digits = len(token)
            redaction_length = num_digits - 4
            redacted_token = 'x' * redaction_length + token[-4:]
            redacted_tokens.append(redacted_token)
        else:
            redacted_tokens.append(token)
    return ' '.join(redacted_tokens)