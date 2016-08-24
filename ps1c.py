# Problem Set 1
# Name: Mia Gaulin
# Collaborators: None
# Time Spent: ~45 minutes
# Date: August 24, 2016

initialBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

balance = initialBalance
lowPayment = balance / 12
highPayment = (balance * (1 + (annualInterestRate / 12)) ** 12) / 12

while True:
    balance = initialBalance
    monthlyPayment = (lowPayment + highPayment) / 2

    for month in range(1,13):
        interest = round(balance * annualInterestRate / 12, 2)
        balance += interest - monthlyPayment

        if balance <= 0:
            break

    if (highPayment - lowPayment < 0.005):
        print 'RESULT'
        monthlyPayment = round(monthlyPayment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(monthlyPayment,2)
        balance = initialBalance

        for month in range(1,13):
            interest = round(balance * annualInterestRate / 12, 2)
            balance += interest - monthlyPayment

            if balance <= 0:
                break

        print "Number of months needed:", month
        print "Balance:", round(balance,2)
        break

    elif balance < 0:
        highPayment = monthlyPayment
    else:
        lowPayment = monthlyPayment
