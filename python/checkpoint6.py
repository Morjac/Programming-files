# py checkpoint6.py

loan = int(input('How large is the loan (on a scale of 1-10)? '))

credit = int(input('How good is your credit history (on a scale of 1-10)? '))

income = int(input('How high is your income (on a scale of 1-10)? '))

down_payment = int(input('How large is your down payment (on a scale of 1-10)? '))

is_loan = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        is_loan = True
    
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            is_loan = True
    
    elif credit < 7 or income < 7:
        is_loan = False

elif loan < 5:
    if credit < 4:
        is_loan = False
    
    elif income >= 7 or down_payment >= 7:
        is_loan = True
        if income >= 4 and down_payment >=4:
            is_loan = True
    else:
        is_loan = False
else:
    is_loan = False


if is_loan:
    print('Yes, you approve for a loan')

elif not is_loan:
    print('No, you dont approve for a loan')