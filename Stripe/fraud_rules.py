'''
Certain colleagues upstairs have let us know that our policy of approving every Authorization Request 
is frowned upon by our investors. Luckily, they informed us of a separate system that our data science 
department built which can detect Authorization Requests that are fraudulent. 

With fraud, the data scientists say, nothing is set in stone. The criteria for fraud change constantly, 
so their system develops new Fraud Rules all the time. They've given us access to their system's stream 
of Fraud Rules, in the following format:
time, field, value
1,merchant,bobs_burgers
20,card_number,4242111111111111

The first Fraud Rule indicates: "from 1 second onward, any Authorization Request with merchant of 
bobs_burgers is fraudulent."
The second indicates: "from 20 seconds onward, any Authorization Request with card_number of 
4242111111111111 is fraudulent."

Once a Fraud Rule is introduced, it is applicable in perpetuity. A new Fraud Rule cannot be applied 
to a previous request.

Example:
TIME EVENT
*      5 fraud rule A    <-- can apply to R3, R4, and R5
|     10 request R3
|     20 request R4
| *   30 fraud rule B    <-- can only apply to R5
| |   40 request R5
v v * 45 fraud rule C    <-- does not apply to R3, R4, R5

Integrate Fraud Rule data: REJECT fraudulent Authorization Requests.

For the same input as before:
timestamp_seconds, unique_id, amount, card_number, merchant
5,R1,5.60,4242424242424242,bobs_burgers
10,R2,500.00,4242111111111111,a_corp

And the fraud rule input:
time, field, value
1,merchant,bobs_burgers
20,card_number,4242111111111111

The expected report:
5 R1 5.60 REJECT
10 R2 500.00 APPROVE
'''
def fraud_rules(transactions, fraud_rules):
    events = []
    fraud_dic = {}
    report = []