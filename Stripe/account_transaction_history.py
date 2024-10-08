'''
一个csv格式的string,csv里面有一些account receivable transaction history。
 然后要求你把里面的相同向合并。 然后格式也要稍微转换一下。
比如说:
merchant A, 2024-01-01, Visa, 100
merchant A, 2024-01-01, Visa, 200
Output:
merchant A, 2024-01-01, Visa, 300

Part 2, Part 3 就是可以添加一个contract, 一个contract可以由多个 account receivable 组成。
merchant A, 2024-01-01, Visa, 100
merchant A, 2024-01-01, Visa, 200
contract1, merchant A, 2024-01-01, Visa, 200

Output:
merchant A, 2024-01-01, Visa, 100
contract, 2024-01-01, Visa, 200
具体格式不太记得了。 题目不是很难，但是要读的东西特别多。
'''

'''
Part 1 prompt: Stripe in Brazil is obliged to register customer's transactions for each merchant with the central bank as an aggregated unit per day.
These are called receivables. A receivable is identified by 3 identifiers:
* merchant_id (String): The id of the merchant on Stripe side.
* card_type (String): The type of the card used for the transaction (e.g. Visa)
* payout_date (String): String date of the funds available to the merchant by Stripe.
A payment transaction in Stripe API can be represented as the following object:
```
Transaction {
    string customer_id
    string merchant_id
    string payout_date
    string card_type
    int amount
}
```
Implement register_receivables function that takes a string in CSV format
where each line represents a transaction and returns the registered aggregated receivables using the rules above.
Print the returned receivables to console using the format below.
Feel free to parse the CSV using a standard or a 3rd party library or implement it yourself.
You can assume the following about the input:
* The first line of the input is a header. The header is always the same so it can be ignored or hardcoded
* You can assume that the input has
already been read from a file and checked for correctness
* No data fields in this file will include commas or whitespace surrounding the field values.
You can also assume the following about the output:
* The first line of the output is the header. The header is always the same so it can be hardcoded
* Order of the output does not matter
Example input 1:
```
customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-30,Visa,150
cust2,merchantA,2021-12-30,Visa,200
cust3,merchantB,2021-12-31,MasterCard,300
cust4,merchantA,2021-12-30,Visa,50
```
Output 1:
```
merchant_id,card_type,payout_date,amount
merchantA,Visa,2021-12-30,400
merchantB,MasterCard,2021-12-31,300
```
Example input 2:
```
customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-29,MasterCard,50
cust2,merchantA,2021-12-29,Visa,150
cust3,merchantB,2021-12-31,Visa,300
cust4,merchantB,2021-12-29,MasterCard,200
```
Output 2
```
merchant_id,card_type,payout_date,amount
merchantA,MasterCard,2021-12-29,50
merchantA,Visa,2021-12-29,150
merchantB,Visa,2021-12-31,300
merchantB,MasterCard,2021-12-29,200
```

Part 2
In Brazil, settlement times can take up to 30 days for domestic card transaction. i.e. A merchant selling items online
will receive their money from a customer after a month of selling an item. This has created a need where merchants
are looking for ways to receive their money faster.
Per the regulations, merchants can sell their receivables to a financial institution. The financial institution
will pay the funds to the merchant earlier and receive the funds from Stripe instead on the payout date.
An agreement between the merchant and a financial institution is called a contract. Stripe is obliged to respect
those contracts and update the registered receivables. Each contract is mapped to one receivable based on the
same 3 identifiers as above:
* merchant_id (String): The id of the merchant on Stripe side.
* card_type (String): The type of the card used for the transaction (e.g. Visa)
* payout_date (String): String date of the funds available to the merchant by Stripe.
A contract sent to Stripe is represented as follows:
```
Contract {
    string contract_id
    string merchant_id
    string payout_date
    string card_type
    integer amount
}
```
Implement update_receivables function that takes the list of registered receivables from part 1 and 
additional parameter of list of contracts.
The result should be the updated list of receivables.
For each contract, a receivable should be created for the contract id, and the corresponding merchant receivable 
should be removed.
Example input 1:
Transactions:
```
customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-05,Visa,300
cust2,merchantA,2022-01-05,Visa,200
cust3,merchantB,2022-01-06,MasterCard,1000
```
Contracts:
```
contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-05,Visa,500
```
=> update_receivables(registered_receivables, input_contracts)
Output 1:
```
id,card_type,payout_date,amount
contract1,Visa,2022-01-05,500
merchantB,MasterCard,2022-01-06,1000
```
Example input 2:
Transactions:
```
customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-07,Visa,500
cust2,merchantA,2022-01-07,Visa,250
cust3,merchantB,2022-01-08,MasterCard,1250
cust4,merchantC,2022-01-09,Visa,1500
```
Contracts:
```
contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-07,Visa,750
contract2,merchantC,2022-01-09,Visa,1500
```
=> update_receivables(registered_receivables, input_contracts)
Output 2:
```
id,card_type,payout_date,amount
contract1,Visa,2022-01-07,750
contract2,Visa,2022-01-09,1500
merchantB,MasterCard,2022-01-08,1250
```
'''

