principal = 100
monthly_rate = 0.00417
account_value = 0

for i in range (1, 7):
    account_value += (principal) * (1 + monthly_rate)
    print(account_value)
