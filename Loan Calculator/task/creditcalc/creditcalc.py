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