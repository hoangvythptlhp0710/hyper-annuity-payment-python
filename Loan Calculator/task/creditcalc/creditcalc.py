""" stage 1:
loan_principal = 'Loan principal: 1000'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
final_output = 'The loan has been repaid!'
print(loan_principal + '\n' + first_month + '\n' + second_month + '\n' + third_month + '\n' + final_output)
"""
# write your code here
import math

"""stage 2:
print("Enter the loan principal: ")
loanPrinciple = int(input())
print("What do you want to calculate?")
print('type "m" - for number of monthly payments,\ntype"p" - for the monthly payment:')
option = input()

if option == 'm':
    print("Enter the monthly payment: ")
    monthPayment = int(input())
    result = loanPrinciple / monthPayment
    month = int(result)
    if loanPrinciple % monthPayment == 0:
        if month == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(str.format(f"It will take {month} months to repay the loan"))
    else:
        print(str.format(f"It will take {month + 1} months to repay the loan"))
elif option == 'p':
    print("Enter the number of months: ")
    month = int(input())
    if loanPrinciple % month == 0:
        result = loanPrinciple / month
        monthlyPayment = int(result)
        print(str.format(f"Your monthly payment = {monthlyPayment}"))
    else:
        monthlyPayment = loanPrinciple / month
        annualPayment = round(monthlyPayment) + 1
        lastPayment = loanPrinciple - (annualPayment * (month - 1))
        print(str.format(f"Your monthly payment = {annualPayment} and the last payment = {lastPayment}"))
"""
# write your code here

import math

print(
    'What do you want to calculate?\ntype "n" for number of monthly payments,\ntype "a" for annuity monthly payment '
    'amount,\ntype "p" for loan principal: ')
loanInput = "Enter the loan interest: "
option = input()
if option == "n":
    print("Enter the loan principal: ")
    loanPrincipal = int(input())
    print("Enter the monthly payment: ")
    monthlyPayment = int(input())
    print(loanInput)
    loanInterest = float(input())
    i = (loanInterest / 100) / 12
    numberOfPayments = monthlyPayment / (monthlyPayment - (i * loanPrincipal))
    numberOfMonths = math.log(numberOfPayments, 1 + i)
    numberOfMonths = int(numberOfMonths) + 1
    months = int(numberOfMonths)
    years = int(numberOfMonths / 12)
    months = months - years * 12
    if years > 1:
        if 1 < months < 12:
            print(str.format(f"It will take {years} years and {months} months to repay this loan!", years, months))
        elif months == 12:
            print(str.format(f"It will take {years + 1} years to repay this loan!"))
        else:
            print(str.format(f"It will take {years} years and 1 month to repay this loan!"))

    elif years == 0:
        if months > 1:
            print(str.format(f"It will take {months} months to repay this loan!", months))
        elif months == 1:
            print("It will take 1 month to repay this loan")
    else:
        if 1 < months < 12:
            print(str.format(f"It will take 1 year and {months} months to repay this loan!", months))
        elif months == 1:
            print("It will take 1 year and 1 month to repay this loan")

elif option == "a":
    print("Enter the loan principal: ")
    loanPrincipal = int(input())
    print("Enter the number of periods: ")
    numberOfPeriods = int(input())
    print("Enter the loan interest: ")
    loanInterest = float(input()) / 12 / 100
    result = loanPrincipal * (loanInterest * (loanInterest + 1) ** numberOfPeriods) / (
            (1 + loanInterest) ** numberOfPeriods - 1)
    result = int(result) + 1
    print(str.format(f"Your monthly payment = {result}"))

else:
    print("Enter the annuity payment: ")
    annuityPayment = float(input())
    print("Enter the number of periods: ")
    numberOfPeriods = int(input())
    print("Enter the loan interest: ")
    loanInterest = float(input()) / 12 / 100
    result = (loanInterest * (loanInterest + 1) ** numberOfPeriods) / ((loanInterest + 1) ** numberOfPeriods - 1)
    loanPayment = int(annuityPayment / result)
    print(str.format(f"Your loan principal = {loanPayment}", loanPayment))
