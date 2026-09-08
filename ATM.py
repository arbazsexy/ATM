Balance = input("Enter an initial balance:");
Deposit = input("Enter the amount you want to deposit:");

NewBalance = Balance + Deposit;

print("Current balance:",NewBalance);

withdraw = input("Enter the amount to withdraw:");
NewBalance  = NewBalance - withdraw;

print("Balance after withdraw:",NewBalance);
