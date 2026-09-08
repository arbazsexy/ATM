balance = float(input("Enter an initial balance: "))

deposit = float(input("Enter the amount you want to deposit: "))

new_balance = balance + deposit

print("Current balance:", new_balance)

withdraw = float(input("Enter the amount to withdraw: "))

new_balance = new_balance - withdraw

print("Balance after withdrawal:", new_balance)
