balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
while month < 12:
    month += 1
    minimum_paid = monthlyPaymentRate * balance
    unpaid_b = balance - minimum_paid
    interest = (annualInterestRate / 12) * unpaid_b
    balance = unpaid_b + interest
    balance = round(balance, 2)
    print('Month ', month, 'Remaining balance is', balance)

print('Remaining Balance:', balance)
