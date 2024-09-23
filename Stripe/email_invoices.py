# https://www.1point3acres.com/bbs/thread-1076365-1-1.html
'''
At Stripe, we send a lot of invoices. For each invoice, we send multiple reminder emails. 
For this question, you will be outputting the subject line of each email we send for customers' 
invoices in sorted order. (Use any library/tool for sorting).

Your invoicing system will need to be able to configure a reminder schedule. 
For example, you might want to send one email 10 days before the invoice comes out, 
one email when the invoice comes out, one email 10 days before the invoice is due, and 
one email when the invoice is due, which is 30 days from when the invoice first came out. 
This send schedule could look something like this, corresponding to the diagram below:

     │
t=-10│[Upcoming] Invoice for Alice
     │
t=0  │[New] Invoice for Alice
     │
t=20 │[Reminder] Invoice for Alice
     │
t=30 │[Due] Invoice for Alice
     │
     ▼

Given a configuration for sending emails, your input will be an unsorted list of unique 
customer invoices with times for when their `[New]` invoice should come out and how much 
we are charging them in dollars. Your objective is to print out the subject lines of all 
emails we will send out in sorted order by time. Your output should include the time, the 
type of email, the customer, and amount due.

Here is a sample of how your system should behave:

send_schedule = {
  -10: "Upcoming",
  0: "New",
  20: "Reminder",
  30: "Due"
}

invoicer = Invoicer.new(send_schedule)

customer_invoices = [
    {"invoice_time": 0, "name": "Alice", "amount": 200},
    {"invoice_time": 1, "name": "Bob", "amount": 100},
]
invoicer.send_emails(customer_invoices)

Output:
-10: [Upcoming] Invoice for Alice for 200 dollars
-9: [Upcoming] Invoice for Bob for 100 dollars
0: [New] Invoice for Alice for 200 dollars
1: [New] Invoice for Bob for 100 dollars
20: [Reminder] Invoice for Alice for 200 dollars
21: [Reminder] Invoice for Bob for 100 dollars
30: [Due] Invoice for Alice for 200 dollars
31: [Due] Invoice for Bob for 100 dollars
'''
class Invoicer:
    def __init__(self, send_schedule):
        self.send_schedule = send_schedule

    def send_emails(self, customer_invoices, customer_payments=None):
        invoices = []
        for invoice in customer_invoices:
            print(invoice)
            time, user, amount = invoice["invoice_time"], invoice["name"], invoice["amount"]
            time_list = []
            for send_time, _ in self.send_schedule.items():
                time_list.append(send_time)
            for t in time_list:
                invoices.append((t, f"{t + time}: [{self.send_schedule[t]}] Invoice for {user} for {amount} dollars"))

        invoices.sort(key=lambda x: x[0])
        for invoice in invoices:
            print(invoice[1])

send_schedule = {
  -10: "Upcoming",
  0: "New",
  20: "Reminder",
  30: "Due"
}
invoicer = Invoicer(send_schedule)
customer_invoices = [
    {"invoice_time": 0, "name": "Alice", "amount": 200},
    {"invoice_time": 1, "name": "Bob", "amount": 100},
]
invoicer.send_emails(customer_invoices)

'''
Part 2 
Customers sometimes make a series of payments to pay their invoice.  
In this part, you will have an unsorted list of payments made by the customers, 
specifying their name, time of payment, and payment amount. Each subject line should 
now accurately reflect how much money is still owed by the customer. For example, if 
Bob pays half of his invoice right when it comes out, his next reminder email will say 
that he owes 50 dollars, not 100. If a customer has fully paid their invoice, we do not 
want to send them any more emails. In addition to returning the sequence of emails sent, 
you will also need to return a list of delinquent customers, those who did not fully pay 
their invoice before the due date, and how much they owe.

customer_invoices = [
    {"invoice_time": 0, "name": "Alice", "amount": 200},
    {"invoice_time": 1, "name": "Bob", "amount": 100},
]
customer_payments = [
    {"payment_time": -9, "name": "Alice", "amount": 100},
    {"payment_time": 1, "name": "Alice", "amount": 50},
    {"payment_time": 0, "name": "Bob", "amount": 100},
]
invoicer.send_emails(customer_invoices, customer_payments)

Output:
-10: [Upcoming] Invoice for Alice for 200 dollars
-9: [Upcoming] Invoice for Bob for 100 dollars
0: [New] Invoice for Alice for 100 dollars
20: [Reminder] Invoice for Alice for 50 dollars
30: [Due] Invoice for Alice for 50 dollars
Delinquent customers:
Alice owes 50 dollars
'''

from collections import defaultdict

class Invoicer:
    def __init__(self, send_schedule):
        self.send_schedule = send_schedule

    def send_emails(self, customer_invoices, customer_payments=None):
        # Initialize a dictionary to store how much each customer owes
        customer_debt = {invoice["name"]: invoice["amount"] for invoice in customer_invoices}
        # If payments are provided, adjust customer debts accordingly
        if customer_payments:
            self._process_payments(customer_debt, customer_payments)

        emails = []
        # Generate email subject lines based on invoice times and send schedule
        for invoice in customer_invoices:
            name = invoice["name"]
            amount = customer_debt[name]
            invoice_time = invoice["invoice_time"]
            print(name)
            for offset, email_type in self.send_schedule.items():
                send_time = invoice_time + offset
                if amount > 0:  # Only send emails if the customer still owes money
                    emails.append((send_time, f"{send_time}: [{email_type}] Invoice for {name} for {amount} dollars"))
        
        # Sort emails by time
        emails.sort(key=lambda x: x[0])

        # Print sorted emails
        for email in emails:
            print(email[1])

        # Delinquency check (for part 2)
        if customer_payments:
            self._check_delinquency(customer_invoices, customer_debt)

    def _process_payments(self, customer_debt, customer_payments):
        # Process payments by subtracting amounts from the customer's debt
        for payment in customer_payments:
            name = payment["name"]
            amount_paid = payment["amount"]
            customer_debt[name] -= amount_paid

    def _check_delinquency(self, customer_invoices, customer_debt):
        delinquent_customers = []
        for invoice in customer_invoices:
            name = invoice["name"]
            amount_owed = customer_debt[name]
            if amount_owed > 0:
                delinquent_customers.append(f"{name} owes {amount_owed} dollars")
        
        # Print delinquent customers
        if delinquent_customers:
            print("Delinquent customers:")
            for delinquent in delinquent_customers:
                print(delinquent)

# Sample usage:

send_schedule = {
    -10: "Upcoming",
    0: "New",
    20: "Reminder",
    30: "Due"
}

# Customer invoices
customer_invoices = [
    {"invoice_time": 0, "name": "Alice", "amount": 200},
    {"invoice_time": 1, "name": "Bob", "amount": 100},
]

# Payments made by customers
customer_payments = [
    {"payment_time": -9, "name": "Alice", "amount": 100},
    {"payment_time": 1, "name": "Alice", "amount": 50},
    {"payment_time": 0, "name": "Bob", "amount": 100},
]

invoicer = Invoicer(send_schedule)
# invoicer.send_emails(customer_invoices, customer_payments)
