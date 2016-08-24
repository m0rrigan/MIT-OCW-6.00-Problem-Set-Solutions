# Problem Set 1
# Name: Mia Gaulin
# Collaborators: None
# Time Spent: ~1 hour
# Date: August 24, 2016

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
minMonthlyPaymentRate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

monthlyInterestRate = annualInterestRate / 12

numMonths = 1
totalAmtPaid = 0

while numMonths <= 12:
    minPayment = round(minMonthlyPaymentRate * balance,2)
    totalAmtPaid += minPayment
    interestPaid = round(monthlyInterestRate * balance,2)
    principlePaid = minPayment - interestPaid
    balance -= principlePaid

    print 'Month:', numMonths
    print 'Minimum monthly payment:', minPayment
    print 'Principle paid:', principlePaid
    print 'Remaining balance:', balance

    numMonths += 1

print 'RESULT'
print 'Total amount paid:', totalAmtPaid
print 'Remaining balance:', balance
