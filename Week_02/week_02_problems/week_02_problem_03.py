balance = 999999
annualInterestRate = 0.18
current_balance = balance
monthly_interest_rate = annualInterestRate / 12
lower_payment = balance / 12
upper_payment = (balance * (1 + monthly_interest_rate)**12) / 12
month = 1
epsilon = 0.01

while abs(current_balance - balance) <= epsilon:
    middle_payment = (lower_payment + upper_payment) / 2
    for i in range(12):
        month += i
        unpaid_b = current_balance - middle_payment
        interest = round((annualInterestRate / 12) * unpaid_b, 2)
        current_balance = round((unpaid_b + interest), 2)
    if abs(current_balance) <= epsilon:
        print('Lowest Payment:', round(middle_payment, 2))
    elif current_balance < 0:
        current_balance = balance
        upper_payment = middle_payment
    else:
        current_balance = balance
        lower_payment = middle_payment