import csv
from collections import defaultdict
from io import StringIO

def register_receivables(input_csv_string):
    # Parse the CSV string
    transactions = []
    f = StringIO(input_csv_string)
    reader = csv.DictReader(f)
    for row in reader:
        # Each row represents a transaction
        transaction = {
            'customer_id': row['customer_id'],
            'merchant_id': row['merchant_id'],
            'payout_date': row['payout_date'],
            'card_type': row['card_type'],
            'amount': int(row['amount'])
        }
        transactions.append(transaction)

    # Aggregate transactions per merchant_id, card_type, payout_date
    receivables_dict = defaultdict(int)
    for txn in transactions:
        key = (txn['merchant_id'], txn['card_type'], txn['payout_date'])
        receivables_dict[key] += txn['amount']

    # Prepare the aggregated receivables
    receivables = []
    for key, amount in receivables_dict.items():
        merchant_id, card_type, payout_date = key
        receivable = {
            'merchant_id': merchant_id,
            'card_type': card_type,
            'payout_date': payout_date,
            'amount': amount
        }
        receivables.append(receivable)

    # Print the registered receivables
    print('merchant_id,card_type,payout_date,amount')
    for receivable in receivables:
        print(f"{receivable['merchant_id']},{receivable['card_type']},{receivable['payout_date']},{receivable['amount']}")

    return receivables

def update_receivables(registered_receivables, contracts_csv_string):
    # Parse the contracts CSV string
    contracts = []
    f = StringIO(contracts_csv_string)
    reader = csv.DictReader(f)
    for row in reader:
        contract = {
            'contract_id': row['contract_id'],
            'merchant_id': row['merchant_id'],
            'payout_date': row['payout_date'],
            'card_type': row['card_type'],
            'amount': int(row['amount'])
        }
        contracts.append(contract)

    # Convert registered receivables to a dictionary for easy lookup
    receivables_dict = {}
    for receivable in registered_receivables:
        key = (receivable['merchant_id'], receivable['card_type'], receivable['payout_date'])
        receivables_dict[key] = {
            'id': receivable['merchant_id'],  # Use 'merchant_id' as 'id' for consistency
            'card_type': receivable['card_type'],
            'payout_date': receivable['payout_date'],
            'amount': receivable['amount']
        }

    # Update receivables based on contracts
    for contract in contracts:
        key = (contract['merchant_id'], contract['card_type'], contract['payout_date'])
        # Remove the merchant receivable
        if key in receivables_dict:
            del receivables_dict[key]
        # Add the contract receivable
        receivables_dict[(contract['contract_id'], contract['card_type'], contract['payout_date'])] = {
            'id': contract['contract_id'],
            'card_type': contract['card_type'],
            'payout_date': contract['payout_date'],
            'amount': contract['amount']
        }

    # Prepare the updated receivables
    updated_receivables = list(receivables_dict.values())

    # Print the updated receivables
    print('id,card_type,payout_date,amount')
    for receivable in updated_receivables:
        print(f"{receivable['id']},{receivable['card_type']},{receivable['payout_date']},{receivable['amount']}")

    return updated_receivables

# Example usage for Part 1:

# Example input 1:
input_csv_1 = '''customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-30,Visa,150
cust2,merchantA,2021-12-30,Visa,200
cust3,merchantB,2021-12-31,MasterCard,300
cust4,merchantA,2021-12-30,Visa,50
'''

print("Output 1:")
register_receivables(input_csv_1)

# Example input 2:
input_csv_2 = '''customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-29,MasterCard,50
cust2,merchantA,2021-12-29,Visa,150
cust3,merchantB,2021-12-31,Visa,300
cust4,merchantB,2021-12-29,MasterCard,200
'''

print("\nOutput 2:")
register_receivables(input_csv_2)

# Example usage for Part 2:

# Example input 1:
transactions_csv = '''customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-05,Visa,300
cust2,merchantA,2022-01-05,Visa,200
cust3,merchantB,2022-01-06,MasterCard,1000
'''

contracts_csv = '''contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-05,Visa,500
'''

print("\nUpdated Receivables Output 1:")
registered_receivables = register_receivables(transactions_csv)
update_receivables(registered_receivables, contracts_csv)

# Example input 2:
transactions_csv_2 = '''customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2022-01-07,Visa,500
cust2,merchantA,2022-01-07,Visa,250
cust3,merchantB,2022-01-08,MasterCard,1250
cust4,merchantC,2022-01-09,Visa,1500
'''

contracts_csv_2 = '''contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-07,Visa,750
contract2,merchantC,2022-01-09,Visa,1500
'''

print("\nUpdated Receivables Output 2:")
registered_receivables = register_receivables(transactions_csv_2)
update_receivables(registered_receivables, contracts_csv_2)
