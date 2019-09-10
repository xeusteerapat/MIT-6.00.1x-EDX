balance = 3926
current_balance = balance
annualInterestRate = 0.2
minimum_paid = 10
month = 0
while current_balance >= 0:
    for i in range(12):
        month += 1
        unpaid_b = current_balance - minimum_paid
        interest = (annualInterestRate / 12) * unpaid_b
        current_balance = unpaid_b + interest
        current_balance = round(current_balance, 2)
        print('month:', month, current_balance)
    if current_balance <= 0:
        print('Lowest Payment:', minimum_paid)
    else:
        minimum_paid += 10
        current_balance = balance
