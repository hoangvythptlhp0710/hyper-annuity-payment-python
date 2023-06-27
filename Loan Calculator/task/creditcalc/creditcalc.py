""" stage 1:
loan_principal = 'Loan principal: 1000'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
final_output = 'The loan has been repaid!'
print(loan_principal + '\n' + first_month + '\n' + second_month + '\n' + third_month + '\n' + final_output)
"""
# write your code here

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
""" stage 3: 
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

"""

# write your code here
""" stage 4:
"""
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, required=False, help="type of payment")
parser.add_argument("--principal", type=int, required=False, help="principal")
parser.add_argument("--periods", type=int, required=False, help="number of periods")
parser.add_argument("--interest", type=float, required=False, help="interest")
parser.add_argument("--payment", type=int, required=False, help="payment")

args = vars(parser.parse_args())

type_ = args["type"]
a = args["payment"]
p = args["principal"]
interest = args["interest"]
n = args["periods"]

if (type_ is None) or (type_ == "diff" and a is not None) or (interest is None) or (n is not None and n < 0):
    print("Incorrect parameters")
else:
    i = interest / (12 * 100)
    if type_ == "diff":
        overpayment = p
        for m in range(1, n + 1):
            d1 = math.ceil(p / n + i * (p - p * (m - 1) / n))
            overpayment -= d1
            print(f"Month {m}: paid out {d1}")
        print(f"\r\nOverpayment = {abs(overpayment)}")
    elif type_ == "annuity":
        if n is None:
            n = math.ceil(math.log(a / (a - i * p), 1 + i))
            years = n // 12
            months = n % 12
            print(f"You need {years} years and {months} months to repay this credit!")
        elif p is None:
            p = math.floor(a / (i / (1 - 1 / math.pow(1 + i, n))))
            print(f"Your credit principal = {p}!")
        else:
            a = math.ceil(p * i / (1 - 1 / math.pow(1 + i, n)))
            print(f"Your annuity payment = {a}!")
        overpayment = n * a - p
        print(f"Overpayment = {overpayment}")
