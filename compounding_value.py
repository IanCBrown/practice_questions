principal = 100
monthly_rate = 0.00417
account_value = 0 

for i in range (1, 7):
    if i == 1:
        account_value = ((1 + monthly_rate) * principal)
    else:
        account_value += (principal) * (1 + monthly_rate)
    print(account_value)

