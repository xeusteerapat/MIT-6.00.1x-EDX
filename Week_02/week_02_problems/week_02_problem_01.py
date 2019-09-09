def pay_dept(b, a, m):
    unpaid_b = 0
    interest = 0
    minimum_paid = 0
    month = 0
    while month < 13:
        month += 1
        minimum_paid = m * b
        unpaid_b = b - minimum_paid
        interest = (a / 12) * b
        b = unpaid_b + interest
        print('Month ', month, 'Remaining balance is', b)
    return b


print(pay_dept(42, 0.2, 0.04))
