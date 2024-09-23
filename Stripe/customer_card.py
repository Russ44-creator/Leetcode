'''
Stripe merchants sometimes bring payment data with them from another payment processor by sending a data 
file containing a list
of card details for us to import. You will be given a string with the contents of a CSV (comma-separated 
value) file that has
already been read, containing a list of card entries in the following format:
    customer_id,card_id,first_name,last_name,card_number,expiration
    cus_100,card_100,John,Doe,4242424242424242,1023
    ...
No data fields in this file will include commas or whitespace surrounding the field values. You can assume that the input has
already been read from a file and checked for correctness. The imported data will only include active cards, so expiration
dates are all in the 21st century.

Exercise:
Write a function that takes the string as input and returns a list of objects representing the parsed card data. The first and
last names (if present) should be combined into a single field, and the expiration date should be parsed into separate month
and year fields. You should include tests to verify the behavior of your function.

Example:
input = """customer_id,card_id,first_name,last_name,card_number,expiration
            cus_100,card_100,John,Doe,4242424242424242,1023
            cus_200,card_200,Jane,Doe,5555555555554444,921
            cus_300,card_300,,Roberts,6011111111111117,820"""
parse_card_data(input)

Returns:
[
    {
        "customer_id": "cus_100",
        "card_id": "card_100",
        "cardholder_name": "John Doe",
        "card_number": "4242424242424242",
        "exp_month": "10",
        "exp_year": "2023"
    },
    {
        "customer_id": "cus_200",
        "card_id": "card_200",
        "cardholder_name": "Jane Doe",
        "card_number": "5555555555554444",
        "exp_month": "9",
        "exp_year": "2021"
    },
    {
        "customer_id": "cus_300",
        "card_id": "card_300",
        "cardholder_name": "Roberts",
        "card_number": "6011111111111117",
        "exp_month": "8",
        "exp_year": "2020"
    }
]
'''