# Problem Set 1
# Name: Mia Gaulin
# Collaborators: None
# Time Spent: ~30 minutes
# Date: August 24, 2016

initialBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

monthlyPayment = 0
monthlyInterestRate = annualInterestRate / 12
balance = initialBalance

while balance > 0:
    monthlyPayment += 10
    balance = initialBalance
    numMonths = 0

    while numMonths < 12 and balance > 0:
        numMonths += 1
        interest = monthlyInterestRate * balance
        balance -= monthlyPayment
        balance += interest

balance = round(balance,2)

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', monthlyPayment
print 'Number of months needed:', numMonths
print 'Balance:', balance
